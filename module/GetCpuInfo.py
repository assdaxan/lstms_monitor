#!/usr/bin/env python3
from module.Shell import Shell
from time import sleep, strftime
import re

class GetCpuInfo(Shell):
    def __init__(self):
        self.re_stat = re.compile(r'(?P<cpu_id>cpu\d*)(?: *)(?P<user>\d+)(?: *)(?P<nice>\d+)(?: *)(?P<system>\d+)(?: *)(?P<idle>\d+)(?: *)(?P<iowait>\d+)(?: *)(?P<irq>\d+)(?: *)(?P<softirq>\d+)(?: *)(?P<steal>\d+)(?: *)(?P<guest>\d+)(?: *)(?P<guest_nice>\d+)(?: *)')
        self.re_cpuinfo_model_name = re.compile(r'(?<=model name\t\: )([^\n]+)')

    def __get(self):
        cpu_info_dict = {}
        t = self.Command('cat /proc/stat')

        datas = self.re_stat.finditer(t)

        for data in datas:
            cpu_id = data.group('cpu_id')
            user = int(data.group('user'), 10)
            nice = int(data.group('nice'), 10)
            system = int(data.group('system'), 10)
            idle = int(data.group('idle'), 10)
            iowait = int(data.group('iowait'), 10)
            irq = int(data.group('irq'), 10)
            softirq = int(data.group('softirq'), 10)
            steal = int(data.group('steal'), 10)

            Total_CPU_time = user+nice+system+idle+iowait+irq+softirq+steal
            Total_CPU_Idle_time = idle + iowait

            cpu_info_dict.update({cpu_id : {'Total_CPU_time':Total_CPU_time, 'Total_CPU_Idle_time':Total_CPU_Idle_time}})

        return cpu_info_dict
    
    def GetUsage(self):
        usage_dict = {}

        datetime_ = strftime("%Y-%m-%d %H:%M:%S")
        PrevTotal = self.__get()
        sleep(10)
        Total = self.__get()
        CPUUsage = 0
        for cpu_id in Total.keys():
            diff_total = (Total[cpu_id]['Total_CPU_time'] - PrevTotal[cpu_id]['Total_CPU_time'])
            diff_idle = (Total[cpu_id]['Total_CPU_Idle_time'] - PrevTotal[cpu_id]['Total_CPU_Idle_time'])
            # diff_total = (Total[cpu_id]['Total_CPU_time'])
            # diff_idle = (Total[cpu_id]['Total_CPU_Idle_time'])
            CPUUsage = CPUUsage + ((diff_total - diff_idle) / diff_total * 100)
        CPUUsage = CPUUsage / len(Total.keys())
        usage_dict.update({'CPU':{"CPUUsage":CPUUsage, "datetime_":datetime_}})

        return usage_dict
        
    def GetCpuModelName(self):
        t = self.Command('cat /proc/cpuinfo | grep "model name"')
        return self.re_cpuinfo_model_name.findall(t)

if __name__ == "__main__":
    cpu = GetCpuInfo()

    print(cpu.GetCpuModelName())
    while(True):
        print(cpu.GetUsage())
        sleep(1)
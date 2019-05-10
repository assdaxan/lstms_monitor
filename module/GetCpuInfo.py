from subprocess import Popen, PIPE
from time import sleep
import re

class GetCpuInfo:
    def __init__(self):
        self.re_info = re.compile(r'(?P<cpu_id>cpu\d*)(?: *)(?P<user>\d+)(?: *)(?P<nice>\d+)(?: *)(?P<system>\d+)(?: *)(?P<idle>\d+)(?: *)(?P<iowait>\d+)(?: *)(?P<irq>\d+)(?: *)(?P<softirq>\d+)(?: *)(?P<steal>\d+)(?: *)(?P<guest>\d+)(?: *)(?P<guest_nice>\d+)(?: *)')

    def __get(self):
        cpu_info_dict = {}
        p = Popen('cat /proc/stat', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        t = p.stdout.read().decode('utf8')

        datas = self.re_info.finditer(t)

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

        PrevTotal = self.__get()
        sleep(1)
        Total = self.__get()

        for cpu_id in Total.keys():
            diff_total = (Total[cpu_id]['Total_CPU_time'] - PrevTotal[cpu_id]['Total_CPU_time'])
            diff_idle = (Total[cpu_id]['Total_CPU_Idle_time']-PrevTotal[cpu_id]['Total_CPU_Idle_time'])
            cpu_usage = (diff_total - diff_idle) / diff_total * 100

            usage_dict.update({cpu_id:cpu_usage})

        return usage_dict
        

if __name__ == "__main__":
    cpu = GetCpuInfo()

    while(True):
        print(cpu.GetUsage())
        sleep(1)
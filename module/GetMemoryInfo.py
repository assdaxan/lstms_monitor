#!/usr/bin/env python3
from module.Shell import Shell
from time import strftime
import re

class GetMemoryInfo(Shell):
    def __init__(self):
        self.re_info = re.compile(r'([\w\(\)_]+)(?:\:)(?: *)(\d+)(?: *)(?:kB)?')
        self.memory_info_dict = {}

    def Get(self):
        self.memory_info_dict.clear()

        t = self.Command('cat /proc/meminfo')
        datas = self.re_info.findall(t)

        for data in datas:
            self.memory_info_dict.update({data[0]:int(data[1], 10)})
    
    def GetUsage(self):
        self.Get()
        MemTotal = self.memory_info_dict['MemTotal']
        MemFree  = self.memory_info_dict['MemFree']
        Inactive = self.memory_info_dict['Inactive']

        datetime_ = strftime("%Y-%m-%d %H:%M:%S")

        return {'MemTotal':MemTotal,
                'MemFree':MemFree,
                'Inactive':Inactive,
                'MemUsage':(MemTotal - (MemFree + Inactive)) / MemTotal * 100,
                'datetime_':datetime_
                }
        

if __name__ == "__main__":
    memory = GetMemoryInfo()
    info = memory.GetUsage()
    print(info)
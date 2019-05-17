#!/usr/bin/env python3
from module.Shell import Shell
import re

class GetDiskInfo(Shell):
    def __init__(self):
        self.re_info = re.compile(r'(?P<Filesystem>[^ \n]+)(?: *)(?P<Size>\d+)(?: *)(?P<Used>\d+)(?: *)(?P<Available>\d+)(?: *)(?P<Percent>\d+)(?:%)(?: *)(?P<Mounted>[^\n]+)')
        self.disk_info_dict = {}

    def Get(self):
        self.disk_info_dict.clear()

        t = self.Command('df -lk')

        datas = self.re_info.finditer(t)

        for data in datas:
            Filesystem = data.group('Filesystem')
            if '/dev/loop' not in Filesystem:
                Size = data.group('Size')
                Used = data.group('Used')
                Available = data.group('Available')
                Percent = data.group('Percent')
                Mounted = data.group('Mounted')
                self.disk_info_dict.update({Mounted:{'Size':Size, 'Used':Used, 'Available':Available, 'Percent':Percent, 'Filesystem':Filesystem}})

        return self.disk_info_dict
        

if __name__ == "__main__":
    disk = GetDiskInfo()
    info = disk.Get()
    print(info)
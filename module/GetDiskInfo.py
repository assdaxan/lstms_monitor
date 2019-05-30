#!/usr/bin/env python3
from module.Shell import Shell
from time import strftime
import re

class GetDiskInfo(Shell):
    def __init__(self):
        self.re_info = re.compile(r'(?P<Filesystem>[^ \n]+)(?: *)(?P<Size>\d+)(?: *)(?P<Used>\d+)(?: *)(?P<Available>\d+)(?: *)(?P<Percent>\d+)(?:%)(?: *)(?P<Mounted>[^\n]+)')
        self.disk_info_dict = {}

    def Get(self):
        self.disk_info_dict.clear()

        datetime_ = strftime("%Y-%m-%d %H:%M:%S")
        t = self.Command('df -lm')

        datas = self.re_info.finditer(t)

        for data in datas:
            Filesystem = data.group('Filesystem')
            if '/dev/loop' in Filesystem:
                pass
            elif 'tmpfs' == Filesystem:
                pass
            else:
                Size = data.group('Size')
                Used = data.group('Used')
                Available = data.group('Available')
                Percent = data.group('Percent')
                Mounted = data.group('Mounted')
                self.disk_info_dict.update({Mounted:{'Size':Size, 'Used':Used, 'Available':Available, 'Percent':Percent, 'Filesystem':Filesystem, 'datetime_':datetime_}})

        return self.disk_info_dict
        

if __name__ == "__main__":
    disk = GetDiskInfo()
    info = disk.Get()
    print(info)
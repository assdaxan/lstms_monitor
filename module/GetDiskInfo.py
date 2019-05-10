#!/usr/bin/env python3
from subprocess import Popen, PIPE
import re

class GetDiskInfo:
    def __init__(self):
        self.re_info = re.compile(r'(?P<Filesystem>[^ \n]+)(?: *)(?P<Size>\d+)(?: *)(?P<Used>\d+)(?: *)(?P<Available>\d+)(?: *)(?P<Percent>\d+)(?:%)(?: *)(?P<Mounted>[^\n]+)')
        self.disk_info_dict = {}

    def Get(self):
        self.disk_info_dict.clear()

        p = Popen('df -lk', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        t = p.stdout.read().decode('utf8')

        datas = self.re_info.finditer(t)

        for data in datas:
            Filesystem = data.group('Filesystem')
            if '/dev/loop' not in Filesystem:
                Size = data.group('Size')
                Used = data.group('Used')
                Available = data.group('Available')
                Percent = data.group('Percent')
                Mounted = data.group('Mounted')
                self.disk_info_dict.update({Filesystem:{'Size':Size, 'Used':Used, 'Available':Available, 'Percent':Percent, 'Mounted':Mounted}})

        return self.disk_info_dict
        

if __name__ == "__main__":
    disk = GetDiskInfo()
    info = disk.Get()
    print(info)
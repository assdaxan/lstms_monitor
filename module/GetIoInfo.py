#!/usr/bin/env python3
from Shell import Shell
import re

class GetIoInfo(Shell):
    def __init__(self):
        self.re_stat = re.compile(r'(?: *)(?:\d+)(?: *)(?:\d+)(?: *)(?P<dev>[\w\d]+)(?: *)(?P<reads>\d+)(?: *)(?P<rd_mrg>\d+)(?: *)(?P<rd_sectors>\d+)(?: *)(?P<ms_reading>\d+)(?: *)(?P<writes>\d+)(?: *)(?P<wr_mrg>\d+)(?: *)(?P<wr_sectors>\d+)(?: *)(?P<ms_writing>\d+)(?: *)(?P<cur_ios>\d+)(?: *)(?P<ms_doing_io>\d+)(?: *)(?P<ms_weighted>\d+)')
        self.io_info_dict = {}

    def Get(self):
        self.io_info_dict.clear()

        t = self.Command('cat /proc/diskstats')
        
        datas = self.re_stat.finditer(t)
        
        for data in datas:
            dev = data.group('dev')
            if 'loop' not in dev:
                ms_reading = data.group('ms_reading')
                ms_writing = data.group('ms_writing')

                self.io_info_dict.update({dev:{'ms_reading':ms_reading, 'ms_writing':ms_writing}})

        return self.io_info_dict


if __name__ == '__main__':
    io = GetIoInfo()
    result = io.Get()
    
    print(result)

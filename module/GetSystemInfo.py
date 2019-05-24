#!/usr/bin/env python3
from module.Shell import Shell
from time import strftime

class GetSystemInfo(Shell):
    def Get(self):
        t = self.Command('uname -n -r -o')
        t = t.strip()
        datas = t.split(' ')

        return {'hostname':datas[0], 'kernel':datas[1], 'os':datas[2]}
        

if __name__ == "__main__":
    system = GetSystemInfo()
    info = system.Get()
    print(info)
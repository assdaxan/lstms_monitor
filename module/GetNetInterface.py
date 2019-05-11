#!/usr/bin/env python3
from Shell import Shell
import re

class GetNetInterface(Shell):
    def __init__(self):
        self.re_interface_info = re.compile(r'((\w+)(?:: )(?:.*)(?:(?:\n {8}).*)*)')
        self.re_interface_inet = re.compile(r'(inet)(?: *)(?P<address>(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))')
        self.re_interface_inet6 = re.compile(r'(?:inet6)(?: *)(?P<address>(?:(?:[a-f0-9]{0,4}):?){6})')

    def Get(self):
        interface_dict = {}
        t = self.Command('ifconfig -a')

        for data in self.re_interface_info.findall(t):
            interface_name = data[1]
            try:
                interface_inet = self.re_interface_inet.search(data[0]).group('address')
            except AttributeError:
                interface_inet = ''
            try:
                interface_inet6 = self.re_interface_inet6.search(data[0]).group('address')
            except AttributeError:
                interface_inet6 = ''
            interface_dict.update({interface_name:{'inet4':interface_inet, 'inet6':interface_inet6}})

        return interface_dict


if __name__ == "__main__":
    NetInter = GetNetInterface()
    interface_dict = NetInter.Get()
    for interface in interface_dict.items():
        print(interface)

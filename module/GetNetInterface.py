from subprocess import Popen, PIPE
import re

class GetNetInterface:
    def __init__(self):
        self.interface_info = re.compile('((\w+)(?:: )(?:.*)(?:(?:\n {8}).*)*)')
        self.interface_inet = re.compile('(inet)(?: *)((?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]))')
        self.interface_inet6 = re.compile('(?:inet6)(?: *)((?:(?:[a-f0-9]{0,4}):?){6})')

    def Get(self):
        interface_dict = {}
        self.P = Popen('ifconfig -a', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        self.stdout = self.P.stdout.read().decode('utf-8')

        for data in self.interface_info.findall(self.stdout):
            interface_name = data[1]
            try:
                interface_inet = self.interface_inet.search(data[0]).group(2)
            except AttributeError:
                interface_inet = ''

            try:
                interface_inet6 = self.interface_inet6.search(data[0]).group(1)
            except AttributeError:
                interface_inet6 = ''
            interface_dict.update({interface_name:{'inet4':interface_inet, 'inet6':interface_inet6}})

        return interface_dict


if __name__ == "__main__":
    NetInter = GetNetInterface()
    interface_dict = NetInter.Get()
    for interface in interface_dict.items():
        print(interface)

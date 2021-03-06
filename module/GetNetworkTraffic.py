#!/usr/bin/env python3
from time import sleep, strftime

class GetNetworkTraffic:
    def __init__(self, interface_name, interface_ip):
        self.interface_ip = interface_ip
        self.interface_name = interface_name
        self.RX_PATH = f'/sys/class/net/{self.interface_name}/statistics/rx_bytes'
        self.TX_PATH = f'/sys/class/net/{self.interface_name}/statistics/tx_bytes'

    def Get(self):
        def get(PATH):
            with open(PATH) as f:
                return int(f.read(), 10)

        before_rx = get(self.RX_PATH)
        before_tx = get(self.TX_PATH)
        sleep(10)
        after_rx = get(self.RX_PATH)
        after_tx = get(self.TX_PATH)

        datetime_ = strftime("%Y-%m-%d %H:%M:%S")

        return {self.interface_name : {'datetime_':datetime_ ,'rx' : (after_rx - before_rx) / 1024, 'tx' : (after_tx - before_tx) / 1024, 'ip':self.interface_ip}}


if __name__ == "__main__":
    t = GetNetworkTraffic('wlp0s20f3')
    print(t.Get())

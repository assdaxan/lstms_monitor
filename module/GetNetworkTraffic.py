from time import sleep
from . import GetNetInterface

class GetNetworkTraffic:
    def __init__(self):
        RX_PATH = '/sys/class/net/%s/statistics/rx_bytes'
        TX_PATH = '/sys/class/net/%s/statistics/tx_bytes'

        netinter = GetNetInterface()
        self.interface_dict = netinter.Get()

    def Get(self):
        def get(interface_name):
            with open(PATH) as f:
                return int(f.read(), 10)

        for interface_name in self.interface_dict.keys():
            before_rx = get(RX_PATH%interface_name)
            before_tx = get(TX_PATH%interface_name)
            sleep(3)
            after_rx = get(RX_PATH%interface_name)
            avter_tx = get(TX_PATH%interface_name)

            print(after_rx - before_rx)
            print(after_tx - after_tx)


if __name__ == "__main__":
    t = GetNetworkTraffic()
    t.Get()

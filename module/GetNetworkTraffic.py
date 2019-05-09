from time import sleep

class GetNetworkTraffic:
    def __init__(self, interface_name):
        self.interface_name = interface_name
        self.RX_PATH = f'/sys/class/net/{self.interface_name}/statistics/rx_bytes'
        self.TX_PATH = f'/sys/class/net/{self.interface_name}/statistics/tx_bytes'

    def Get(self):
        def get(PATH):
            with open(PATH) as f:
                return int(f.read(), 10)

        before_rx = get(self.RX_PATH)
        before_tx = get(self.TX_PATH)
        sleep(3)
        after_rx = get(self.RX_PATH)
        after_tx = get(self.TX_PATH)

        return {self.interface_name : {'rx' : after_rx - before_rx, 'tx' : after_tx - before_tx}}


if __name__ == "__main__":
    t = GetNetworkTraffic('wlp0s20f3')
    print(t.Get())

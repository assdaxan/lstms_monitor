import json
import urllib3
from module.GetNetInterface import GetNetInterface 
from module.GetNetworkTraffic import GetNetworkTraffic

with open('Token.conf', 'r') as f:
        token = f.read()

http = urllib3.PoolManager()

data = {}
NetInterface = GetNetInterface()
interfaces = NetInterface.Get()

for interface in interfaces:
        NetworkTraffic = GetNetworkTraffic(interface)
        data.update(NetworkTraffic.Get())

encoded_data = json.dumps(data).encode('utf-8')

r = http.request(
        'POST',
        'https://lstms.ubun.net/monitor/traffic.php',
        body=encoded_data,
        headers={'Content-Type': 'application/json',
                "token":token}
    )
print(r.data.decode('utf-8'))
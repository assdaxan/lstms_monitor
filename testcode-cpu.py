import json
import urllib3
from module.GetCpuInfo import GetCpuInfo

http = urllib3.PoolManager()

cpu = GetCpuInfo()
data = cpu.GetUsage()

encoded_data = json.dumps(data).encode('utf-8')

r = http.request(
        'POST',
        'https://lstms.ubun.net/monitor/cpu.php',
        body=encoded_data,
        headers={'Content-Type': 'application/json',
                "token":"asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdf"}
    )
print(r.data.decode('utf-8'))
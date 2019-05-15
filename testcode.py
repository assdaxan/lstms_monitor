import json
import urllib3
from module.GetMemoryInfo import GetMemoryInfo

http = urllib3.PoolManager()

mem = GetMemoryInfo()
data = mem.GetUsage()

encoded_data = json.dumps(data).encode('utf-8')

r = http.request(
        'POST',
        'http://203.234.19.91/monitor/memory.php',
        body=encoded_data,
        headers={'Content-Type': 'application/json',
                "token":"asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdf"}
    )
print(r.data.decode('utf-8'))
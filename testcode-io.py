import json
import urllib3
from module.GetIoInfo import GetIoInfo

http = urllib3.PoolManager()

io = GetIoInfo()
data = io.Get()

encoded_data = json.dumps(data).encode('utf-8')

r = http.request(
        'POST',
        'https://lstms.ubun.net/monitor/IO.php',
        body=encoded_data,
        headers={'Content-Type': 'application/json',
                "token":"asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdf"}
    )
print(r.data.decode('utf-8'))
import json
import urllib3
from module.GetUserInfo import GetUserInfo

with open('/etc/lstms_m/Token.conf', 'r') as f:
    token = f.read()

http = urllib3.PoolManager()

user = GetUserInfo()
data = user.Get()

encoded_data = json.dumps(data).encode('utf-8')

r = http.request(
        'POST',
        'https://lstms.ubun.net/monitor/user.php',
        body=encoded_data,
        headers={'Content-Type': 'application/json',
                "token":token}
    )
print(r.data.decode('utf-8'))
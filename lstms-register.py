import json
import urllib3
from os import path, system
from module.GetSystemInfo import GetSystemInfo

def login():
    print("LSTMS Login Please")
    ID = input("ID : ")
    PW = input("PW : ")

    return {'ID':ID, 'PW':PW}

CONF_FILE = '/etc/lstms_m/Token.conf'

if(path.exists(CONF_FILE) == True):
    print('Exists Token')
else:
    http = urllib3.PoolManager()

    system_info = GetSystemInfo()
    data = system_info.Get()
    data.update(login())

    encoded_data = json.dumps(data).encode('utf-8')

    r = http.request(
            'POST',
            'https://lstms.ubun.net/register/client-register.php',
            body=encoded_data,
            headers={'Content-Type': 'application/json'}
        )

    res = r.data.decode('utf-8')
    if res == 'ID or password is incorrect':
        print("ID or password is incorrect")
    else:
        data = res.split(":")

        with open(CONF_FILE, 'w') as f:
            f.write(data[1].strip())

        system(f"chown lstms:lstms {CONF_FILE}")

        print("Client registration complete!!")
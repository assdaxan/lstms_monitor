import json
import urllib3
from os import path
from module.GetSystemInfo import GetSystemInfo

def check(file_name):
    return path.exists(file_name)

def login():
    print("LSTMS Login Please")
    ID = input("ID : ")
    PW = input("PW : ")

    return {'ID':ID, 'PW':PW}

CONF_FILE = 'Token.conf'

if(check(CONF_FILE) == True):
    print('Exists Token')
else:
    http = urllib3.PoolManager()

    system = GetSystemInfo()
    data = system.Get()
    data.update(login())

    encoded_data = json.dumps(data).encode('utf-8')

    r = http.request(
            'POST',
            'https://lstms.ubun.net/register/client-register.php',
            body=encoded_data,
            headers={'Content-Type': 'application/json'}
        )

    res = r.data.decode('utf-8')
    data = res.split(":")

    with open(CONF_FILE, 'w') as f:
        f.write(data[1].strip())
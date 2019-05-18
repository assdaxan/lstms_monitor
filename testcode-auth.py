#!/usr/bin/env python3
from time import sleep, strftime
from subprocess import Popen, PIPE
from select import poll
import json
import urllib3
import re

class GetAuthLog:
    def __init__(self):
        self.re_log = re.compile(r'(?:(?P<mon>\w+) (?P<day>\d+) (?P<time>(?:\d+\:?){3}))(?: *)(?P<user>[^ ]+)(?: *)(?P<command>[\w]+)(?:(?:\[(?P<pid>\d+)\])?\:)(?: *)(?P<log>[^\n]+)')
        self.MON = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    
    def Crawl(self):
        f = Popen('tail -n 0 -F /var/log/auth.log', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        p = poll()
        p.register(f.stdout)

        while True:
            if p.poll():
                self.Parser(f.stdout.readline().decode('utf8'))

    def Parser(self, line):
        data = self.re_log.search(line)
        if data.group('command') in ['sshd', 'sudo', 'su']:
            self.Post(data)

    def Post(self, data):
        data_dict = {"datetime_":f"{strftime('%Y')}-{self.MON[data.group('mon')]}-{data.group('day')} {data.group('time')}",
                        "user":data.group('user'),
                        "command":data.group('command'),
                        "log":data.group('log')}
        encoded_data = json.dumps(data_dict).encode('utf-8')
        
        http = urllib3.PoolManager()
        r = http.request(
                'POST',
                'https://lstms.ubun.net/monitor/auth.php',
                body=encoded_data,
                headers={'Content-Type': 'application/json',
                        "token":"asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdfqwer1234asdf"}
            )
        print(r.data.decode('utf-8'))


if __name__ == "__main__":
    log = GetAuthLog()
    log.Crawl()
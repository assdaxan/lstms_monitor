#!/usr/bin/env python3
from time import sleep
from subprocess import Popen, PIPE
from select import poll

f = Popen('tail -n 0 -F /var/log/auth.log', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
p = poll()
p.register(f.stdout)

while True:
    if p.poll():
        print(f.stdout.readline())
    sleep(1)

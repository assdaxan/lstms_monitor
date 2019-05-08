from time import sleep
from subprocess import Popen, PIPE

p = Popen('iostat | grep sda', stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
t = p.stdout.read()
print(t.split())

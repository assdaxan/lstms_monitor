from subprocess import Popen, PIPE

class Shell(object):
    def Command(self, cmd):
        p = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
        t = p.stdout.read().decode('utf8')
        return t
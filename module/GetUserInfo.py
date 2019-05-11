#!/usr/bin/env python3
import re

class GetUserInfo:
    def __init__(self):
        self.user_info_dict = {}

    def Get(self):
        self.user_info_dict.clear()

        with open('/etc/passwd', 'r') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.split(':')
                self.user_info_dict.update({line[0]:{'uid':line[2], 'gid':line[3], 'info':line[4], 'home':line[5], 'shell':line[6]}})

        return self.user_info_dict


if __name__ == '__main__':
    user = GetUserInfo()
    result = user.Get()
    print(result)
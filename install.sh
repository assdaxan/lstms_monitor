#!/bin/bash

echo "Install Python3"
sudo apt install -y python3

echo "Add User lstms_m"
echo 'Y' | sudo adduser --shell /usr/sbin/nologin --no-create-home --disabled-password --disabled-login --quiet lstms_m

echo "Add Crontab"
(sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-cpu.py' ) | sudo crontab -u lstms_m -
(sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-memory.py' ) | sudo crontab -u lstms_m -
(sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-disk.py' ) | sudo crontab -u lstms_m -
(sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-traffic.py' ) | sudo crontab -u lstms_m -
(sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-io.py' ) | sudo crontab -u lstms_m -
(sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-user.py' ) | sudo crontab -u lstms_m -

echo "Add Systemd Service"
sudo cp /etc/lstmsm_m/lstms.service /etc/systemd/system/lstms.service

echo "Start LSTMS Service"
sudo systemctl start lstms
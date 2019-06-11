#!/bin/bash

echo "Install Python3"
sudo apt install -y python3

echo "Add User lstms_m"
echo 'Y' | sudo adduser --shell /usr/sbin/nologin --no-create-home --disabled-password --disabled-login --quiet lstms_m

echo "LSTMS Permission Setting"
chown -R lstms_m:lstms_m /etc/lstms_m

echo "Register LSTMS Client"
sudo /usr/bin/python3 /etc/lstms_m/lstms-register.py

# echo "Add Crontab"
# (sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-cpu.py' ) | sudo crontab -u lstms_m -
# (sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-memory.py' ) | sudo crontab -u lstms_m -
# (sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-disk.py' ) | sudo crontab -u lstms_m -
# (sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-traffic.py' ) | sudo crontab -u lstms_m -
# (sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-io.py' ) | sudo crontab -u lstms_m -
# (sudo crontab -u lstms_m -l; echo '* * * * * /usr/bin/python3 /etc/lstms_m/lstms-user.py' ) | sudo crontab -u lstms_m -

echo "Add Systemd Service"
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-auth.service
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-cpu.service
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-memory.service
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-disk.service
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-io.service
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-traffic.service
sudo cp /etc/lstms_m/lstms.service /etc/systemd/system/lstms-user.service

echo "Enable LSTMS Service"
sudo systemctl enable lstms-auth
sudo systemctl enable lstms-cpu
sudo systemctl enable lstms-memory
sudo systemctl enable lstms-disk
sudo systemctl enable lstms-io
sudo systemctl enable lstms-traffic
sudo systemctl enable lstms-user

echo "Start LSTMS Service"
sudo systemctl start lstms-auth
sudo systemctl start lstms-cpu
sudo systemctl start lstms-memory
sudo systemctl start lstms-disk
sudo systemctl start lstms-io
sudo systemctl start lstms-traffic
sudo systemctl start lstms-user
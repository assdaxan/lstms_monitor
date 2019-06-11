#!/bin/bash

echo "Stop LSTMS Service"
sudo systemctl stop lstms-auth
sudo systemctl stop lstms-cpu
sudo systemctl stop lstms-memory
sudo systemctl stop lstms-disk
sudo systemctl stop lstms-io
sudo systemctl stop lstms-traffic
sudo systemctl stop lstms-user

echo "Disable LSTMS Service"
sudo systemctl disable lstms-auth
sudo systemctl disable lstms-cpu
sudo systemctl disable lstms-memory
sudo systemctl disable lstms-disk
sudo systemctl disable lstms-io
sudo systemctl disable lstms-traffic
sudo systemctl disable lstms-user

echo "Remove Systemd Service"
sudo rm /etc/systemd/system/lstms-auth.service
sudo rm /etc/systemd/system/lstms-cpu.service
sudo rm /etc/systemd/system/lstms-memory.service
sudo rm /etc/systemd/system/lstms-disk.service
sudo rm /etc/systemd/system/lstms-io.service
sudo rm /etc/systemd/system/lstms-traffic.service
sudo rm /etc/systemd/system/lstms-user.service

echo "Remove LSTMS Script"
sudo rm -rf /etc/lstms_m

echo "Del User lstms_m"
sudo deluser lstms_m
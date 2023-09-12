#!/bin/bash

# System Information
echo "### System Information ###"
echo "Hostname: $(hostname)"
echo "Kernel Version: $(uname -r)"
echo "Operating System: $(cat /etc/os-release | grep "PRETTY_NAME" | cut -d '"' -f 2)"
echo "Uptime: $(uptime)"

# CPU Information
echo -e "\n### CPU Information ###"
lscpu

# Memory Information
echo -e "\n### Memory Information ###"
free -h

# Disk Information
echo -e "\n### Disk Information ###"
df -h

# Network Information
echo -e "\n### Network Information ###"
ip addr show

# Users and Groups
echo -e "\n### Users and Groups ###"
cat /etc/passwd
cat /etc/group

# Mounted Filesystems
echo -e "\n### Mounted Filesystems ###"
mount

# Firewall Rules (if applicable)
if command -v iptables &>/dev/null; then
    echo -e "\n### Firewall Rules ###"
    iptables -L
elif command -v ufw &>/dev/null; then
    echo -e "\n### Firewall Rules ###"
    ufw status
fi

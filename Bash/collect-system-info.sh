#!/bin/bash
#this file's output would be redirected to another device so that it is collected not on the main machine
printf "Collecting Information....\n\n"
echo "TIME INFORMATION:"
x=$(date)
y=$(uptime)
echo "current date is:" $x
echo "uptime is:" $y
printf "\nOS INFORMATION:\n"
x=$(grep -E '^(VERSION|NAME)=' /etc/os-release)
y=$(cat /proc/version)
echo "kernel information:" $y
echo "operating system information:" $x
printf "\nSYSTEM SPECS:\n"
v=$(lscpu | grep -E '^(Architecture|Model)')
w=$(free)
x=$(df -h)
y=$(lsblk)
z1=$(hostname)
z2=$(hostname -d)
echo "cpu information:" $v
printf "used memory: " 
echo $w | awk '{print $9}'
printf "free memory: "
echo $w | awk '{print $10}'
echo "disk space usage:"
echo "$x"
echo "full partitions list:"
echo "$y"
printf "hostname is $z1 and domain name is $z2"
printf "\n\nNETWORK INFORMATION:\n"
y=$(ip a)
z=$(lsof -i 4)
echo "MACs and IPs of all interfaces:"
echo "$y"
echo "interfaces running in promiscuous mode(blank means none):"
echo $y | grep PROMISC
echo "all active network connections:"
echo "$z"
printf "\nUSER INFORMATION:\n\n"
z=$(w)
x=$(awk -F: '/\/home/ {printf "%s:%s\n",$1,$3}' /etc/passwd)
y=$(find / -uid 0 \( -perm -4000 -o -perm -2000 \) -type f  &> SUIDFILES.txt) #this would be changed to be a location not on the pc like on a flash drive or something
w=$(cut -d: -f1,3 /etc/passwd | grep -E ':[0-9]{4}$' | cut -d: -f1)
v=$(cut -d: -f1,3 /etc/passwd | grep ':0')
echo "currently logged in users" 
echo "$z"
echo "list of all non system users:" $w
echo "users with uid 0:" $v
echo "to see all SUID files look at the text file created"
printf "\nPROCESSES AND OPEN FILES:\n\n"
y=$(ps ax)
x=$(pidof nc | head -n1 | cut -d " " -f1)
z=$(lsof -p $x)
w=$(lsof +L1)
echo "all running process:"
echo "$y"
echo "all files open by nc:"
echo "$z"
echo "unlinked files that are still open"
echo "$w"
printf "\nMISC:\n"
z=$(find ~ -type f -executable -mtime -1 &> 1dayedited.txt) #same as other redirect, would be sent to a usb drive or something similar and checked manually
x=$(sudo crontab -u root -l) #need sudo permissions
y=$(cat /etc/group)
z=$(cat ~/.bash_history)
w=$(ls /dev)
echo "root scheduled tasks:"
echo "$x"
echo "all groups on the system:"
echo "$y"
echo "current users bash history"
echo "$z"
echo "looking for suspicious files in /dev"
echo "$w"
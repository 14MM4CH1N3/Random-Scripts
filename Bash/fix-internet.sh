#!/bin/bash
#meant to be run as a cron job, made for a friend who had a server
#running and it would just randomly lose its IP address while he was asleep
#so this just checks for connectivity and up/downs the interface to reconnect
OUTPUT=$(ping <dns server> -c 2 | grep Unreachable)
if [ -z "$OUTPUT" ] 
then
    echo "hi" > /dev/null
else
    $(dhclient -r)
    wait
    $(ip link set dev <hardcode interface> down)
    wait
    $(ip link set dev <hardcode interface> up)
    wait
    $(dhclient)
    wait
fi
## Lathund simple stuff

To install with no screen install the 64 bit os
with ssh enabled with password and WLAN enabled
and also with ethernet cabel (hängslen och livrem)


finding the raspberry pi:
``` {bash}
ping raspberrypi.local
```

then obviously:
``` {bash}
ssh pi@192.168.xxx.xxx
```


To install docker on your pi is as simple as
``` {bash}
curl -sSL get.docker.com | sh
```


Only allow connections on ssh, http and (https?) ports...
```
pi@raspberrypi:~$ sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
pi@raspberrypi:~$ sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
pi@raspberrypi:~$ sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
pi@raspberrypi:~$ sudo iptables -A INPUT -j DROP
```



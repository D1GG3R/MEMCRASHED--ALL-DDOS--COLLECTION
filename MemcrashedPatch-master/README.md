# MEMCRASHED DDOS EXPLOIT TOOL

* Author: [@037](https://twitter.com/037)
** Patch Author: https://vk.com/alex_super228

'''
Original: https://github.com/649/Memcrashed-DDoS-Exploit
'''

This tool allows you to send forged UDP packets to Memcached servers obtained from Shodan.io

### Patch

In the script of the tool , I embedded a shodan key that I found in the public domain.

### Prerequisites

The only thing you need installed is Python 3.x

```
apt-get install python3
```

You also require to have Scapy and Shodan modules installed
```
pip install scapy
```

```
pip install shodan
```
```
Or : python3 installer.py
```

### Using Shodan API

This tool requires you to own an upgraded Shodan API

You may obtain one for free in [Shodan](https://shodan.io/) if you sign up using a .edu email

![alt text](https://raw.githubusercontent.com/649/Memcrashed-DDoS-Exploit/master/2.png)
![alt text](https://raw.githubusercontent.com/649/Memcrashed-DDoS-Exploit/master/1.png)
![alt text](https://raw.githubusercontent.com/649/Memcrashed-DDoS-Exploit/master/3.png)
![alt text](https://raw.githubusercontent.com/649/Memcrashed-DDoS-Exploit/master/4.png)


### Using Docker

##### [Demo](https://asciinema.org/a/v1AEEa17xzqUfyW4pEIS0JONW)

You may deploy this tool to the cloud using a light Alpine Docker image.

> Note: Make sure to explicitly enter 'y' or 'n' to the interactive prompt

```bash
git clone https://github.com/AlexZiroYT/MemcrashedPatch.git
cd MemcrashedPatch
docker build -t memcrashed .
docker run -it memcrashed

```


import os, time

install = input("Install the required repositories? (y/n) : ")

if install == ('y'):
    time.sleep(1)
    pip = 'apt install python3-pip'
    os.system (pip)
    time.sleep(1)
    scapy = 'pip install scapy'
    os.system (scapy)
    time.sleep(1)
    shodan = 'pip install shodan'
    os.system (shodan)
    time.sleep(1)
    print("Installed!")
elif install == ('n'):
    print("Okay, use Memcrashed.py")
    mem = 'python3 Memcrashed.py'
    os.system (mem)
elif install != ('y','n'):
    print('An unknown value, use "y" if "n" ')
    exit()
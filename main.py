import os
import sys
from scapy.all import *

ans, unans = arping("192.168.1.0/24")
if ans:
        first_response = ans[0]
        #print(first_response)
        req, res = first_response
        if (res.haslayer(ARP)):
                result = res.getlayer(ARP).hwsrc
                print((result))
                result = res.getlayer(ARP).psrc
                print(result)


#ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.1.0/24"),timeout=2)

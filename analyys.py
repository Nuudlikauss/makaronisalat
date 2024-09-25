# pip install dnspython
from scapy.all import *
import dns.resolver
import dns.reversename

d_resolv = dns.resolver.Resolver()
d_resolv.nameservers = ['dns ip siia']
ips = set()
#file = "capture.pcap" <------ kommeteeri tagasi kui tahad rdpcapi kasutada
#s = rdpcap(file) <------ kommeteeri tagasi kui tahad rdpcapi kasutada


#for p in s:                <------ kommeteeri tagasi kui tahad rdpcapi kasutada
with PcapReader('capture.pcap') as pcap_reader:    # <------------------ kommenteeri välja kui tahad rdpcapi kasutada
    for p in pcap_reader:                          # <------------------ kommenteeri välja kui tahad rdpcapi kasutada
        if p.haslayer('IP'):
            src_ip = p['IP'].src
            dst_ip = p['IP'].dst
            ips.add(src_ip)
            ips.add(dst_ip)

def nslookup(ip):
    try:
        # mingi dnsi nuss on siis kirjeldame reverse lookupi
        r = dns.reversename.from_address(ip)
        h = str(d_resolv.resolve(r, "PTR")[0])
        return h
    except Exception as e:
        return None
    
for ip in ips:
    hostname = nslookup(ip)
    if hostname:
        print(f"IP: {ip}, Hostname: {hostname}")
    else:
        print(f"IP: {ip}, Hostname not found")

#import IPython;IPython.embed(colors='neutral')
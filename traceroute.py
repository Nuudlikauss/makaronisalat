Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import csv 
import os



def traceroute(hostname):
    print "[+] Generating traceroute information for '{}' ... ".format(hostname),
    os.system("tracert {} > data/{}.txt ".format(hostname,hostname))
    print "OK"

f = open("dnsnames.csv",'rb')
reader = csv.reader(f)
for rida in reader:
    traceroute(rida[0])

f.close()



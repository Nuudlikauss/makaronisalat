Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import csv
import nmap
import sys


# python blah.py > results.txt 


nm = nmap.PortScanner()

def sk2nn(hostname):
    print hostname + ":",
    nm.scan(hostname)

    print nm.scanstats()['uphosts']
        
    


f = open("dnsnames.csv", 'rb')
reader = csv.reader(f,delimiter=';')
for rida in reader:
    sk2nn(rida[0])
f.close()

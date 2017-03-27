import csv
import nmap
import sys


# python blah.py > results.txt 


nm = nmap.PortScanner()

def sk2nn(hostname):
    print hostname + ":",
    nm.scan(hostname)

    print nm.scanstats()['uphosts']
        
    


f = open("''''''.csv", 'rb')
reader = csv.reader(f,delimiter=';')
for rida in reader:
    sk2nn(rida[0])
f.close()

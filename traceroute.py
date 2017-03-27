import csv 
import os



def traceroute(hostname):
    print "[+] Generating traceroute information for '{}' ... ".format(hostname),
    os.system("tracert {} > data/{}.txt ".format(hostname,hostname))
    print "OK"

f = open("something.csv",'rb')
reader = csv.reader(f)
for rida in reader:
    traceroute(rida[0])

f.close()



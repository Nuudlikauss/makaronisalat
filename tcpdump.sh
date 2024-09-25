#!/bin/bash

# Define interface and ports
INTERFACE="any"
#PORTS=$(netstat -tlnup | awk '{print $4}' | cut -d':' -f2 | sort | uniq)
#LISTENING_PORTS=$(echo "$PORTS" | awk '{print "port " $1}' | paste -sd "or")
# Define output file
OUTPUT_FILE="capture.pcap"

#Get hostname ip to exclude
#SRC_IP=$(hostname -I | awk '{print $1}')

# Do tcpdump
tcpdump -i "$INTERFACE" -c1000 -nn -w "$OUTPUT_FILE" #port "$LISTENING_PORTS"

#!/bin/bash

# Author: Priya
# Description: Capture network packets using tcpdump and save output to text file

# Timestamp and output file names
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
CAPTURE_TXT="packet_capture_$TIMESTAMP.txt"
CAPTURE_PCAP="packet_capture_$TIMESTAMP.pcap"

# Log function
log() {
    echo "[Priya] $1" | tee -a "$CAPTURE_TXT"
}

log "Starting packet capture at $TIMESTAMP"
log "Saving human-readable output to $CAPTURE_TXT"
log "Saving raw packet data to $CAPTURE_PCAP"

# Start capture (change 'icmp' to 'tcp', 'port 80', etc. for other types)
log "Running: sudo tcpdump -i any -c 20 -n -v icmp"
sudo tcpdump -i any -c 20 -n -v icmp -w "$CAPTURE_PCAP" &> /dev/null

# Convert pcap to human-readable text using tcpdump -r
log "Converting pcap to readable text..."
tcpdump -nn -r "$CAPTURE_PCAP" | tee -a "$CAPTURE_TXT"

log "Capture complete."
log "Output saved in:"
log "  - $CAPTURE_TXT (text summary)"
log "  - $CAPTURE_PCAP (for Wireshark)"

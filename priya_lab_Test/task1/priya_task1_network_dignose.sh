#!/bin/bash

# Author: Priya
# Description: Network diagnostics script with detailed logging and PDF conversion

# Create timestamped output directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTDIR="network_diagnostics_$TIMESTAMP"
mkdir -p "$OUTDIR"

# Output files
TXT_OUT="$OUTDIR/output.txt"
PDF_OUT="$OUTDIR/output.pdf"

# Get hostname
HOSTNAME=$(hostname)

log() {
    echo "[Priya] $1" | tee -a "$TXT_OUT"
}

run_and_log() {
    CMD_DESC="$1"
    CMD="$2"

    log "----- START: $CMD_DESC -----"
    log "Running command: $CMD"
    echo "===================================" | tee -a "$TXT_OUT"
    eval "$CMD" 2>&1 | tee -a "$TXT_OUT"
    log "----- COMPLETE: $CMD_DESC -----"
    echo -e "\n\n" >> "$TXT_OUT"
}

log "Network diagnostics started by Priya at $TIMESTAMP"
log "Machine Name (Hostname): $HOSTNAME"
log "Creating output folder at $OUTDIR"

# Start tcpdump in background (ICMP and traceroute)
TCPDUMP_FILE="$OUTDIR/icmp_traceroute.pcap"
log "Starting tcpdump to capture ICMP and traceroute traffic into $TCPDUMP_FILE"
sudo tcpdump icmp or udp port 33434 -w "$TCPDUMP_FILE" &
TCPDUMP_PID=$!

sleep 2  # Ensure tcpdump starts properly

# Run commands
run_and_log "Network Configuration (ifconfig)" "ifconfig"
run_and_log "Active Network Connections (netstat)" "netstat -tulnp"
run_and_log "DNS Lookup (nslookup google.com)" "nslookup google.com"
run_and_log "Traceroute to google.com" "traceroute google.com"
run_and_log "Ping to google.com" "ping -c 4 google.com"

# Stop tcpdump
log "Stopping tcpdump process (PID: $TCPDUMP_PID)"
sudo kill $TCPDUMP_PID
sleep 1
log "tcpdump capture saved to $TCPDUMP_FILE"

# Convert TXT to PDF (if tools available)
if command -v enscript >/dev/null 2>&1 && command -v ps2pdf >/dev/null 2>&1; then
    log "Converting output.txt to PDF..."
    enscript "$TXT_OUT" -o - | ps2pdf - "$PDF_OUT"
    log "PDF saved to $PDF_OUT"
else
    log "enscript or ps2pdf not found; skipping PDF conversion."
fi

log "Diagnostics complete. Output files are in: $OUTDIR"

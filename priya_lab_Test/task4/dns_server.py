#!/usr/bin/env python3

import socket

LOG_FILE = "dns_server_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

# Predefined DNS table (domain to IP mapping)
DNS_TABLE = {
    "example.com": "93.184.216.34",
    "openai.com": "104.18.12.123",
    "google.com": "142.250.74.206"
}

def run_dns_server(host="127.0.0.1", port=5353):
    log(f"[DNS Server] Starting on {host}:{port}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    while True:
        data, client_addr = server_socket.recvfrom(1024)
        domain = data.decode().strip()
        log(f"[DNS Server] Received request for domain: {domain}")

        ip = DNS_TABLE.get(domain, "Domain not found")
        log(f"[DNS Server] Responding with IP: {ip}")
        server_socket.sendto(ip.encode(), client_addr)

if __name__ == "__main__":
    run_dns_server()


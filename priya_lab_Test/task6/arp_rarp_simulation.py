import time

LOG_FILE = "arp_rarp_log.txt"

# Sample ARP table (like a local cache of IP ↔ MAC mappings)
ARP_TABLE = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

# Reverse mapping for RARP
RARP_TABLE = {v: k for k, v in ARP_TABLE.items()}

def log(message):
    print(message)
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

def simulate_arp(ip_address):
    log(f"\n[ARP] Resolving MAC address for IP: {ip_address}")
    time.sleep(1)
    mac = ARP_TABLE.get(ip_address)
    if mac:
        log(f"[ARP] Response: MAC address for {ip_address} is {mac}")
    else:
        log(f"[ARP] Error: No MAC address found for {ip_address}")

def simulate_rarp(mac_address):
    log(f"\n[RARP] Resolving IP address for MAC: {mac_address}")
    time.sleep(1)
    ip = RARP_TABLE.get(mac_address)
    if ip:
        log(f"[RARP] Response: IP address for {mac_address} is {ip}")
    else:
        log(f"[RARP] Error: No IP address found for {mac_address}")

def main():
    log("=== ARP / RARP Protocol Simulation ===")
    while True:
        choice = input("\n1. Simulate ARP\n2. Simulate RARP\n3. Exit\nChoose an option: ").strip()
        if choice == '1':
            ip = input("Enter IP address: ").strip()
            simulate_arp(ip)
        elif choice == '2':
            mac = input("Enter MAC address (e.g., AA:BB:CC:DD:EE:01): ").strip().upper()
            simulate_rarp(mac)
        elif choice == '3':
            log("\n[Simulation] Exiting ARP/RARP simulation.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()


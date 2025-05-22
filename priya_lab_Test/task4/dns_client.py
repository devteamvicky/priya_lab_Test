import socket

LOG_FILE = "dns_client_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def run_dns_client(server_host="127.0.0.1", server_port=5353):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        domain = input("Enter domain name (or type 'exit' to quit): ").strip()
        if domain.lower() == "exit":
            break

        log(f"[Client] Sending domain: {domain}")
        client_socket.sendto(domain.encode(), (server_host, server_port))

        data, _ = client_socket.recvfrom(1024)
        response = data.decode()
        log(f"[Client] Received response: {response}")

    client_socket.close()
    log("[Client] Connection closed.")

if __name__ == "__main__":
    run_dns_client()


#!/usr/bin/env python3
import socket

LOG_FILE = "echo_client_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def run_echo_client(host='127.0.0.1', port=9001):
    log(f"[Client] Connecting to {host}:{port}")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        msg = input("You: ")
        if msg.lower() == 'exit':
            break
        client_socket.sendall(msg.encode())
        log(f"[Client] Sent: {msg}")
        data = client_socket.recv(1024)
        log(f"[Client] Received Echo: {data.decode()}")

    client_socket.close()
    log("[Client] Connection closed.")

if __name__ == "__main__":
    run_echo_client()

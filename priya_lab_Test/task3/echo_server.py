import socket
#!/usr/bin/env python3

LOG_FILE = "echo_server_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def run_echo_server(host='127.0.0.1', port=9001):
    log(f"[Server] Starting Echo Server on {host}:{port}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    log("[Server] Waiting for connection...")

    conn, addr = server_socket.accept()
    log(f"[Server] Connected to {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg = data.decode()
        log(f"[Server] Received: {msg}")
        conn.sendall(data)
        log(f"[Server] Echoed: {msg}")

    log("[Server] Connection closed.")
    conn.close()
    server_socket.close()

if __name__ == "__main__":
    run_echo_server()

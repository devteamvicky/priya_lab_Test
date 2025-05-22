import socket

LOG_FILE = "chat_server_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def run_chat_server(host='127.0.0.1', port=9002):
    log(f"[Server] Starting Chat Server on {host}:{port}")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, addr = server_socket.accept()
    log(f"[Server] Connected to {addr}")

    while True:
        client_msg = conn.recv(1024).decode()
        if client_msg.lower() == 'exit':
            log("[Server] Client ended chat.")
            break
        log(f"Client: {client_msg}")
        reply = input("You: ")
        conn.sendall(reply.encode())
        log(f"You: {reply}")

    conn.close()
    server_socket.close()
    log("[Server] Connection closed.")

if __name__ == "__main__":
    run_chat_server()

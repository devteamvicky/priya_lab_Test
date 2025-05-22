import socket

LOG_FILE = "chat_client_log.txt"

def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as f:
        f.write(msg + "\n")

def run_chat_client(host='127.0.0.1', port=9002):
    log(f"[Client] Connecting to {host}:{port}")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        msg = input("You: ")
        client_socket.sendall(msg.encode())
        log(f"You: {msg}")
        if msg.lower() == 'exit':
            break
        reply = client_socket.recv(1024).decode()
        log(f"Server: {reply}")

    client_socket.close()
    log("[Client] Connection closed.")

if __name__ == "__main__":
    run_chat_client()

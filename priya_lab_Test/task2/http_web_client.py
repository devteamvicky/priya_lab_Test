#!/usr/bin/env python3
import socket

def download_webpage(host, path="/", port=80):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"[Client] Connecting to {host}:{port}...")
    client_socket.connect((host, port))
    print("[Client] Connected.")

    # Form HTTP GET request
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    print("[Client] Sending HTTP request...")
    client_socket.send(request.encode())

    # Receive the response
    response = b""
    while True:
        data = client_socket.recv(4096)
        if not data:
            break
        response += data

    print("[Client] Response received. Closing connection.")
    client_socket.close()

    # Split headers and body
    header_end = response.find(b"\r\n\r\n")
    headers = response[:header_end].decode(errors='ignore')
    body = response[header_end + 4:]

    # Save full response to file
    with open("http_response.txt", "w", encoding="utf-8", errors="ignore") as f:
        f.write(headers + "\n\n")
        f.write(body.decode("utf-8", errors="ignore"))

    # Save only the body to an HTML file
    with open("downloaded_page.html", "wb") as f:
        f.write(body)

    print("[Client] Full HTTP response saved to 'http_response.txt'")
    print("[Client] Web page content saved to 'downloaded_page.html'")

# Example usage
if __name__ == "__main__":
    download_webpage("example.com", "/")

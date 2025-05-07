import socket
import threading

PORT = 5050
BUFFER_SIZE = 4096

def handle_client(conn, addr):
    print(f"\nNew connection from {addr}")
    data = conn.recv(BUFFER_SIZE)
    if data:
        try:
            message = data.decode('utf-8')
            print("\n--- New Message Received ---")
            print(message)
            print("--- End of Message ---\n")
        except Exception as e:
            print("Error decoding message:", e)
    conn.close()

def main():
    server_ip = "0.0.0.0"  # Listen on all interfaces
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((server_ip, PORT))
        server.listen()
        print(f"Receiver is listening on port {PORT}...")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    main()


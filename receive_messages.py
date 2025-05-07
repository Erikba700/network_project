import socket
import threading
import datetime

PORT = 5050
BUFFER_SIZE = 4096
LOG_FILE = "received_messages.log"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp}\n{message}\n\n")

def pretty_print(message):
    # Naively extract some tags
    try:
        to = message.split('to="')[1].split('"')[0]
        from_ = message.split('from="')[1].split('"')[0]
        body = message.split("<body>")[1].split("</body>")[0]
        print(f"\n--- New Message ---")
        print(f"From: {from_}")
        print(f"To:   {to}")
        print(f"Body: {body}")
        print(f"--- End of Message ---\n")
    except Exception:
        print(f"\nReceived malformed message:\n", message)

def handle_client(conn, addr):
    print(f"\nNew connection from {addr}")
    data = conn.recv(BUFFER_SIZE)
    if data:
        try:
            message = data.decode('utf-8')
            pretty_print(message)
            log_message(message)
        except Exception as e:
            print("Error decoding message:", e)
    conn.close()

def main():
    server_ip = "0.0.0.0"
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


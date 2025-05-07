# IP Messenger Receiver

This project is a basic IP-based messaging receiver that listens for incoming messages, displays them, and logs them to a file. It works over TCP/IP and receives messages encoded in XML format. Every received message is logged with a timestamp and printed to the terminal.

---

## Features

- Listens for incoming messages on a specified port.
- Displays message details in a human-readable format (From, To, Body).
- Logs received messages with timestamps to a log file.
- Handles connections from multiple clients using threading.

---

## Requirements

- Python 3.x
- No third-party libraries required (uses built-in libraries):
  - `socket`
  - `threading`
  - `datetime`
  - `xml.etree.ElementTree`

---

## Usage

### Starting the Receiver

1. Navigate to the project folder in your terminal.
2. Run the `receive_messages.py` script:

   ```bash
   python3 receive_messages.py
This will start the server and begin listening for incoming messages on port 5050.

Sending a Message
To test the receiver:

Open a new terminal window.

From the same project directory, run the send_message.py script:

bash
python3 send_message.py
You’ll be prompted to enter the receiver's IP address and your message. The message will be sent in XML format to the server.

Message Format
The receiver expects messages in the following XML format:

xml
<message to="recipient_ip" from="sender_ip" type="chat" xmlns="jabber:client">
  <body>Message content goes here</body>
</message>
Example Output
When a message is received, the server terminal will display:

vbnet
--- New Message ---
From: sender_ip
To:   recipient_ip
Body: Message content goes here
--- End of Message ---
Example Log Format
In received_messages.log, each message is stored with a timestamp:

php-template
[YYYY-MM-DD HH:MM:SS]
<message to="recipient_ip" from="sender_ip" type="chat" xmlns="jabber:client">
  <body>Message content goes here</body>
</message>

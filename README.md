# IP Messenger Receiver

This project is a basic IP-based messaging receiver that listens for incoming messages, displays them, and logs them to a file. The project works over TCP/IP, receiving messages encoded in XML format. The system logs every received message with a timestamp and prints the details to the terminal.

## Features

- Listens for incoming messages on a specified port.
- Displays message details in a human-readable format (From, To, Body).
- Logs received messages with timestamps to a log file.
- Handles connections from multiple clients using threading.

## Requirements

- Python 3.x
- Required Python libraries:
  - `socket`
  - `threading`
  - `datetime`

### Optional (for logging and message formatting):
- `colorama` (for colored terminal output; removed in this version)

## Installation

1. Clone or download the repository to your server or machine.

2. Install necessary Python packages (if not already installed):
   - You can install Python using the following commands (if you don't have it already):
   
     ```bash
     sudo apt update
     sudo apt install python3
     sudo apt install python3-pip
     ```
   
   - Install any missing dependencies:

     ```bash
     pip3 install --user socket
     ```

## Usage

### Starting the Receiver

1. Navigate to the project folder in your terminal.
2. Run the `receive_messages.py` script:

   ```bash
   python3 receive_messages.py
This will start the server listening for incoming messages on port 5050.Message Format
The receiver expects messages to be in the following format:

xml
Copy
Edit
<message to="recipient_ip" from="sender_ip" type="chat" xmlns="jabber:client">
  <body>Message content goes here</body>
</message>
Example Output
Upon receiving a message, the receiver will display the message details in the terminal:

vbnet
Copy
Edit
--- New Message ---
From: sender_ip
To:   recipient_ip
Body: Message content goes here
--- End of Message ---
It will also log the message to received_messages.log with a timestamp.

Example Log Format
The log will store the messages with a timestamp in the following format:

php-template
Copy
Edit
[YYYY-MM-DD HH:MM:SS]
<message to="recipient_ip" from="sender_ip" type="chat" xmlns="jabber:client">
  <body>Message content goes here</body>
</message>



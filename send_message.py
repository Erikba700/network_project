import socket
import xml.etree.ElementTree as ET

PORT = 5050

def build_xmpp_message(to_ip, from_ip, message):
    msg = ET.Element('message', {
        'to': to_ip,
        'from': from_ip,
        'type': 'chat',
        'xmlns': 'jabber:client'
    })
    body = ET.SubElement(msg, 'body')
    body.text = message
    return ET.tostring(msg, encoding='unicode')

def send_message(contact_ip, sender_ip, message):
    xmpp_msg = build_xmpp_message(contact_ip, sender_ip, message)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((contact_ip, PORT))
        s.sendall(xmpp_msg.encode('utf-8'))
        print("Message sent.")

def main():
    contact_ip = input("Enter recipient IP address: ").strip()
    sender_ip = input("Enter your IP address: ").strip()
    message = input("Enter message to send: ").strip()
    send_message(contact_ip, sender_ip, message)

if __name__ == "__main__":
    main()


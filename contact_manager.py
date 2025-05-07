import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def list_contacts():
    contacts = load_contacts()
    for idx, contact in enumerate(contacts):
        print(f"{idx + 1}. {contact['name']} - {contact['ip']}")

def add_contact():
    name = input("Enter name: ")
    ip = input("Enter IP address: ")
    contacts = load_contacts()
    contacts.append({"name": name, "ip": ip})
    save_contacts(contacts)
    print("Contact added.")

def remove_contact():
    list_contacts()
    idx = int(input("Enter the number of the contact to remove: ")) - 1
    contacts = load_contacts()
    if 0 <= idx < len(contacts):
        removed = contacts.pop(idx)
        save_contacts(contacts)
        print(f"Removed {removed['name']}.")
    else:
        print("Invalid selection.")

def edit_contact():
    list_contacts()
    idx = int(input("Enter the number of the contact to edit: ")) - 1
    contacts = load_contacts()
    if 0 <= idx < len(contacts):
        name = input("New name (leave empty to keep current): ") or contacts[idx]["name"]
        ip = input("New IP (leave empty to keep current): ") or contacts[idx]["ip"]
        contacts[idx] = {"name": name, "ip": ip}
        save_contacts(contacts)
        print("Contact updated.")
    else:
        print("Invalid selection.")

def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. List contacts")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Remove contact")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            list_contacts()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()


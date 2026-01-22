import math
contacts = {}

def display_menu():
    while True:
        print ('''Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit''')
        n = int(input())
        if n == 1:
            add_contact(contacts)
        elif n == 2:
            view_contact(contacts)
        elif n == 3:
            edit_contact(contacts)
        elif n == 4:
            delete_contact(contacts)
        elif n == 5:
            list_all_contacts(contacts)
        elif n == 6:
            break
        
def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()
    if (name in contact_book):
        print("Contact already exists!")
    else:
        contact_book[name] = {
	    "phone": phone,
	    "email": email,
	    "address": address
        }
        print("Contact added successfully!")
def view_contact(contact_book):
    contact_name = input()
    if contact_name in contact_book:
        res = f'''Name: {contact_name}
Phone: {contact_book[contact_name]['phone']}
Email: {contact_book[contact_name]['email']}
Address: {contact_book[contact_name]['address']}'''
        print(res)
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        phone = input()
        email = input()
        address = input()
        contact_book[name]["phone"] = phone
        contact_book[name]["email"] = email
        contact_book[name]["address"] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if not contact_book:
        print("No contacts available.")
    else:
        for key, value in contact_book.items():
            print(f"Name: {key}")
            print(f"Phone: {value['phone']}")
            print(f"Email: {value['email']}")
            print(f"Address: {value['address']}\n")


display_menu()
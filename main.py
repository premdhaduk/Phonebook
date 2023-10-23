#functions for phonebook
import pickle
import sys

contacts = []
def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    contact = {"name": name, "phone_number": phone_number}
    contacts.append(contact)
def view_contact():
    if not contacts:
        print("No contacts in the phonebook.")
    else:
        print("List of Contacts: ")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone_number']}")
def search_contact():
    if not contacts:
        print("No contacts in the phonebook.")
        return

    search_term = input("Enter a name or phone number to search: ")
    matching_contacts = []

    for contact in contacts:
        if search_term.lower() in contact["name"].lower() or search_term in contact['phone_number']:
            matching_contacts.append(contact)
    if matching_contacts:
        print("Matching Contacts: ")
        for idx, contact in enumerate(matching_contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone_number']}")
    else:
        print("No matching contacts")

def edit_contact():
    if not contacts:
        print("No contacts in the phonebook.")
        return

    view_contact()
    contact_idx = int(input("Enter number of the contact to edit: ")) - 1

    if 0 <= contact_idx < len(contacts):
        contact = contacts[contact_idx]
        print(f'Editing Contact: {contact["name"]}')
        #prompt input of new information
        new_name = input("Enter the new name (leave empty to keep unchanged): ")
        new_phone_number = input("Enter the new phone number (leave empty to keep unchanged): ")

        if new_name:
            contact['name'] = new_name
        if new_phone_number:
            contact['phone_number'] = new_phone_number

        print("Contact updated successfully")
    else:
        print("Invalid Contact Number")

def delete_contact():
    if not contacts:
        print("No contacts in the phonebook.")
        return
    view_contact()  # Display a list of contacts to choose from
    contact_idx = int(input("Enter the number of the contact to delete: ")) - 1

    if 0 <= contact_idx < len(contacts):
        deleted_contact = contacts.pop(contact_idx)
        print(f"Contact '{deleted_contact['name']}' deleted successfully.")
    else:
        print("Invalid contact number.")


def exit_phonebook():
    print("Exiting Phonebook. Goodbye!")

def save_contacts_to_file(filename):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)

def load_contacts_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

contacts = load_contacts_from_file('phonebook.pkl')

#Welcome Screen

while True:
    print("Welcome to my Phonebook, I hope you find what you are looking for!")
    print("1. Add Contacts")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Edit Contacts")
    print("5. Delete Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6) ")


    #User Input Conversion

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contact()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        edit_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        save_contacts_to_file('phonebook.pkl')
        exit_phonebook()
        break
    else:
        print("Invalid Choice. Please select a valid option.")



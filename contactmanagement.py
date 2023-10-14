class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts[name] = contact
        print(f"{name} has been added to your contacts.")

    def view_contacts(self):
        if self.contacts:
            for name, contact in self.contacts.items():
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print()
        else:
            print("Your contact list is empty.")

    def edit_contact(self, name, new_phone, new_email):
        if name in self.contacts:
            contact = self.contacts[name]
            contact.phone = new_phone
            contact.email = new_email
            print(f"{name}'s contact information has been updated.")
        else:
            print(f"{name} is not in your contacts.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"{name} has been deleted from your contacts.")
        else:
            print(f"{name} is not in your contacts.")

def main():
    contact_manager = ContactManager()

    while True:
        print("Contact Management Menu:")
        print("1. Add a new contact")
        print("2. View contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact_manager.add_contact(name, phone, email)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name = input("Enter the name of the contact to edit: ")
            new_phone = input("Enter the new phone number: ")
            new_email = input("Enter the new email address: ")
            contact_manager.edit_contact(name, new_phone, new_email)
        elif choice == "4":
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            print("You have Selected Exit!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

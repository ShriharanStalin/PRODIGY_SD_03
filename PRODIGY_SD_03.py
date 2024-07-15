# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 16:17:02 2024

@author: Shriharan S
"""
class Contact:
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def display_contact(self):
        print("Name: ", self.name)
        print("Phone Number: ", self.phone_number)
        print("Email Address: ", self.email_address)
        print("----------------------------")

class ContactManagementSystem:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter Name: ")
        phone_number = input("Enter Phone Number: ")
        email_address = input("Enter Email Address: ")
        
        new_contact = Contact(name, phone_number, email_address)
        self.contacts.append(new_contact)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                contact.display_contact()

    def edit_contact(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            self.view_contacts()
            index = int(input("Enter the index of the contact you want to edit: ")) - 1

            if 0 <= index < len(self.contacts):
                print("Editing Contact:")
                self.contacts[index].display_contact()

                new_name = input("Enter new Name: ")
                new_phone_number = input("Enter new Phone Number: ")
                new_email_address = input("Enter new Email Address: ")

                updated_contact = Contact(new_name, new_phone_number, new_email_address)
                self.contacts[index] = updated_contact
                print("Contact updated successfully!")
            else:
                print("Invalid index. Please enter a valid index.")

    def delete_contact(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            self.view_contacts()
            index = int(input("Enter the index of the contact you want to delete: ")) - 1

            if 0 <= index < len(self.contacts):
                print("Deleting Contact:")
                self.contacts[index].display_contact()
                self.contacts.pop(index)
                print("Contact deleted successfully!")
            else:
                print("Invalid index. Please enter a valid index.")

    def main_menu(self):
        choice = 0

        while choice != 5:
            print("Contact Management System")
            print("1. Add New Contact")
            print("2. View Contacts")
            print("3. Edit Contact")
            print("4. Delete Contact")
            print("5. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.add_contact()
            elif choice == 2:
                self.view_contacts()
            elif choice == 3:
                self.edit_contact()
            elif choice == 4:
                self.delete_contact()
            elif choice == 5:
                print("Exiting Contact Management System. Goodbye!")
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.main_menu()


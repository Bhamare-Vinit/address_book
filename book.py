'''
@Author: Vinit Bhamare
@Date: 2024-07-10 15:00:30
@Last Modified by: Vinit Bhamare
@Last Modified time: 2024-07-13 14:00:30
@Title : Address book
'''
from collections import OrderedDict
import json
import os

class AddressBookManager:
    def __init__(self):
        self.address_books = {}
        self.load_address_books()

    def create_address_book(self, book_name):
        """
        Description: Creates a new address book with the given name.
        Parameters: 
            1. book_name: The name of the new address book.
        Return: None
        """
        if book_name not in self.address_books:
            self.address_books[book_name] = Address_Book(book_name)
            self.save_address_books()
            print(f"Address book '{book_name}' created successfully.")
        else:
            print(f"Address book '{book_name}' already exists.")

    def get_address_book(self, book_name):
        """
        description:Retrieves an address book by name
        Parameters: 1. book_name: The name of the address book to retrieve.
        Return: Address_Book: The address book with the given name or None if not found
        """
        return self.address_books.get(book_name, None)

    def save_address_books(self):
        """
        Description: Saves all address books to a JSON file.
        Parameters: None
        Return: None
        """
        with open('address_books.json', 'w') as file:
            json.dump({book_name: book.contact for book_name, book in self.address_books.items()}, file)

    def load_address_books(self):
        """
        Description: Loads address books from a JSON file
        Parameters
        Return: None
        """
        if os.path.exists('address_books.json'):
            with open('address_books.json', 'r') as file:
                address_books_data = json.load(file)
                for book_name, contacts in address_books_data.items():
                    address_book = Address_Book(book_name)
                    address_book.contact = contacts
                    self.address_books[book_name] = address_book


class Address_Book:
    def __init__(self, name):
        self.name = name
        self.contact = {}

    def add_contact(self, fname=None, lname=None, address=None, city=None, state=None, zip=None, phone_number=None, email=None):
        """
        Description: Adds a new contact to the address book
        Parameters:
            1. fname: First name of the contact
            2. lname: Last name of the contact
            3. address: Address of the contact
            4. city: City of the contact
            5. state: State of the contact
            6. zip: ZIP code of the contact
            7. phone_number: Phone number of the contact
            8. email: Email address of the contact
        Return: None
        """
        if fname and lname and address and city and state and zip and phone_number and email:
            if phone_number not in self.contact:
                self.contact[phone_number] = {
                    "firstname": fname,
                    "lastname": lname,
                    "address": address,
                    "city": city,
                    "state": state,
                    "zip_code": zip,
                    "email": email
                }
                print(f"Added successfully {self.contact}")
                self.save_contacts()
            else:
                print(f"{phone_number} already exists in address book")
        else:
            print("Invalid input")

    def display(self):
        """
        Description: Displays contacts sorted by phone number or name.
        Parameters: None
        Return: None
        """
        if self.contact:
            print("\n1. Sort by Phone Number\n2. Sort by Name")
            n = int(input("Enter your option: "))
            if n == 1:
                print("Print sorted value by Phone Number!")
            if n == 2:
                print("Print sorted value by firstname!")
            print("-"*134)
            print(f"| {"Phone Number":^12} | {"First Name":^12} | {"Last Name":^12} | {"Address":^12} | {"City":^12} | {"State":^12} | {"Zip-Code":^12} | {"Email":^25} |")
            print("-"*134)

            
            if n == 1:
                self.contact = OrderedDict(sorted(self.contact.items()))
                for number, details in self.contact.items():
                    # print(f"Phone Number: {number}, Details: {details}")
                    print(f"| {number:^12} | {details["firstname"]:^12} | {details['lastname']:^12} | {details['address']:^12} | {details['city']:^12} | {details['state']:^12} | {details['zip_code']:^12} | {details['email']:^25} |")
                    print("-"*134)

            elif n == 2:
                self.contact = dict(sorted(self.contact.items(), key=lambda item: item[1]['firstname']))

                for number, details in self.contact.items():
                    # print("K")
                    # print(f"Phone Number: {number}, Details: {details}")
                    print(f"| {number:^12} | {details["firstname"]:^12} | {details['lastname']:^12} | {details['address']:^12} | {details['city']:^12} | {details['state']:^12} | {details['zip_code']:^12} | {details['email']:^25} |")
                    print("-"*134)

        else:
            print("No contacts found.")

    def get_count_city(self):
        """
        Description: Counts contacts by city and displays the count.
        Parameters:
        Return: None
        """
        city = {}
        if self.contact:
            self.contact = OrderedDict(sorted(self.contact.items()))
            for number, details in self.contact.items():
                if details["city"] not in city:
                    city[details["city"]] = 1
                elif details["city"] in city:
                    city[details["city"]] += 1
                else:
                    pass
            print(city)
            city = OrderedDict(sorted(city.items()))
            print("-"*37)
            print(f"| {'City':^15} | {'Count':^15} |")
            print("-"*37)

            for citys, count in city.items():
                print(f"| {citys: ^15} | {count:^15} |")
                print("-"*37)
        else:
            print("No contacts found.")

    def get_count_state(self):
        """
        Description: Counts contacts by state and displays the count.
        Parameters: None
        Return: None
        """
        state = {}
        if self.contact:
            self.contact = OrderedDict(sorted(self.contact.items()))
            for number, details in self.contact.items():
                if details["state"] not in state:
                    state[details["state"]] = 1
                elif details["state"] in state:
                    state[details["state"]] += 1
                else:
                    pass
            print(state)
            state = OrderedDict(sorted(state.items()))
            # print(f"{'State':^10} - {'Count':^10}")
            print("-"*37)
            print(f"| {'State':^15} | {'Count':^15} |")
            print("-"*37)
            for states, count in state.items():
                # print(f"{states: ^10} : {count: ^10}")
                print(f"| {states: ^15} | {count:^15} |")
                print("-"*37)
        else:
            print("No contacts found.")

    def search_by_city(self, search_city):
        """
        Description: Searches contacts by city and displays the results.
        Parameters: 
            1. search_city: name of city to search
        Return: None
        """
        if self.contact:
            self.contact = OrderedDict(sorted(self.contact.items()))
            print(f"People who live in {search_city} city:")
            print("-"*134)
            print(f"| {"Phone Number":^12} | {"First Name":^12} | {"Last Name":^12} | {"Address":^12} | {"City":^12} | {"State":^12} | {"Zip-Code":^12} | {"Email":^25} |")
            print("-"*134)
            for number, details in self.contact.items():
                if details["city"] == search_city:
                    # print(f"Phone Number: {number}, Details: {details}")
                    print(f"| {number:^12} | {details["firstname"]:^12} | {details['lastname']:^12} | {details['address']:^12} | {details['city']:^12} | {details['state']:^12} | {details['zip_code']:^12} | {details['email']:^25} |")
                    print("-"*134)

        else:
            print("No contacts found.")

    def search_by_state(self, search_state):
        """
        Description: searches contacts by state and displays the results.
        Parameters: 
            1. search_state:name of state to search for.
        Return: None
        """
        if self.contact:
            self.contact = OrderedDict(sorted(self.contact.items()))
            print(f"People who live in {search_state} state:")
            print("-"*134)
            print(f"| {"Phone Number":^12} | {"First Name":^12} | {"Last Name":^12} | {"Address":^12} | {"City":^12} | {"State":^12} | {"Zip-Code":^12} | {"Email":^25} |")
            print("-"*134)
            for number, details in self.contact.items():
                if details["state"] == search_state:
                    # print(f"{details['firstname']} {details['lastname']}")
                    print(f"| {number:^12} | {details["firstname"]:^12} | {details['lastname']:^12} | {details['address']:^12} | {details['city']:^12} | {details['state']:^12} | {details['zip_code']:^12} | {details['email']:^25} |")
                    print("-"*134)
        else:
            print("No contacts found.")

    def edit_entry(self, fname=None, lname=None, address=None, city=None, state=None, zip=None, phone_number=None, email=None):
        """
        Description: edits an existing contact in the address book.
        Parameters:
            1. fname: First name 
            2. lname: Last name 
            3. address: Address 
            4. city: City 
            5. state: State 
            6. zip: ZIP code 
            7. phone_number: Phone number 
            8. email: Email address 
        Return: None
        """
        if phone_number and phone_number in self.contact:
            lst_info = self.contact[phone_number]
            if fname:
                lst_info["firstname"] = fname
            if lname:
                lst_info["lastname"] = lname
            if address:
                lst_info["address"] = address
            if city:
                lst_info["city"] = city
            if state:
                lst_info["state"] = state
            if zip:
                lst_info["zip_code"] = zip
            if email:
                lst_info["email"] = email
            self.contact[phone_number] = lst_info
            self.save_contacts()
            print("Data updated successfully")
        else:
            print("Phone number does not exist in the database")

    def delete_entry(self, phone_number=None):
        """
        Description: Deletes contact from the address book
        Parameters:
            1. phone_number: Phone number to delte
        Return: None
        """
        if phone_number and phone_number in self.contact:
            del self.contact[phone_number]
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Phone number does not exist in the database")

    def save_contacts(self):
        """
        Description: Saves current contacts to a JSON file.
        Parameters: None
        Return: None
        """
        manager.save_address_books()

    def console(self, manager):
        """
        Description: Provides console interface for managing the address book.
        Parameters: None
        Return: None
        """
        while True:
            try:
                print("\n1. Create Address Book\n2. Add Contact\n3. Display Book\n4. Edit Contact\n5. Delete Contact\n6. Search by\n7. Exit")
                n = int(input("Enter your option: "))
                if n == 1:
                    book_name = input("Enter the name of the new address book: ")
                    manager.create_address_book(book_name)
                elif n == 2:
                    book_name = input("Enter the name of the address book to add a contact: ")
                    book = manager.get_address_book(book_name)
                    if book:
                        num = int(input("Enter the number of entries you want to add: "))
                        for i in range(num):
                            fname = input("Enter first name: ")
                            lname = input("Enter last name: ")
                            address = input("Address: ")
                            city = input("Enter the city: ")
                            state = input("Enter the state: ")
                            zip = input("Enter the zip code: ")
                            phone_number = input("Phone Number: ")
                            email = input("Email: ")
                            book.add_contact(fname, lname, address, city, state, zip, phone_number, email)
                    else:
                        print(f"Address book '{book_name}' does not exist.")
                elif n == 3:
                    book_name = input("Enter the name of the address book to display: ")
                    book = manager.get_address_book(book_name)
                    if book:
                        book.display()
                    else:
                        print(f"Address book '{book_name}' does not exist.")
                elif n == 4:
                    book_name = input("Enter the name of the address book to edit a contact: ")
                    book = manager.get_address_book(book_name)
                    if book:
                        phone_number = input("Phone Number to edit: ")
                        fname = input("Enter first name: ")
                        lname = input("Enter last name: ")
                        address = input("Address: ")
                        city = input("Enter the city: ")
                        state = input("Enter the state: ")
                        zip = input("Enter the zip code: ")
                        email = input("Email: ")
                        book.edit_entry(fname, lname, address, city, state, zip, phone_number, email)
                    else:
                        print(f"Address book '{book_name}' does not exist.")
                elif n == 5:
                    book_name = input("Enter the name of the address book to delete a contact: ")
                    book = manager.get_address_book(book_name)
                    if book:
                        phone_number = input("Enter the Phone Number you want to delete: ")
                        book.delete_entry(phone_number)
                    else:
                        print(f"Address book '{book_name}' does not exist.")
                elif n == 6:
                    book_name = input("Enter the name of the address book to display: ")
                    book = manager.get_address_book(book_name)
                    if book:
                        print("\n1. Search using city\n2. search using state\n3. get count by city\n4. get count by state")
                        n = int(input("Enter your option: "))
                        if n == 1:
                            search_city = input("Enter the city you want to search: ")
                            book.search_by_city(search_city)
                        elif n == 2:
                            search_state = input("Enter the name of state: ")
                            book.search_by_state(search_state)
                        elif n == 3:
                            book.get_count_city()
                        elif n == 4:
                            book.get_count_state()
                        else:
                            print("Invalid number")
                    else:
                        print(f"Address book '{book_name}' does not exist.")
                elif n == 7:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    manager = AddressBookManager()
    consoles = Address_Book(None)
    consoles.console(manager)

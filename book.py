from collections import OrderedDict
import os

class AddressBookManager:
    def __init__(self):
        self.address_books = {}
        self.load_address_books()

    def create_address_book(self, book_name):
        if book_name not in self.address_books:
            self.address_books[book_name] = Address_Book(book_name)
            self.save_address_books()
            print(f"Address book '{book_name}' created successfully.")
            print('...')
        else:
            print(f"Address book '{book_name}' already exists.")

    def get_address_book(self, book_name):
        return self.address_books.get(book_name, None)

    def save_address_books(self):
        for book_name, book in self.address_books.items():
            book.save_contacts()

    def load_address_books(self):
        for file in os.listdir():
            if file.endswith('.txt'):
                book_name = file[:-4]
                address_book = Address_Book(book_name)
                address_book.load_contacts()
                self.address_books[book_name] = address_book

class Address_Book:
    def __init__(self, name):
        self.name = name
        self.contact = {}

    def add_contact(self, fname=None, lname=None, address=None, city=None, state=None, zip=None, phone_number=None, email=None):
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
                print(f"Added successfully ")
                print(f"{self.contact}")
                self.save_contacts()
            else:
                print(f"{phone_number} already exists in address book")
        else:
            print("Invalid input")

    def display(self):
        if self.contact:
            print("\n1. Sort by Phone Number\n2. Sort by Name")
            n = int(input("Enter your option: "))
            if n == 1:
                print("Print sorted value by key!")
                self.contact = OrderedDict(sorted(self.contact.items()))
                for number, details in self.contact.items():
                    print(f"Phone Number: {number}, Details: {details}")

            elif n == 2:
                print("Print sorted value by firstname!")
                self.contact = dict(sorted(self.contact.items(), key=lambda item: item[1]['firstname']))

                for number, details in self.contact.items():
                    print(f"Phone Number: {number}, Details: {details}")

        else:
            print("No contacts found.")

    def get_count_city(self):
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
            print(f"{'City':^10} - {'Count':^10}")

            for citys, count in city.items():
                print(f"{citys: ^10} : {count: ^10}")
        else:
            print("No contacts found.")

    def get_count_state(self):
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
            print(f"{'State':^10} - {'Count':^10}")
            for states, count in state.items():
                print(f"{states: ^10} : {count: ^10}")
        else:
            print("No contacts found.")

    def search_by_city(self, search_city):
        if self.contact:
            self.contact = OrderedDict(sorted(self.contact.items()))
            print(f"People who live in {search_city} city:")
            for number, details in self.contact.items():
                if details["city"] == search_city:
                    print(f"Phone Number: {number}, Details: {details}")
        else:
            print("No contacts found.")

    def search_by_state(self, search_state):
        if self.contact:
            self.contact = OrderedDict(sorted(self.contact.items()))
            print(f"People who live in {search_state} state:")
            for number, details in self.contact.items():
                if details["state"] == search_state:
                    print(f"{details['firstname']} {details['lastname']}")
        else:
            print("No contacts found.")

    def edit_entry(self, fname=None, lname=None, address=None, city=None, state=None, zip=None, phone_number=None, email=None):
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
        if phone_number and phone_number in self.contact:
            del self.contact[phone_number]
            self.save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Phone number does not exist in the database")

    def save_contacts(self):
        with open(f'{self.name}.txt', 'w') as file:
            for phone_number, details in self.contact.items():
                file.write(f"{phone_number},{details['firstname']},{details['lastname']},{details['address']},{details['city']},{details['state']},{details['zip_code']},{details['email']}\n")

    def load_contacts(self):
        if os.path.exists(f'{self.name}.txt'):
            with open(f'{self.name}.txt', 'r') as file:
                for line in file:
                    phone_number, firstname, lastname, address, city, state, zip_code, email = line.strip().split(',')
                    self.contact[phone_number] = {
                        "firstname": firstname,
                        "lastname": lastname,
                        "address": address,
                        "city": city,
                        "state": state,
                        "zip_code": zip_code,
                        "email": email
                    }

    def console(self, manager):
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

class AddressBookManager:
    def __init__(self):
        self.address_books = {}

    def create_address_book(self, book_name):
        if book_name not in self.address_books:
            self.address_books[book_name] = Address_Book()
            print(f"Address book '{book_name}' created successfully.")
        else:
            print(f"Address book '{book_name}' already exists.")

    def get_address_book(self, book_name):
        return self.address_books.get(book_name, None)

class Address_Book:
    def __init__(self):
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
                print(f"Added successfully {self.contact}")
            else:
                print(f"{phone_number} already exists in address book")
        else:
            print("Invalid input")

    def display(self):
        if self.contact:
            for number, details in self.contact.items():
                print(f"Phone Number: {number}, Details: {details}")
        else:
            print("No contacts found.")

    def search_by_city(self,search_city):
        if self.contact:
            print(f"People who lives in {search_city} city:")
            for number,details in self.contact.items():
                if details["city"]==search_city:
                    print(f"Phone Number: {number}, Details: {details}")
        else:
            print("No contacts found.")
    def search_by_state(self,search_state):
        if self.contact:
            print(f"People who lives in {search_state} state:")
            for number,details in self.contact.items():
                if details["state"]==search_state:
                    # print(f"Phone Number: {number}, Details: {details}")
                    print(f"{details["firstname"]} {details["lastname"]}")
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
            print("Data updated successfully")
        else:
            print("Phone number does not exist in the database")

    def delete_entry(self, phone_number=None):
        if phone_number and phone_number in self.contact:
            del self.contact[phone_number]
            print("Contact deleted successfully!")
        else:
            print("Phone number does not exist in the database")

    def console(self,manager):
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
                        num=int(input("Enter the number of entries you want to add: "))
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
                elif n==6:
                    book_name = input("Enter the name of the address book to display: ")
                    book = manager.get_address_book(book_name)
                    if book:
                        print("\n1. Search using city\n2. search using state\n")
                        n = int(input("Enter your option: "))
                        if n==1:
                            search_city=input("Enter the city you want to search: ")
                            book.search_by_city(search_city)
                        elif n==2:
                            search_state=input("Enter the name of state: ")
                            book.search_by_state(search_state)
                        else:
                            print("Envalid number")
                    else:
                        print(f"Address book '{book_name}' does not exist.")

                elif n == 7:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

# Example usage:
manager = AddressBookManager()
consoles = Address_Book()
consoles.console(manager)

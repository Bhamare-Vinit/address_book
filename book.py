

class Address_Book:
    def __init__(self):
        self.contact={}
    def addContact(self,fname=None,lname=None,address=None,city=None,state=None,zip=None,phone_number=None,email=None):
        if fname!=None and lname!=None and address!=None and city!=None and state!=None and zip!=None and phone_number!=None and email!=None :
            if phone_number not in self.contact:
                self.contact[phone_number]={"firstname":fname,"lastname":lname,"address":address,"city":city,"state":state,"zip_code":zip,"email":email}
                # [fname,lname,address,city,state,zip,email]
                print(f"Added successfully {self.contact}")
                print(self.contact)
            else:
                print(f"{phone_number} is all ready exist in adress book")
        else:
            print("Envalid Input ")

    def display(self):
        if self.contact:
            for number, details in self.contact.items():
                print(f"Phone Number: {number}, Details: {details}")
        else:
            print("No contacts found.")


    def edit_entry(self,fname=None,lname=None,address=None,city=None,state=None,zip=None,phone_number=None,email=None):
        if phone_number != None and phone_number in self.contact:
            lst_info = self.contact[phone_number]
            print(lst_info)
            if fname != None:
                lst_info["firstname"] = fname
            if lname != None:
                lst_info["lastname"] = lname
            if address != None:
                lst_info["address"] = address
            if city != None:
                lst_info["city"] = city
            if state != None:
                lst_info["state"] = state
            if zip != None:
                lst_info["zip"] = zip
            if email != None:
                lst_info["email"] = email
            self.contact[phone_number] = lst_info
            print("Data updated successfully")
        else:
            print("Phone number does not exists in the database")


    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Display Book\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
                n = int(input("Enter your options: "))
                if n == 1:
                    fname = input("Enter first name: ")
                    lname= input("Enter last name: ")
                    address = input("Address: ")
                    city=input("Enter the city: ")
                    state=input("Enter the state: ")
                    zip=input("Enter the zip code: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    if len(fname) == 0:
                        fname = None
                    if len(lname) == 0:
                        lname = None
                    if len(address) == 0:
                        address = None
                    if len(city) == 0:
                        city = None
                    if len(phone_number) == 0:
                        phone_number = None
                    if len(email) == 0:
                        email = None

                    self.addContact(fname, lname, address, city, state, zip, phone_number, email)

                if n==2:
                    self.display()
                
                if n==3:
                    fname = input("Enter first name: ")
                    lname= input("Enter last name: ")
                    address = input("Address: ")
                    city=input("Enter the city: ")
                    state=input("Enter the state: ")
                    zip=input("Enter the zip code: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    if len(fname) == 0:
                        fname = None
                    if len(lname) == 0:
                        lname = None
                    if len(address) == 0:
                        address = None
                    if len(city) == 0:
                        city = None
                    if len(phone_number) == 0:
                        phone_number = None
                    if len(email) == 0:
                        email = None
                    self.edit_entry(fname, lname, address, city, state, zip, phone_number, email)
            except Exception as e:
                pass         

contact_book = Address_Book()
contact_book.console()
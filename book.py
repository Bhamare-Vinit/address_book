

class Address_Book:
    def __init__(self):
        self.contact={}
    def addContact(self,fname=None,lname=None,address=None,city=None,state=None,zip=None,phone_number=None,email=None):
        print("This on ")
        if fname!=None and lname!=None and address!=None and city!=None and state!=None and zip!=None and phone_number!=None and email!=None :
            if phone_number not in self.contact:
                self.contact[phone_number]=[fname,lname,address,city,state,zip,email]
                print(f"Added successfully {self.contact}")
            else:
                print(f"{phone_number} is all ready exist in adress book")
        else:
            print("Envalid Input ")

    def display():
        pass

    def console(self):
        while True:
            try:
                print("\n1. Add Contact\n2. Delete Contact\n3. Edit Contact\n4. Search Contact\n5. View Contacts\n6. Stop")
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
            except Exception as e:
                pass         

contact_book = Address_Book()
contact_book.console()
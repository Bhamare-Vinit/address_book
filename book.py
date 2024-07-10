
def get_contact_details():
    contact = {
        "first_name": input("Enter first name: "),
        "last_name": input("Enter last name: "),
        "address": input("Enter address: "),
        "city": input("Enter city: "),
        "state": input("Enter state: "),
        "zip": input("Enter zip code: "),
        "phone_number": input("Enter phone number: "),
        "email": input("Enter email: ")
    }
    return contact

def display_contact(contact):
    print("\nContact Information:")
    print(f"First Name: {contact['first_name']}")
    print(f"Last Name: {contact['last_name']}")
    print(f"Address: {contact['address']}")
    print(f"City: {contact['city']}")
    print(f"State: {contact['state']}")
    print(f"Zip: {contact['zip']}")
    print(f"Phone Number: {contact['phone_number']}")
    print(f"Email: {contact['email']}")

contact = get_contact_details()

display_contact(contact)

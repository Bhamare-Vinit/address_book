# Original dictionary
contacts = {
    1: {'firstname': 'v', 'lastname': 'v', 'address': 'v', 'city': 'v', 'state': 'mh', 'zip_code': '12', 'email': 'v'},
    2: {'firstname': 'ab', 'lastname': 'o', 'address': 'o', 'city': 'o', 'state': 'mh', 'zip_code': 'o', 'email': 'o'},
    3: {'firstname': 'aa', 'lastname': 'a', 'address': 'a', 'city': 'a', 'state': 'a', 'zip_code': 'a', 'email': 'a'}
}

# Sort the dictionary based on 'firstname'
sorted_contacts = dict(sorted(contacts.items(), key=lambda item: item[1]['firstname']))

# Print the sorted dictionary
print(sorted_contacts)

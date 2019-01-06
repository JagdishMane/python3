#!/usr/bin/env python3.6
user = {'admin': True, 'active': True, 'name': 'Jagdish'}
print(user)
if user['admin'] and user['active']:
    print(f"User is admin and active")
elif user['admin']:
    print(f"ADMIN is {user['name']}")
elif user['active']:
    print(f"User {user['name']} is ACTIVE")
else:
    print(f"User is neigther admin nor active")


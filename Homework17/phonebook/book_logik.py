#coding UTF = 8

import book_methods
import json
import sys
data_ph = open("data_phonebook.json","r+")
data = json.load(data_ph)

while True:
    user_choice = input("For using phonebook type:\nfor reading info: 'read'\nfor exit: 'exit'\n\
for adding :'add'\nfor seaching: 'search'\n").lower()
    if user_choice == "read":
        book_methods.read(data)
    elif user_choice == "add":
        book_methods.add(data, data_ph)
        book_methods.save(data, data_ph)
    elif user_choice == "exit":
        print("bye")
        book_methods.save(data, data_ph)

    elif user_choice == "search":
        book_methods.search(data)
    else:
        print("no such function")
        continue

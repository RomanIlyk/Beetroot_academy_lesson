#coding UTF = 8
import json
data_ph = open("data_phonebook.json","r+")
data = json.load(data_ph)

#data_ph = open("data_phonebook.json","r+")
#opens the whole book
def read(data):
    for k in data.items():
      print(list(k))

#adding contacts
def add(data,number = None,first_name = None,last_name = None,city = None):
        number = input("Please, type contact number: ")
        if len(number) < 11:
            print("not the correct number")
            return add(data,data_ph)
        else:
             first_name = input("Please, type contact first name: ")
             last_name = input("Please, type contact last name: ")
             city = input("Please, type city: ")
             new_data = {number : {"first_name": first_name,"last_name": last_name,"city": city}}
             data.update(new_data)
             json.dump(new_data,data_ph,indent= 4)
#def add(data,data_ph):

#save book
def save(data,dict):
    with open('data_phonebook.json', 'w') as data_ph:
        json.dump(data, data_ph, indent=4)

#search by number
def search(data):
    number_to_read = input("please, type number: ")
    print(data[number_to_read])

#пошук по імені чи призвищу не виходить реалізувати(





import json
from pprint import pprint
import re


def write_(data, filename):
    with open(filename, 'w+', encoding='UTF-8') as file_:
        json.dump(data, file_, indent=4)


def read_(filename):
    with open(filename, 'r+', encoding='UTF-8') as file:
        return json.load(file)


phone_book = {
    'Mark': '+380506585958',
    'Steve': '380545852891'
}

print('!* In this App you can enter one of five available commands.'
      '\nAvailable commands: add, delete, show, list, stats')

while True:
    command = input('Enter a command: ')
    if command == 'add': # add record
        name = input('Enter a name: ')
        phone_book = read_('dict.json')
        if phone_book.get(name):
            print('A record already exist')
        else:
            attempt = 3
            while attempt > 0:
                phone = input('Enter a phone number: ')
                if re.fullmatch('(\+380|380|0)\d{9}', phone):
                    phone_book[name] = phone
                    write_(phone_book, 'dict.json')
                    print('A new record created')
                    break
                else:
                    attempt -= 1
                    print(f'{attempt} attempts left')
                    print("Please, input a valid phone number")

    elif command == 'delete':         # delete record by name(key)
        del_name = input('Enter the name that you would like to delete: ')
        phone_book = read_('dict.json')
        if phone_book.get(del_name):
            del phone_book[del_name]
            write_(phone_book, 'dict.json')
            print(f'The {del_name} has been successfully deleted from the phone book')
        else:
            print(f"The {del_name} doesn't exist in the phone book. Please try again!!!" )

    elif command == 'show':             # detail info by name
        show_name = input('Enter a name: ')
        phone_book = read_('dict.json')
        if phone_book.get(show_name):
            print(show_name, phone_book[show_name])
        else:
            print(f"The {show_name} doesn't exist in the phone book. Please try again!!!")

    elif command == 'list':             # list of all names in phone book
        phone_book = read_('dict.json')
        pprint(phone_book)

    elif command == 'stats':             # Amount of records
        phone_book = read_('dict.json')
        if len(phone_book) == 1:
            str_ = 'record'
        else:
            str_ = 'records'
        print(f'Phone Book contains {len(phone_book)} {str_}')
    else:
        print('Unknown command.\nThis App allow you enter only one from 5 available commands:'
              '\nadd, delete, show, list, stats ')

import json
from pprint import pprint


def write_(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='UTF-8') as file_:
        json.dump(data, file_, indent=4)


def read_(filename):
    with open(filename, 'r+', encoding='UTF-8') as file:
        return json.load(file)


phone_book = {
    'Mark': '+48523654785',
    'Steve': '+8054585289'
}

print('!* In this App you can enter one of five available commands.'
      '\nAvailable commands: add, delete, show, list, stats')

while True:
    command = input('Enter a command: ')
    if command == 'add': # додати запис
        name = input('Enter a name: ')
        phone_book = read_('dict.json')
        if phone_book.get(name):
            print('A record already exist')
        else:
            phone = input('Enter a phone number: ')
            phone_book[name] = phone
            write_(phone_book, 'dict.json')
            print('A new record created')

    elif command == 'delete':         # всвидалити запис за іменем (ключем)#
        del_name = input('Enter the name that you would like to delete: ')
        phone_book = read_('dict.json')
        if phone_book.get(del_name):
            del phone_book[del_name]
            write_(phone_book, 'dict.json')
            print(f'The {del_name} has been successfully deleted from the phone book')
        else:
            print(f"The {del_name} doesn't exist in the phone book. Please try again!!!" )

    elif command == 'show':             # детальна інформація по імені
        show_name = input('Enter a name: ')
        phone_book = read_('dict.json')
        if phone_book.get(show_name):
            print(show_name, phone_book[show_name])
        else:
            print(f"The {show_name} doesn't exist in the phone book. Please try again!!!")

    elif command == 'list':             # список всіх імен в книзі
        phone_book = read_('dict.json')
        pprint(phone_book)

    elif command == 'stats':             # кількість записів
        phone_book = read_('dict.json')
        if len(phone_book) == 1:
            str_ = 'record'
        else:
            str_ = 'records'
        print(f'Phone Book contains {len(phone_book)} {str_}')
    else:
        print('Unknown command.\nThis App allow you enter only one from 5 available commands:'
              '\nadd, delete, show, list, stats ')


import datetime
import inspect

func_name = None


def my_decorator_func(func):
    def deco_func():
        func()
        global func_name
        frame = inspect.currentframe()
        func_name = inspect.getframeinfo(frame).function
        now_ = datetime.datetime.now().strftime("%H:%M")
        dict_ = {func_name: now_}
        json_data = json.dumps(dict_)
        with open('Deco.json', 'w', encoding='UTF-8') as file:
            file.write(json_data)
    return deco_func


@my_decorator_func
def my_func():
    print('This is my func')


my_function = my_decorator_func(my_func)

my_func()


class MyCustomException(Exception):
    def __init__(self):
        message = 'Custom exception is occurred!'
        super().__init__(message)


try:
    raise MyCustomException()
except MyCustomException as error_:
    e = error_
    now_ = datetime.datetime.now().strftime("%H:%M")
    json_text = json.dumps(f'{e} at {now_}')
    json_text = json.loads(str(json_text))
    with open('Deco.json', 'w', encoding='UTF-8') as file:
        json.dump(json_text, file)
finally:
    print('The error text was recorded in the Deco.json')


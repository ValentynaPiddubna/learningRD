phone_book = {'Mark': '234565456',
              'Steve': '345434565',
              'Vasyl': '456985698'

}

print('!* In this App you can enter one of five available commands.'
      '\nAvailable commands: add, delete, show, list, stats')

while True:
    command = input('Enter a command: ')
    if command == 'add': # додати запис
        name = input('Enter a name: ')
        if phone_book.get(name):
            print('A record already exist')
        else:
            phone = input('Enter a phone number: ')
            phone_book[name] = phone
            # phone_book[phone] = phone
            print('A new record created')
    elif command == 'delete': # всвидалити запис за іменем (ключем)#
        del_name = input('Enter the name that you would like to delete: ')
        if phone_book.get(del_name):
            del phone_book[del_name]
            print(f'The {del_name} has been successfully deleted from the phone book')
        else:
            print(f"The {del_name} doesn't exist in the phone book. Please try again!!!" )

    elif command == 'show': #  детальна інформація по імені
        show_name = input('Enter a name: ')
        if phone_book.get(show_name):
            print(show_name, phone_book[show_name])
        else:
            print(f"The {show_name} doesn't exist in the phone book. Please try again!!!")

    elif command == 'list': # список всіх імен в книзі #
        for key in phone_book:
           print(key, phone_book[key])

    elif command == 'stats': # кількість записів
        if len(phone_book) == 1:
            str = 'record'
        else:
            str = 'records'
        print(f'Phone Book contains {len(phone_book)} {str}')
    else:
        print('Unknown command.\nThis App allow you enter only one from 5 available commands:'
              '\nadd, delete, show, List, stats ')



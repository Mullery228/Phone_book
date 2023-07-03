from .text import *


def menu() -> int:
    print(main_menu)
    while True:
        choise = input(choising)
        if choise.isdigit() and 0 < int(choise) < 9:
            return int(choise)
        print(error)

def print_message(message: str):
    lenht = len(message)
    print('\n' + '-'*lenht)
    print(message)
    print('-'*lenht + '\n')

def show_all_contacts(book: list[dict[str, str]]):
    if book:
        print('\n' + '-'*87)
        print('  ID', 'Имя', 'Номер телефона', 'Описание', 'Город', sep='            ')
        for contact in book:
            uid = contact.get('id')
            name = contact.get('name')
            phone = contact.get('phone')
            comment = contact.get('comment')
            city = contact.get('city')
            print(f'{uid:>3}) {name:<20} | {phone:<20} | {comment:<20} | {city:<20}')
        print('-'*87 + '\n')
    else:
        print(book_error)

def return_input(message: str):
    print(message)
    name = input(new_contact[0])
    phone = input(new_contact[1])
    comment = input(new_contact[2])
    city = input(new_contact[3])
    return {'name': name, 'phone': phone, 'comment': comment, 'city': city}

def search_contact(message: str):
    print()
    return input(message)

def delete_contact(message: str):
    print()
    return input(message)

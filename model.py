
book = []

path = 'contacts.txt'

def open_file():
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        us_id, name, phone, comment, city = contact.strip().split(';')
        book.append({'id': us_id, 'name': name, 'phone': phone, 'comment': comment, 'city': city})
    print(book)

def check_id():
    uid_list = []
    for contact in book:
        uid_list.append(int(contact.get('id')))
    return {'id': max(uid_list) + 1}

def add_contact(new: dict):
    new.update(check_id())
    book.append(new)

def search(word: str):
    result = []
    for contact in book:
        for value in contact.values():
            if word.lower() in value.lower():
                result.append(contact)
                break
    return result

def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            book[index-1][key] = field

def delete(index: int):
    print(index - 1)
    book.pop(index - 1)

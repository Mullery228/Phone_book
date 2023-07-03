import model
from view import menu, show_all_contacts, print_message, return_input, search_contact, delete_contact
from view import text

def start():
    while True:
        choise = menu()
        match choise:
            case 1:
                model.open_file()
                print_message(text.open_suc)
            case 2:
                pass
            case 3:
                show_all_contacts(model.book)
            case 4:
                new = return_input(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                word = search_contact(text.search_word)
                result = model.search(word)
                show_all_contacts(result)
            case 6:
                word = search_contact(text.search_word)
                result = model.search(word)
                show_all_contacts(result)
                index = search_contact(text.input_index)
                new = return_input(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.book[int(index) - 1].get('name')
                print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))

            case 7:
                word = search_contact(text.search_word)
                result = model.search(word)
                show_all_contacts(result)
                index = search_contact(text.input_index)
                model.delete(int(index))
            case 8:
                break

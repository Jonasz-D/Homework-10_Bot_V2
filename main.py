from collections import UserDict, UserList

def input_error(func):
    def inner(base_command, command):
        try:
            return func(base_command, command)
        except KeyError:
            return 'The command is not exist'
            
        except ValueError:
            return 'Phone number must consist of numbers'
        
        except IndexError:
            return 'Not given name or phone number'

    return inner


class Field:
    def __init__(self, contact_data):
        self.contact_data = contact_data
    

class Name(Field):
    def __init__(self, contact_data):
        super().__init__(contact_data)
        

class Phone(Field):
    def __init__(self, contact_data):
        super().__init__(contact_data)

        if not self.contact_data.isdigit():
            raise ValueError

class Record():
    def __init__(self, contact_name):
        self.name = Name(contact_name)
        self.phone_num = []

    def add_phone(self, phone):
        self.phone_num.append(str(Phone(phone)))

    def remove_phone(self, phone):
        self.phone_num.remove(str(Phone(phone)))

    def change_phone(self, phone, new_phone):
        self.phone_num.remove(str(Phone(phone)))
        self.phone_num.append(str(Phone(new_phone)))


class AdressBook(UserDict):
    def add_record(self, name):
        self.data[Record(name).name] = Record(name)

    def show_all(self):
        all_contacts = ''
        for contact, phones in self.data.items():
            all_contacts += f'Name: {str(contact):<10} Phone number: {phones.phone_num}\n'

        return all_contacts
    
def hello(command):
    return 'How can I help you?'

def create_contact(command):
    name = command[1]
    if list(contacts.keys()) == []:
        return contacts.add_record(name)

    for contact in contacts.keys():
        if name == str(contact):
            return 'The contact already exists'
        
    return contacts.add_record(name)

def add_phone(command):
    name, phone = command[1], command[2]
    for contact, phones in contacts.items():
        if name == str(contact) and phone not in phones.phone_num:
            phones.add_phone(phone)
            return
      
    return "The contact doesn't exists or phone number was already added"

def change_phone_num(command):
    name, phone_num, new_phone = command[1], command[2], command[3]
    
    for contact, phones in contacts.items():
        if name == str(contact) and phone_num in phones.phone_num:
            phones.change_phone(phone_num, new_phone)
            return
    return "The contact or phone number doesn't exists"

def show_contact(command):
    name = command[1]
    for contact, phones in contacts.items():
        if name == str(contact):
            return f'contact name: {str(contact)}; phones: {phones.phone_num}'
    
    return f"contact name: {name} doesn't exists"

def delete_phone(command):
    name, phone = command[1], command[2]
    for contact, phones in contacts.items():
        if name == str(contact) and phone in (phones.phone_num):
            phones.remove_phone(phone)
            return
        
    return "The contact or phone number doesn't exists"
    
def show_all(command):
    return contacts.show_all()

def end_program(command):
    return False

def accepted_commands(command):
    commands = (list(OPERATIONS.keys()))
    message = ''
    for command in commands:
        message += f'"{command}" '
        
    return f"Accepted commands: {message}"


OPERATIONS = {
    'accepted_commands':accepted_commands,
    'hello': hello,
    'create_contact': create_contact,
    'add_phone': add_phone,
    'change_phone_num': change_phone_num,
    'show_contact': show_contact,
    'delete_phone': delete_phone,
    'show_all': show_all,
    'good_bye': end_program, 
    'close': end_program, 
    'exit': end_program, 
    '.': end_program, 
}

@input_error
def handler_command(base_command, command):
    return OPERATIONS[base_command](command)

def main():
    flag = True
    print(accepted_commands(OPERATIONS))
    while flag:
        command = input('Write your command: ').lower().strip().split()

        try:
            base_command = command[0]
        except IndexError:
            continue

        handler = handler_command(base_command, command)

        if isinstance(handler, str):
            print(handler)
        
        elif isinstance(handler, bool):
            flag = handler

        else:
            handler


contacts = AdressBook()

if __name__ == '__main__':
    main()

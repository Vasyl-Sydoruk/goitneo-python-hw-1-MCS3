def parse_input(user_input):

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        name_index = args.index(name)
        args.insert(name_index, phone)
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Sorry your number isn't in database"

def show_all(contacts):
    all_contacts = ''
    for name, phone in contacts.items():
        all_contacts += f'{name} - {phone},'

    all = all_contacts.split(',')
    
    result = ''
    for item in all:
        if item == all[-2]:
            result += item
        elif item != '':
            result += f'{item}\n'

    return result



    

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError:
                print("Please type in format: <command> <name> <phone>")
                continue
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError:
                print("Please type in format: <command> <name> <phone>")
                continue
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
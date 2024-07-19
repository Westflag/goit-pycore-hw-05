def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as error:
            args_count = len(args[0])
            if(args_count == 0): return "Give me name and phone please."
            if(args_count == 1): return "Enter phone number"
            return "Enter the argument for the command"

    return inner

def input_error_find(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as error:
            args_count = len(args[0])
            if(args_count == 0): return "Enter name"
            return "Enter the argument for the command"

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    exist = name in contacts.keys() 
    contacts[name] = phone
    result = ""
    if(exist):
       result = "Contact updated." 
    else: result = "Contact added."
    return result

@input_error
def update_contact(args, contacts):
    name, phone = args
    exist = name in contacts.keys() 
    result = ""
    if(exist):
        contacts[name] = phone
        result= "Contact updated"
    else:
        result = "Contact not found."   
    return result

@input_error_find
def find_contact(args, contacts):
    name = args[0]
    exist = name in contacts.keys() 
    result = ""
    if(exist):
        result = contacts[name]
    else:
        result = "Contact not found."   
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
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "all":
            print(contacts)        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

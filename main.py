#Task 1#
def total_salary(path):
    total_salary = 0
    developer_count = 0
 
    try:
        with open(path, 'r') as file:
            for line in file:
                name, salary = line.strip().split(',')
                salary = int(salary)
                total_salary += salary
                developer_count += 1
 
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    average_salary = total_salary / developer_count
    return total_salary, average_salary
salary_path = "path/to/salary_file.txt"
total, average = total_salary(salary_path)
print(f"The total salary of all developers is {total} and the average salary is {average}.")


#Task 2#
def get_cats_info(path):
    cats_info = []
    with open(path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                cat_id, name, age = parts
                cat_dict = {
                    'id': cat_id,
                    'name': name,
                    'age': int(age)
                }
                cats_info.append(cat_dict)
    
    return cats_info


#Task_3#
import sys
import colorama
from pathlib import Path


colorama.init()
BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
RESET_ALL = ""
DEEP_TAB = "\t"


def my_scandir(path, tab):  
    p = Path(path)
    for child in p.iterdir():         
        if child.is_dir()==True:    
            print(f"{BLUE}{DEEP_TAB* tab}{str(child.name)}{RESET_ALL}")
            my_scandir(path=str(child), tab=tab+1)
        else:
             print(f"{GREEN}{DEEP_TAB* tab}{str(child.name)}{RESET_ALL}")
    

if __name__ == "__main__":
     if len(sys.argv)<=1:
        print("dir argument not found")
        exit(-1)
     start_path = sys.argv[1]
     start =Path(start_path)     
     if not start.is_dir():
         print("dir argument is not a dir")
         exit(-2)
     print(f"{BLUE}{start_path}{RESET_ALL}")
     my_scandir(path=start_path, tab=1)


#Task_4#
contacts = {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")


def change_contact(name, phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Contact {name} updated.")
    else:
        print(f"Contact {name} not found.")


def show_phone(name):
    if name in contacts:
        print(f"The phone number for {name} is {contacts[name]}.")
    else:
        print(f"Contact {name} not found.")


def show_all():
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add" and len(args) == 2:
            add_contact(args[0], args[1])
        elif command == "change" and len(args) == 2:
            change_contact(args[0], args[1])
        elif command == "phone" and len(args) == 1:
            show_phone(args[0])
        elif command == "all":
            show_all()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
#To Do List
user_input = 'random'
data = []

def show_menu():
    print("\nMenu: ")
    print("1. Add an item") 
    print("2. Mark as done")
    print("3. View item")
    print("4. Exit")

while user_input != '4':

    show_menu()
    user_input = input("\nEnter your choice: ")

    if user_input == '1':
        item = input("\nWhat is to be done? :")
        data.append(item)
        print("\nAdded item: ",item)
    elif user_input == '2':
        item= input("\nWhat is to be marked as done?: ")
        if item in data:
            data.remove(item)
            print("\nRemoved item: ",item)
        else:
            print("Item does not exist in the list")
    elif user_input == '3':
        print("\nList of to-do itmes:")
        for item in data:
            print(item)
    elif user_input == 4:
        print("Exit")
        print("Good Bye!!")
    else:
        print("Please enter one of 1, 2, 3, or 4")
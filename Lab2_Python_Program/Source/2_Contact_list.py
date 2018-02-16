Contact_list=[{"name":"Barath","number":"5122031577","email":"rr@gmail.com"},
              {"name":"Phani","number":"8169081577","email":"ss@gmail.com"}]

def menu():
    print("\nMenu:\n1.Display contact by name\n2.Display contact by number\n3.Edit contact by name\n4.Exit\nEnter choice:")
    choice = input()
    return int(choice)

while True:
    choice = menu()

    #display contact by name
    if choice==1:
        name = input("Enter name:")
        for x in Contact_list:
            if(x.get("name") == name):
                print(x)

    # display contact by number
    elif choice == 2:
        number = input("Enter number:")
        for x in Contact_list:
            if (x.get("number") == number):
                print(x)
    # Edit contact by number or email
    elif choice == 3:
        name = input("Enter name:")
        for x in Contact_list:
            if (x.get("name") == name):
                option = input("1.Edit number\n2.Edit email\nEnter choice:")
                options_value = int(option)
                if options_value == 1:
                    new_number = input("Enter new number:")
                    x["number"] = new_number
                if options_value == 2:
                    new_email = input("Enter new email:")
                    x["email"] = new_email
                print(x)
    #exit
    elif choice == 4:
        break
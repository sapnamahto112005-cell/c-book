# yeh mera github ka 1st project hai

def Add_contact():

    with open("phone_boot.txt", "a") as file:

        name = input("Enter your name: ")

        phone_num = input("Enter your phone number: ")

        try:
            if not phone_num.isdigit():
                raise ValueError

            if len(phone_num) != 10:
                raise ValueError

        except ValueError:
            print("Please enter a valid 10-digit phone number!")
            return

        email_add = input("Enter your email address: ")

        file.write(f"Information: {name}\n")
        file.write(f"Contact: {phone_num}\n")
        file.write(f"E-mail: {email_add}\n")
        file.write("-----------------------------\n")

        print("Contact added successfully!")


def View_contact():

       with open("phone_boot.txt","r") as file:
           content = file.read()

       print("\n------------All Contact----------------")
       print(content)   

def search_contact():

       search_name = input("enter name (what u search): ")

       with open("phone_boot.txt","r") as file:

           for line in file:

               if search_name.lower() in line.lower():
                   print("contact found!!!")
                   print(line)
                   return

       print("contact not found!!!!")       

while True:

    print("\n-----------------------------")
    print("Welcome to our Phone Book!")
    print("-----------------------------")

    print("\n1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Add_contact()

    elif choice == "2":
        View_contact()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")



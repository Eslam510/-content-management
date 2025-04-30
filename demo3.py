import os
contacts = {}
def clear_screen () :
    os.system("cls" if os.name == "nt" else "clear")
while True :
    
    print("Contant mangment")
    print("1- Add contant :")
    print("2- View contant :")
    print("3- Edit contant :")
    print("4- Exit :")
    
    user_choice = input("please choose a number from 1-4\n")
    if user_choice == "1" :
        id = input("Enter the contact ID \n ")
        name = input("please type a name \n")
        phone = input("please type a phone number\n")
        contacts[id] = {"name":name,"number":phone}
        print(f"{name} was add successfuly ")

    elif user_choice == "2" :
        print(contacts)

    elif user_choice == "3" :
        id_edit = input("please entr an ID edit :\n")
        name_edit = input("Enter a new name :\n")
        phone_edit = input("Enetr a new number :\n")
        contacts[id_edit] = {"name":name_edit,"phone":phone_edit}
        print("Success.........")
        
    elif  user_choice == "4" :
        print("Exiting program..........") 
        break
    
    else :
        print("Invalid choice !!!")

       
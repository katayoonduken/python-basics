phone ={}
while True:
    print("1) Add contact")
    print("2) Search contact")
    print("3) Show all contacts")
    print("4) Delete contact")
    print("5) Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("enter name: ").lower()
        if name not in phone:
            number = input("enter number: ")
            phone[name] = number
        else:
            edit =int(input("already exsit do you want to to edit?(if yes enter 1 or no enter 2: ) "))
            if edit == 1:
                replacenumber = input(" enter your  number edit ")
                phone[name]= replacenumber
            else:
                print(" ok ")
    elif choice == 2:
        num = input("enter name :").lower()
        if num in  phone:
            print(phone[num])
        else:
            print("that name is not exist")
    elif choice == 3:
        if 1<= len(phone):
            for name , number in phone.items():
                print(f"{name} : {number}")
        else:
            print(" empty")
    elif choice == 4:
        delt =input(" enter name: ").lower()
        if delt in phone:
            phone.pop(delt)
        else:
            print("is not exist")
    elif choice == 5:
        break
    else:
        print(" only 1 ,2 ,3 ,4 ,5")


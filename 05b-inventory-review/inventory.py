items ={}
LOW_STOCK_LIMIT = 5 
while True:
    print("1) Add item")
    print("2) Remove stock")
    print("3) Show inventory")
    print("4) Delete item by number")
    print("5) Total units")
    print("6) Exit")
    user = int(input("enter your choice: "))
    if user == 1:
        item = input(" enter your item: ").lower()
        numitem = int(input(" enter your numitem: "))
        if numitem > 0 :
            if item in items:
                add =int(input("Should it be added to the existing balance? (yes =1 or no = 2)"))
                if add == 1:
                    items[item] += numitem
                else:
                    print("ok")
            else:
                items[item] =numitem
        else:
            print("The quantity must be positive.")
    elif user==2:
        restok = input("Enter the item you want : ").lower()
        if restok in items:
            numrestok = int(input("Enter the quantity you want: "))
            if 0 < numrestok <= items[restok]:
                items[restok] -= numrestok
                if items[restok] == 0:
                    items.pop(restok)

            else:
                print("You either entered a negative number or an amount greater than your balance.")
        else:
            print("Item does not exist")

    elif user == 3:
        if len(items) > 0:
            for number , (name, qty) in  enumerate(items.items() , start = 1):
                if qty < LOW_STOCK_LIMIT:
                    mark = " (LOW)"
                else:
                    mark = ""
                print(f"{number}. {name}: {qty}{mark}")
        else:
            print("The warehouse is empty.")


    elif user  == 4 :
        removeitem = int(input("Enter the item number you wish to delete: "))
        if 1 <= removeitem <=len(items) :
            names = list(items)
            name =names[removeitem-1]
            items.pop(name)
        else:
            print("Does not exist")

    elif user == 5:
        total = 0

        for qyt in items.values():
            total += qyt
        print(total)

    elif user == 6:
        break
    else:
        print("only 1 2 3 4 5  6")


            




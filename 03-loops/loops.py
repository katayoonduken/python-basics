

while True:
    print("hello pick your item")
    print(" 1) Multiplication table")
    print(" 2) Sum of numbers from 1 to N")
    print(" 3) Exit")
    user = int(input("enter your choice: " ))
    if user == 1:
        number = int(input("enter a number: "))
        for x in range(1,11):
            print(f"{number} x {x} = {number * x}")
    elif user == 2:
        number_s =int(input("enter a number: "))
        total = 0
        for i in range(1, number_s + 1):
            total = total + i
        print(total)

    elif user == 3:
        break
    else:
        print("only pick from the given options")
        
    




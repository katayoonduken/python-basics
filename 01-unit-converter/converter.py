choice = int(input("Enter the conversion you want: select option 1 for Celsius to Fahrenheit, or option 2 for the reverse."))
if choice == 1:
    celsius = float(input("enter celsius: "))
    conversion_f = celsius *9/5 +32 
    print(f"{celsius}C = {conversion_f}F")  

elif choice == 2:
    fahrenheit = float(input("enter fahrenheit: "))
    conversion_c = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}F = {conversion_c}C")
else:
    print("Invalid option selected. Please choose either 1 or 2.")



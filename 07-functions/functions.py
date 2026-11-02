
def is_palindrome(text):
    x = text.lower().replace(" ","")
    return x == x[::-1]

def count_digits(text):
    count = 0
    for ch in text:
        if ch.isdigit():
            count += 1
    return count
def count_upper(text):
    upword =0
    for ch in text:
        if ch.isupper():
            upword += 1
    return upword
def count_lower(text):
    lowword = 0
    for ch in text:
        if ch.islower():
            lowword += 1 
    return lowword
def count_special(text):
    speword = 0
    for ch in text :
        if  not ch.isalnum():
            speword += 1 
    return speword
def missing_rules(password):
    missing = []
    if len(password) < 8:
        missing.append("length")
    if count_digits(password) == 0:
        missing.append("digit")
    if count_upper(password) == 0:
        missing.append("uppercase")
    if count_lower(password) == 0:
        missing.append("lowercase")
    if count_special(password) == 0:
        missing.append("specialcase")

    return missing
def strength(password):
    satisfied = 5 - len(missing_rules(password))
    if satisfied == 5:
        return "strong"
    elif satisfied>= 3:
        return "medium"
    else:
        return "weak"

def show_menu():
    print("1) Palindrome checker")
    print("2) Password strength")
    print("3) Exit")

def main():
    while True:
        show_menu()
        user = int(input("Enter your choice: "))
        if user == 1:
            text = input("Enter your text: ")
            if text.strip() == "":
                print("enter some text")    
            elif is_palindrome(text):              
                print("Palindrome")
            else:
                print("Not palindrome")
        elif user == 2:
            password = input("Enter your password: ")
            print(strength(password))                
            missing = missing_rules(password)
            if missing:
                print("Missing:", ", ".join(missing))
            else:
                print("Missing: none")
        elif user == 3:
            break
        else:
            print("Only 1, 2, 3")

main()

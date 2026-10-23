while True:
    print("1) Palindrome checker")
    print("2) Password strength")
    print("3) Exit")
    user = int(input( " enter your chioce :"))
    if user == 1 :
        text = input("enter your txet: ").lower().replace(" ","")
        if text == text[::-1]:
            print(" Palindrome ")
        else:
            print(" not Palindrome")
    elif user == 2:
        passw = input(" enter your password: ")
        paseg = len(passw) >= 8
        pasup = False
        paslo = False
        pasdi = False
        pasas = False

        for i in passw:
            if i.isupper():
                pasup = True
            elif i.islower():
                paslo = True
            elif i.isdigit():
                pasdi = True
            if not i.isalnum():
                pasas = True

        score = 0
        if paseg == True:
            score += 1
        if pasup == True:
            score += 1
        if paslo == True:
            score += 1
        if pasdi == True:
            score += 1
        if pasas == True:
            score += 1

        if score == 5:
            print("strong")
        elif score >= 3:
            print("medium")
        else:
            print("weak")

        miss = []

        if not paseg:
            miss.append("length")
        if not pasup:
            miss.append("uppercase")
        if not paslo:
            miss.append("lowercase")
        if not pasdi:
            miss.append("digit")
        if not pasas:
            miss.append("special")

        if miss:
            print("missing:", ", ".join(miss))
        else:
            print("missing: none")
        

    elif user == 3:
        break
    else:
        print("only 1 ,2 ,3")



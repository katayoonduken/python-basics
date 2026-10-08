score = float(input("enter your score: "))
if score > 100 or score < 0:
    print("Invalid score. Please enter a score between 0 and 100.")
    exit()
elif score >= 90 and score <= 100:
    if score >= 97:
        print("Your grade is A+")
    elif score >= 93:
        print("Your grade is A")
    elif score >= 90:
        print("Your grade is A-")
elif score >= 80:
    if score >= 87:
        print("Your grade is B+")
    elif score >= 83:
        print("Your grade is B")
    elif score >= 80:
        print("Your grade is B-")
elif score >= 70 :
    if score >= 77:
        print("Your grade is C+")
    elif score >= 73:
        print("Your grade is C")
    elif score >= 70:
        print("Your grade is C-")
elif score >= 60 :
    print("Your grade is D")
else:
    print("your grade is F")

if score >= 60 :
    print("status: passed")
else:
    print("status: failed")
   

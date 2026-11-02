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


print(missing_rules("Abcdefg1!"))


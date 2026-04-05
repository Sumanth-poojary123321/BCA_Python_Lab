def nearlyEqual(str1, str2):
    count = 0
 
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            count += 1

    count += abs(len(str1) - len(str2))


    if count > 1:
        return False
    else:
        return True



str1 = input("Enter First string: ")
str2 = input("Enter Second string: ")

if nearlyEqual(str1, str2):
    print("Strings are nearly equal")
else:
    print("Strings are not nearly equal")
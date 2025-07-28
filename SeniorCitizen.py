#Program to read Name and Year of Birth of The Person and check whether Senior Citizen or not

name_ = input("Please Enter the Name of Person: ")
yearOfBirth = int(input("Please Enter the Year of Birth: "))

if yearOfBirth<1960:
    print("---SENIOR CITIZEN---")

else:
    print("---Not a SENIOR CITIZEN---")
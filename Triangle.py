#This Program is to Determine the Type of Triangle, Whether it is a valid Triangle or A Equilateral or Isoscles or Scalene

s1=int(input("Enter the First Side of the Triangle: "))
s2=int(input("Enter the Second Side of the Triangle: "))
s3=int(input("Enter the Third Side of the Triangle: "))

if s1>=0 and s2>=0 and s3>=0:
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s3 + s2 > s1):
        print("It is a Valid Triangle")
        if s1 == s2 and s2 == s3:
            print("---The Triangle is a Equilateral Triangle---")
        elif s1==s2 or s2==s3 or s1 == s3:
            print("---The Triangle is a Isoscles Triangle---")
        else:
            print("---The Triangle is a Scalene Triangle---")
    else:
        print("---It is not a Valid Triangle---")

else:
    print("---All Sides of a Triangle has to be Positive---")
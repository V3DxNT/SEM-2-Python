def C2F():
    centi=float(input("Enter the Temperature in Centigrade to Convert: "))
    faren=(centi * (9/5))+32
    print("The Farenheit Temperature is: " + str(faren) + 'F')

def F2C():
    far=float(input("Enter the Temperature in Farenheit to Convert:"))
    cel=(far -32) * (5/9)
    print("The Centigrade Temperature is: " + str(cel)  + "'")


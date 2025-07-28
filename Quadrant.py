def Quadrant(x, y):
    if x == 0 and y == 0:
        return "The point is at the Origin."
    elif x == 0:
        return "The point lies on the Y-axis."
    elif y == 0:
        return "The point lies on the X-axis."
    else:
        quadrant_lookup = {
            (True, True): "Quadrant I",
            (False, True): "Quadrant II",
            (False, False): "Quadrant III",
            (True, False): "Quadrant IV"
        }
        position = quadrant_lookup[(x > 0, y > 0)]
        return "The point lies in "+ position

x=int(input("Enter the X of the Cordinate: "))
y=int(input("Enter the Y of the Cordinate: "))
print(Quadrant(x, y))

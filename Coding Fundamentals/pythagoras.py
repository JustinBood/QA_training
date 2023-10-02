print("Here are your options \n 1) Find tge length of A given B and C \n 2) Find the length of B given A and C \n 3) Find the length of C given A and B")
while True:
    selection = input("Enter 1,2 or 3")
    if selection != "1" or selection != "2" or selection != "3":
        print("Try again")
    else:
        break

if selection == "1":
    b = float(input("Enter length of side B: "))
    c = float(input("Enter length of side C: "))
    a = ((c**2)-(b**2)) ** 0.5
    print(a)

if selection == "2":
    a = float(input("Enter length of side A: "))
    c = float(input("Enter length of side C: "))
    b = ((c**2)-(a**2)) ** 0.5
    print(b)

if selection == "3":
    a = float(input("Enter length of side A: "))
    b = float(input("Enter length of side C: "))
    c = ((a**2)+(b**2)) ** 0.5
    print(c)
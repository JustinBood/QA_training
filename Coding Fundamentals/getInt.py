min = 1
max = 100
t = True
count = 0
while t:
    num = int(input("Enter a number:"))

    if num >min and num < max:
        print(num)
        break
    elif count == 2:
        print(None)
        t= False
    else:
        print("Wrong try again")
        count +=1
    
 

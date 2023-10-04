menu = "1) Add 2 times \n 2) Find the difference between 2 times \n 3) Convert into Hours \n 4) Convert into minutes \n 5) Convert Minutes to Time \n 6) Convert Hours into Time \n 7) Convert Days into Time"
choice = int(input("Enter your choice: "))

if choice == 1 or choice == 2:
    time1 = input("Enter your first time in the following format DD:HH:MM: ")
    time2 = input("Enter your second time in the following format DD:HH:MM: ")
elif choice == 3 or choice == 4:
    time1 = input("Enter your time in the following format DD:HH:MM: ")
elif choice == 5 or choice == 6 or choice == 7:
    time = int(input("Enter your Hour/Minute/Day to be converted: "))

if choice == 1:
    list1 = time1.split(":")
    day1 = list1[0]
    hour1 = list1[1]
    min1 = list1[2]

    list2 = time2.split(":")
    day2 = list2[0]
    hour2 = list2[1]
    min2 = list2[2]

    dayc = int(day1) + int(day2)
    hourc = int(hour1) + int(hour2)
    minc = int(min1) + int(min2)
    
    if minc >= 60:
        hourc += minc // 60
        minc = minc % 60
    
    if hourc >= 24:
        dayc += 24 // hourc
        hourc = 24 % hourc
    comp = (f"{dayc}:{hourc}:{minc}")

    print(comp)
elif choice == 2:
    list1 = time1.split(":")
    day1 = list1[0]
    hour1 = list1[1]
    min1 = list1[2]

    list2 = time2.split(":")
    day2 = list2[0]
    hour2 = list2[1]
    min2 = list2[2]

    dayc = int(day1) - int(day2)
    hourc = int(hour1) - int(hour2)
    minc = int(min1) - int(min2)

    while minc < 0:
        minc += 60
        hourc -= 1
    
    while hourc < 0:
        hourc += 24
        dayc -= 1
    
    comp = (f"{dayc}:{hourc}:{minc}")

    print(comp)

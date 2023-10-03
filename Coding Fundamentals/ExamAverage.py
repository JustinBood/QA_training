while True:
    score1 = int(input("Enter your ICT score: "))
    if score1 >= 1 and score1 <= 100:
        break
    else:
        print("Please enter your proper grade.")

while True:
    score2 = int(input("Enter your English score: "))
    if score2 >= 1 and score2 <= 100:
        break
    else:
        print("Please enter your proper grade.")

while True:
    score3 = int(input("Enter your Math score: "))
    if score3 >= 1 and score3 <= 100:
        break
    else:
        print("Please enter your proper grade.")

average = (score1 + score2 + score3) / 3

if average >= 65:
    print("Well done, you passed. Your average was", average)
else:
    print("You failed. Your average was", average)

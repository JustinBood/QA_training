age = int(input("What's your age? "))

if age >= 18:
    print("You're in category A")
elif age >= 16:
    print("You're in category B")
elif age < 16:
    print("You're in category C")
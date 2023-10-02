while True:
    score = int(input("Enter your grade: "))
    if score >= 1 and score <= 100:
        break
    else:
        print("Please enter your proper grade.")

while True:
    level = int(input("Enter your level: "))
    if level == 1 or level == 2:
        break
    else:
        print("Please enter your correct level.")

if level == 1:
    if score >= 71:
        grade = "Distinction"
    elif score >60:
        grade = "Merit"
    elif score >=50:
        grade = "Pass"
    else: 
        grade = "Fail"
else:
    if score >= 66:
        grade = "Distinction"
    elif score >=51:
        grade = "Merit"
    elif score >=40:
        grade = "Pass"
    else: 
        grade = "Fail"
    
print(f"Your grade is: {grade}")
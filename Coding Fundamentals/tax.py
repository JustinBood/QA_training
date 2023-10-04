def getIncomeTax(salary):
    if int(salary) <= 11850:
         return f"your salary after tax is {salary}"
    elif int(salary) <= 34500:
        salary -= 11850
        salary =  salary - (salary * 0.8) 
        return f"your tax is {salary}"
    elif int(salary) <= 150000:
        salary -= 11850
        salary =  salary - (salary * 0.6) 
        return f"your tax is {salary}"
    elif int(salary) > 150000:
        salary -= 11850
        salary =  salary - (salary * 0.55) 
        return f"your tax is {salary}"


print(getIncomeTax(34500))
print(getIncomeTax(150000))
print(getIncomeTax(200000))


price = 0
children3 = 0
children12 = 10
students = 15
adults64 = 20
seniors65 = 12




age = int(input("how old are you"))

if age < 3:
    price = children3
    
elif age<=12:
    price = children12

elif age<=64:   
    if input("are you a student y/n")== "y":
        price = students
    else:
            price = adults64
            
elif age>=65:
    price = seniors65

print(price)


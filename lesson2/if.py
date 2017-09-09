age = int(input("PLease input your age: ")) #task 1 age

if age > 22:
    print("Work")
elif age > 17:
    print("University")
elif age > 6:
    print("School")
else: 
    print("Kindergarten")


#task 2 strings comparison 

userinput = str(input("Введите любое слово: ")) 
userinput1 = str(input("Введите другое слово, лучше \"learn\": "))

def somefunction (arg,arg1):
    if len(arg) == len(arg1): 
        return 1 
    elif userinput1=="learn": 
        return 3 
    elif len(arg) > len(arg1): 
        return 2
    else:  
        return "ХЗ что тогда возвращать, в задании не сказано"

print(somefunction (userinput,userinput1))
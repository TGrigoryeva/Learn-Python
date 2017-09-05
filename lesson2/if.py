age = int(input("PLease input your age: ")) #task 1 age

if age > 22:
    print("Work")
elif age > 17:
    print("University")
elif age > 6:
    print("School")
else: 
    print("Kindergarten")


def somefunction (somenumber): #task 2 strings comparison
    return somenumber

userinput = str(input("Введите любое слово: "))
userinput1 = str(input("Введите другое слово, лучше \"learn\": "))

if len(userinput) == len(userinput1):
    print(somefunction(1))
elif userinput1=="learn":
    print(somefunction(3))
elif len(userinput) > len(userinput1):
    print(somefunction(2))
else: 
    print(somefunction("ХЗ что тогда возвращать, в задании не сказано"))

number = int(input("number:"))
number2 = int(input("number2:"))
age = int(input("age:"))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("Zero")
if int(number2) % 2 == 0:
    print("even")
else:
    print("odd")
if age > 18:
    print("adult")
elif age < 18:
    print('child')

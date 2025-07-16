i = 0
# while i <= 50:
# for i in range(1, 51):
while True:
    if i % 3 == 0 and i % 5 ==0:
        print("fizz and buzz")
    elif i % 5 == 0 :
        print("buzz")
    elif i % 3 == 0 :
        print("fizz")
    else:
        print(i)

    i += 1
    

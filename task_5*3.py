n = int(input("the number is:"))

for i in range(n):
    space = abs(n//2 - i)
    star = n - space * 2
    print(space * " " + star * "*" + space * " ")

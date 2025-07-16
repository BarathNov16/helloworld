k = int(input("k:"))
numb = []
for i in range(k):
    num = int(input(f"enter number {i+1}:"))
    numb.append(num)
print("you entered:", numb)
sorted_list = sorted(numb)
print("The maximium value is:",sorted_list[-1])

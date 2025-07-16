k = int(input("k:"))
alph = []
# for i in range(k):
#     string = input(f"enter letter {i+1}:")
#     alph.append(string)

alph = str(input(f"enter letter :"))
print("you entered:", alph)
vowels = 'aeiou'
filter = [ch for ch in alph if ch in vowels]
sorted_1 = sorted(filter)
count = len(sorted_1)
print("vowels are:", sorted_1)
print("total numbern of vowles are:",count)

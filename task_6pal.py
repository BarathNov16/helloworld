def check_palindrome(word):
    pal_word = word[::-1]
    return word == pal_word

word =input("enter the word:")

if check_palindrome(word):
    print("palidrome")
else: 
    print("not palidrome")
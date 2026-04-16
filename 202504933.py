word = input("Enter a word: ")

letters = list(word)
print("Array form:", letters)

reversed_letters = letters[::-1]
print("Reversed array:", reversed_letters)

if letters == reversed_letters:
    print("The word is a palindrome")
else:
    print("The word is NOT a palindrome")
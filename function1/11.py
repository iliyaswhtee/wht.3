def is_palindrome(word):
    word = word.replace(" ", "").lower()

    if word == word[::-1]:
        return True
    else:
        return False
word = str(input("Enter your word: "))
if is_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")

#its working!!!!!!!!!!!
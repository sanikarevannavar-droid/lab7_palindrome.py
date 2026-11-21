import sys

def check_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

if len(sys.argv) > 1:
    string = sys.argv[1]
else:
    string = "madam"

print("String:", string)

if check_palindrome(string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

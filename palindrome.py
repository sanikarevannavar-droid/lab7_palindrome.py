
def check_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

string = input("Enter a string: ")

if check_palindrome(string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

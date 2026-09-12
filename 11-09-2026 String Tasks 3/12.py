# Take a string from the user and check whether it is a palindrome. 

text = input("Enter a String:")

rev_text = text[::-1]

print("Is Palindrome:", text.lower() == rev_text.lower())
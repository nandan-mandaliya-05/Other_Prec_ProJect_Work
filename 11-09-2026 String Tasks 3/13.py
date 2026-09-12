# Take a number from the user and check whether it is a palindrome. 

text = input("Enter a String:")

rev_text = text[::-1]

print("Is Palindrome Number:", text.lower() == rev_text.lower())
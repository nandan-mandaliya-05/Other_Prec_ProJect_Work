# Remove extra spaces, remove non-alphabetic characters, find length, reverse the string, and check whether it is a palindrome. 

text = "       Python245@123       "

# remove extra spaces

# remove_middle_spaces = text.replace(" ","")
# print(remove_middle_spaces)
remove_spaces = text.strip()
print("Strip text:",remove_spaces)

# remove non-alphabetic characters
alpha_string = ""
for i in remove_spaces:
    if i.isalpha():
        alpha_string += i
print("Alphabet String:",alpha_string)

# find length
print("Length of Remove spaces Text:",len(text.strip()))

# reverse the string
rev_text = remove_spaces[::-1]

print(rev_text)

# check a Palindrome
text = input("Enter a word or sentence what are you want:")

rev_text = text[::-1]

print("Is Palindrome:",text.lower()==rev_text.lower())

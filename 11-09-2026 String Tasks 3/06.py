# Remove numbers and special characters from a string. 

text = "Python@78666"

new_text = ""

for i in text:
    if i.isalpha():
        new_text += i
        
print(new_text)
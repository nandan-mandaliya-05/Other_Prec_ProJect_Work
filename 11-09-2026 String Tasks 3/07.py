# Extract only numeric characters from a string. 

text = "Python@78666"

new_text = ""

for i in text:
    if i.isdigit():
        new_text += i
    
print(new_text)    

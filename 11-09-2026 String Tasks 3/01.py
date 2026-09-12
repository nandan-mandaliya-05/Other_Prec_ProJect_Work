# Join a list of city names using " - "

text = "Ahmdabad Rajkotn Pune Banglore"

# Method 1
text_split = text.split()
print(text_split)

text_split_join = " - ".join(text_split)
print(text_split_join)

# Method 2
text_join = " - ".join(text.split())
print(text_join)



# Reverse a string by converting it into a list and using .reverse(). 

text = "Python is awasome"

text_list = list(text)
text_list.reverse()

print(text_list)

text_list_join = "".join(text_list)

print(text_list_join)


# for each word
# text_split = text.split()

# rev_list = []

# for i in text_split:
#     rev_list.append(i[::-1])
    
# result = " ".join(rev_list)
# print(result)
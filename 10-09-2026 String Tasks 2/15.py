# Combined Task: Create a sentence about a shopping order containing product name, quantity, price, and customer name. Use % formatting, upper(), lower(), find(), replace(), count(), and split() on the data.

customer_name = "Rohit Sharama"
quantity = 3
product_name = "wireless headphones"
price = 12500

print("%s placed a shopping order for %d %s, totaling ₹%d." % (customer_name,quantity,product_name,price))

sentence = "%s %s placed a shopping order for %d %s, totaling ₹%d." % (customer_name,customer_name,quantity,product_name,price)
print(sentence.upper())
print(sentence.lower())
print(sentence.find("Sharama"))
print(sentence.replace("Rohit Sharama","Virat Kohli"))
print(sentence.count("Rohit Sharama"))
print(sentence.split(" "))
print(sentence.split())





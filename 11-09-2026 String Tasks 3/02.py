# Join a list of programming languages using " | "

city = "Python C++ Java R Javascript"

# Method 1
city_split = city.split()
print(city_split)

city_split_join = " | ".join(city_split)
print(city_split_join)

# Method 2
city_join = " | ".join(city.split())
print(city_join)
# For Loop: Create a multiline string containing five animal names, split it using split("\n"), and print each animal using a for loop.

animal_name = """Tiger
Elephant
Penguin
Dolphin
Kangaroo"""

animal_name_list = animal_name.split("\n")
for i in animal_name_list:
    print(i)

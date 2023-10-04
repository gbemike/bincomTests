import os

with open("name.txt", "r") as file:
    name = file.read()
    surname = name.split(" ")[0]
    middle_name = name.split(" ")[1]
    first_name = name.split(" ")[2]
    print(f"Surname: {surname}\nMiddle Name: {middle_name}\nFirst Name: {first_name}\n")
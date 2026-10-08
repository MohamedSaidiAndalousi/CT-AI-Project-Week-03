email = input("Enter an existing Howest email address: ")

name = email.split("@")[0]
parts = name.split(".")

first_name = parts[0].capitalize()
last_name = " ".join(parts[1:]).title()

print(f"The last name is {last_name} and the first name is {first_name}")
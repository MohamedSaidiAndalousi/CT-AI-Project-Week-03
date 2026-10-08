def generate_password(last_name, first_name, date_of_birth):
    last_name = last_name.replace(" ", "").lower()
    first_name = first_name.replace(" ", "").upper()

    month_year = date_of_birth[3:5] + date_of_birth[6:10]

    password = last_name[:3] + first_name[:2] + month_year

    return password


last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
date_of_birth = input("Enter your date of birth (dd-mm-yyyy): ")

print(generate_password(last_name, first_name, date_of_birth))
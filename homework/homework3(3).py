def check_email_address(email):
    parts = email.split("@")

    if len(parts) != 2:
        return False

    name = parts[0]
    domain = parts[1]

    if domain != "student.howest.be":
        return False

    name_parts = name.split(".")

    if len(name_parts) != 2:
        return False

    if name_parts[0] == "" or name_parts[1] == "":
        return False

    return True


print(check_email_address("jan.janssens@student.howest.be"))
print(check_email_address("jan.janssens@howest.be"))
print(check_email_address("janjanssens@student.howest.be"))
print(check_email_address("jan..janssens@student.howest.be"))
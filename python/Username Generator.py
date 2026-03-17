first_name = "Harshit"
last_name = "Sharma"
birth_year = 2003

# Username
username = first_name.lower() + "_" + last_name.lower() + "_" + str(birth_year)[-2:]

# Email
email = first_name.lower() + "." + last_name.lower() + "@gmail.com"

# Password hint (first letter of each name + year + !)
password_hint = first_name[0].upper() + last_name[0].upper() + str(birth_year) + "!"

# Print results
print("Username:", username)
print("Email:", email)
print("Password Hint:", password_hint)
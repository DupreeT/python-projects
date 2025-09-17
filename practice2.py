# Hard-coded correct password
correct_password = "password"

# Allow up to 3 attempts
attempts = 3

while attempts > 0: #run while attempts remain
    password = input("enter password: ")

    if password == correct_password:
        print("Access granted")
        break
    else:
        attempts = attempts - 1
        print(f"incorrect password. Attempts left: {attempts}")
        if attempts == 0:
            print("Account locked.")




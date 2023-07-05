import random

x = "QWERTYUIOPASDFGHJKLZXCVBNM"
y = "qwertyuiopasdfghjklzxcvbnm"
z = "123456789@£_&$§∆✓%?!"

password_letters = x+y+z

choice = input("Need a password?: ")

hll = '\033[1;0m'
hl1 = '\033[1;43m'
hl2 = '\033[1;44m'
hl3 = '\033[1;41m'
hl4 = '\033[1;42m'

hl_col = [hl1, hl2, hl3]
hl_colour = random.choice(hl_col)


if choice == "yes" or choice == "yea" or choice == "yws" or choice == "ya" or choice == "ye" or choice == "yup" or choice == "yawh" or choice == "y":
    password = "".join(random.choices(password_letters, k  = random.randint(7, 24)))
    password_high = hl_colour  + password + hll
    print(f"{password_high} is the generated password, keep it safe buddy")
    print("")
    print(password_high)
else:
    print("Cancelled.")

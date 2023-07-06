
import random

x = "QWERTYUIOPASDFGHJKLZXCVBNM"
y = "qwertyuiopasdfghjklzxcvbnm"
z = "123456789@£_&$§∆✓%?!"

password_letters = x + y + z + x + z + y
words_yes = ["yes", "ya", "yup", "yip", "y", "yah", "yws", "ye", "yas", "yass", "yee", "yeo", "yah", "sure", "ok", "okay", "sur", "surw"]

choice = input("Need a pass?: ")

#hl stands for highlight
hll = '\033[1;0m'
hl1 = '\033[1;43m'
hl2 = '\033[1;44m'
hl3 = '\033[1;41m'
hl4 = '\033[1;42m'

hl_col = [hl1, hl2, hl3, hl4]
hl_colour = random.choice(hl_col)

def gen_pass():
     global choice
     if choice in words_yes:
         password = "".join(random.choices(password_letters, k  = random.randint(9, 19)))
         global hl_colour
         password_high = hl_colour + password + hll
         print(f"{password_high} is the generated password, keep it safe buddy")
         print("")
         print(password_high)
         again = input("Another?: ")
         if again in words_yes:
             hl_colour = random.choice(hl_col)
             gen_pass()
         else:
             print("Cancelled.")
     else:
         print("Cancelled.")
         
gen_pass()

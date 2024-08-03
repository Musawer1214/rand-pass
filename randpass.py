import random
import string

passw_lenth = 12

charval = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(passw_lenth):
    password += random.choice(charval)




print(password)
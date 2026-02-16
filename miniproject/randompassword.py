import random
import string

pass_len=10
charval=string.ascii_letters+string.digits+string.punctuation

password = ""
for i in range(pass_len):
    password+=random.choice(charval)
print("Your password is :",password)
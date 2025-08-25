import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

print("This is from Hao")

password = "".join(random.sample(total, length))

print(password)

# 456 from hao
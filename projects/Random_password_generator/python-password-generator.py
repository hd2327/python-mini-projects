import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

print("This is a feather form Dong")

password = "".join(random.sample(total, length))

print(password)

# 456 from hao


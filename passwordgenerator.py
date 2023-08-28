import random

uppercase_chars = ("QWERTYUIOPASDFGHJKLZXCVBNM")
lowercase_chars = ("qwertyuiopasdfghjklzxcvbnm")
special_chars =("!@#$%^&*()")
num_chars = ("123456789")

all = uppercase_chars + lowercase_chars + special_chars + num_chars

length = int(input("How many characters would you like your password to be?: "))

password = "".join(random.sample(all,length))
print(f"Your Password is : {password}")


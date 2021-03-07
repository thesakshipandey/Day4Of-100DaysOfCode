import random

name = input("ENTER THE NAMES")
list_li = name.split()
length = len(list_li)
choice = random.randint(0,length-1)
Pay_name = list_li[choice]
print(f"{Pay_name} is gonna pay the bill!!")

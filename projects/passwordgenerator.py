import string
import random
res1= []
res2= []
res3= []
letters= list(string.ascii_lowercase + string.ascii_uppercase)
numbers= list(range(0,10))
symbols=['@', '#', '$', '%', '*', '&', '!']
let=int(input(f"How many letters would you like in your password\n"))
num=int(input(f"How many numbers do you want in your password\n"))
sym=int(input(f"How many symbols do you want in your password\n"))

for i in range(0,let):
    x=random.randint(0,len(letters)-1)
    res1.append(letters[x])

for i in range(0,num):
    x=random.randint(0,len(numbers)-1)
    res2.append(numbers[x])


for i in range(0,sym):
    x=random.randint(0,len(symbols)-1)
    res3.append(symbols[x])


finalpassword= res1 + res2 + res3
random.shuffle(finalpassword)

final=(str(finalpassword))
print(*finalpassword)
















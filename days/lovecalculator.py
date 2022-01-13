n1= input("Enter your name ")
n2=input("Enter your name ")
name1=n1.lower()
name2=n2.lower()
str1= "true"
str2="love"
c=0
d=0
for i in range(0,len(str1)):
   c+= name1.count(str1[i]) + name2.count(str1[i])
for i in range (0,len(str2)):
   d+= name1.count(str2[i]) +name2.count(str2[i])

#print(f"{c}{d}")

res1= c*10 + d
print((res1))

if res1>90 or res1<10:
    print(f"{name1}, {name2} go together like coke and mint ")
elif res1>40 or res1<50:
    print(f"{name1}, {name2} look good together ")
else:
    print(f"Your score is {res1}")
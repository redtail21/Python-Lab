import random
import datetime
name = input("What is your name: ")
l = 8
for i in range(1):
    password=""
    passwdlst = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%?"
    i=1
    while i<=l:
        password = password + random.choice(passwdlst)
        i = i+1
c=(password)
x = datetime.datetime.now()
print(f"({c}) this password is created on ({x}) by {name} ")
fl=open('output3.txt','a')
fl.write(f"({c}) this password is created on ({x}) by {name} \n")
fl.close()
sum = 1
i = 1
n = int(input("enter a value to find factorial: "))
while i<=n:
    sum=sum*i
    i=i+1
print(f"factorial of {n} is {sum}")

fl=open('output6.txt','a')
fl.write(f"factorial of {n} is {sum}")
fl.close()
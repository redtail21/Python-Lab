fl=open('output10.txt','a')
# binary to decimal
a = input("Enter the binary number : ")
from_base = 2
answer = int(a,from_base)
print(answer)
fl.write(f"{a} Binary to Decimal is {answer}\n")
# decimal to binary
a = int(input("enter the decimal number : "))
answer = bin(a)
answer=answer[2:]
print(answer)
fl.write(f"{a} Decimal to Binary is {answer}\n")
fl.close()
a = input("Enter a Number or String to check palindrome : ")
b = a[::-1]
if(a==b):
    c=(f"{a} is palindrome ")
    print(c)
else:
    c=(f"{a} is not palindrome ")
    print(c)

fl=open('output7.txt','a')
fl.write(c+'\n')
fl.close()
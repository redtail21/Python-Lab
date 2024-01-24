num=int(input("Enter a Number to find multiplication table: "))
fl=open('output9.txt','a')
fl.write(f"multiplication table of {num}\n")
for i in range(1,11):
    print(num, 'x', i, '=', num*i)
    j=num*i
    fl.write(f"{str(num)} X {str(i)} = {str(j)} \n")
fl.close()
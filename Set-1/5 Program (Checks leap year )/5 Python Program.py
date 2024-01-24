
year = int(input("Enter a year to check if it's a leap year: "))
leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
if leap_year:
    c=(f"{year} is a leap year.")
    print(c)
else:
    c=(f"{year} is not a leap year.")
    print(c)
fl=open('output5.txt','a')
fl.write(str(c)+'\n')
fl.close()
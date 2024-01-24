# F = (9/5)C + 32  celsius to fahrenheit
c=float(input("enter celsius value : "))
f=(c*(9/5)+32)
f=round(f,2)
print(f"{str(c)} celsius = {str(f)} fahrenheit\n")

# °C = (°F - 32) × 5/9  fahrenheit to celsius
f1=int(input("enter fahrenheit value : "))
c1=((f1-32)*5/9)

c1=round(c1,2)
print(f"{str(f1)} fahrenheit = {str(c1)} celsius\n")

fl = open("output1.txt",'a')
fl.write(f"{str(c)} celsius = {str(f)} fahrenheit\n")
fl.write(f"{str(f1)} fahrenheit = {str(c1)} celsius\n")
fl.close()

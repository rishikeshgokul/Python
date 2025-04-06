
t=float(input("temperature: "))
unit=input("choose unit('k' OR 'f' OR 'c'): ")


if unit=="c":
    print("Temperature in Fahrenheit=",t*(9/5)+32,"F",sep=(""))
    print("Temperature in Kelvin=",t+273.15,"K",sep=(""))

elif unit=="F":
    print("Temperature in Celsius=",t-32*5/9,"C",sep=(""))
    print("Temperature in Kelvin=",t-32*(5/9)+273.15,"K",sep=(""))

elif unit=="k":
    print("Temperature in Celsius=",t-273.25,"C",sep=(""))
    print("Temperature in fahrenheit=",t-273.15*(9/5)+32,"F",sep=("")) 

else:
    print("ERROR")

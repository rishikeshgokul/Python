"""
a=input("give your word: ")

b=a.lower()

p=b.count("a")
e=b.count("e")
y=b.count("i")
x=b.count("o")
z=b.count("u")

print(f"number of vowels are: {p+e+y+x+z}")
"""

"""m=int(input("enter the mathematics marks: "))
s=int(input("enter the science marks: "))
e=int(input("enter the the english marks: "))

x=m+s+e
y=(m+s+e)/3
print(f"total marks:{x}")
print(f"average marks:{y}")

if y>=90:
    print("Grade: A")

elif y==50<80:
    print("Grade: B")

else:
    print("pass")
"""




"""#palindrome checker

a=input("enter your word: ")
b=a[::-1]

if a==b:
   print("It is a Palindrome!")

else:
   print("It is not a Palindrome")"""

'''
a=input("give three numbers:")

x,y,z=a.split(",")

q=int(x)
w=int(y)
e=int(z)

if q>w and q>e:
    print(f"the largest number is: {x}")

elif w>q and w>e:
    print(f"the largest number is: {y}")

elif e>q and e>w:
    print(f"the largest number is: {z}")

else:
    
    print("all are equal")

'''
"""#leap year checker

year=int(input("enter the year: "))
 

if year%100==0 and year%400!=0:
    print("not a leap year")

elif year%4==0:
    print("it is a leap year")

"""

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

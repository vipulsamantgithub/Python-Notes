"""
a=float(input("enter 1st no.= "))
b=float(input("enter 2nd no.= "))
c=a+b
print(c)

"""

"""

a=float(input("enter dividend no.= "))
b=float(input("enter divisor no.= "))
print("remainder is = ",a%b)

"""

"""

a="Vipul"
c="Hi "+a
print(c)
print(a[:9])

"""

"""

a=str(input("Enter the user name: "))
b="Hi "+a+ " Good afternoon."
print(b)

"""

"""

name=str(input("enter the name: "))
date=input("enter the date: ")
print(f"Dear {name} \n you are selected \n {date}")

"""

#               OR

"""

a="Dear <Name> \n You are selected \n <Date> "
name=str(input("enter the name: "))
date=input("enter the date: ")
a=a.replace("<Name>",name)
a=a.replace("<Date>",date)
print(a)
"""

a="vipul  samant is from  Uk"

b=count(a("  "))
print(b)
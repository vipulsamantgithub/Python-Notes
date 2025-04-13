# A function is a group of statement performing a specific task
# When a program gets bigger in size and its complexity grows, it gets difficult for a programer to track which piece of code is doing what.
# A function can be used by a programmer in a program any number of times.

# Program to greet a user a with "GOOD DAY" using functions.
"""
name=input("Enter the name: ")
def fun():      # function definition - where we define set of instruction what function will do.
    print(f"GOOD DAY {name}")
fun()   #function call -- for running the set of instruction inside the function definition.
"""

# The functions are of 2 types:
# 1.  Built in function(Already present in the python -- Ex- len(),print(),range() etc.)
# 2.  User defined function(defined by the user--- Ex THe above program fun() was user defined) 

# Function with arguments
# A function can accept some value that it can work with. We can put these value in the parenthesis.

"""
def fun(name, ending):   # function with 2 arguments- name and ending
    print(f"Hi {name}")
    print(ending)
fun("Vipul", "Thanks")  # returning value to the arguments made during function definition
fun("Ram", "Bye")
"""

# A function can also return value like below in the program:

"""
def fun(name):
    print(f"Hi {name}")

a=fun("vipul")   # you can also call function this way
print(a)  # here a doesn't store any value because you have not used any return inside the fun(name)."""

# Lets check how to return some value that a will store in below program
"""
def fun(name):
    print(f"Hi {name}")
    return "printed"
a=fun("vipul")   
print(a) 
"""

# Default argument

"""def fun(name='Ram'):    # here we have given default value i.e Ram to name
    print(f"Hi {name}")
   
fun("vipul")   # Vipul will be printed 
fun()        # As this has no argument so will take default value and will print - Ram
"""

# Recursion -- It is a function that calls itself.
# It is used to directly use the a mathematical formula as function.


# logic of factorial
"""
fact(1)=1
fact(2)=1*2
fact(3)=1*2*3
fact(4)=1*2*3*4
fact(5)=1*2*3*4*5

fact(n)=n*n-1.......3*2*1
fact(n)=n*fact(n-1)
Example- find the fact(3)
    # So here recusion can be used 
    Fact(3)=3*fact(2)
           =3*2*fact(1)
           =3*2*1      # In this way recursion will for work for finding the fact(3) function will call itself again and again.

"""
# finding factorial using the recursion
"""
def fact(n):
    if (n==1 or n==0):
        return 1
    return n*fact(n-1)   
n=int(input("enter the number: "))
print(f"The factorial of a number is: {fact(n)}")
"""

# factorial without recursion and using for loop and if else.


n=int(input("enter the number: "))
fact=1
if(n==1 or n==0):
    fact=1
else:
    for i in range(1,n+1):
        fact=fact*i
print(fact)

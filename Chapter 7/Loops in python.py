# While loop -- In while loop the condition is checked first if it evaluates to be true the body of the loop is executed otherwise not.
# If the loop is entered, the process of [condition check & execution] is continued until the condition becomes False.

# Write a program to print 1 to 50 using while loop and for loop
# Through while loop
"""
i=1
while(i<=50):
    print(i)
    i+=1
"""
# Through for loop
"""
for i in range(1,51):
    print(i)
"""

# list using while loop
"""
l=["vipul","ram","Rahul","sam"]
i=0
while(i<len(l)):
    print(l[i])
    i+=1
"""

# list using for loop
"""
l=["vipul","ram","Rahul","sam"]
for i in l:
    print(i)
"""

# tuple using for loop
"""
l=("vipul","ram","Rahul","sam")
for i in l:
    print(i)
"""

# steps in for loop
"""
for i in range(1,100,4):
    print(i)
"""

# for loop with else - when the loops end then the else part is executed
"""
a=[1,2,3,4,5,6]
for i in a:
    print(i)

else:
    print("The execution is completed")
"""

# Break statement -- exit the loop right now
"""
for i in range(1,50):
     if(i==20):   # if break is used before print(i) it will print upto 19 and then condtion is check and it exits out of loop.
        break
    print(i)    # if break is used after print(i) it will print upto 20 and then condtion is check and it exits out of loop.
""" 
# continue statement -- skip that particular iteration and continue
"""
for i in range(1,50):
    if(i==20):   # if continue is used before print(i) it will print upto 19 and then condtion is checked and it skips 20 and then continues to print from 21.
        continue
    print(i) # if continue is used after print(i) it will print upto 20 and then condtion is checked but as 20 is already printed so cant skip 20 now, so will print 1-50 normally.

"""

# pass statement - It instructs to do nothing. Used when you want to work on other things and want to leave the current thing as it is then use pass.
"""
l=[1,2,3]
for i in l:
    pass   # writing while loop so using pass inside for loop
i=0
while(i<len(l)):
    print(l[i]**2)  #printing squares of list
    i+=1
"""
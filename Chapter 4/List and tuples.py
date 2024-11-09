# List are containers to store a values of any data type.

"""
a=["vipul",12,"samant",24]
print(a[2])
a[1]=11
print(a)
"""
# List methods

"""
# sort - in below program it sorts the original list that's why list are called mutabble. But sort returns none.
b=[1,31,22,2,0,5]
b.sort()
print(b)

# Here in below program you can see, it returns none because sort changes the original list.
b=[1,31,22,2,0,5]
c=b.sort()
print(c)

# But if you want to store it into new list then use "sorted()"
b=[1,31,22,2,0,5]
c=sorted(b)  #this will create new list 'c' with sorted elements of 'b'
print(c)
"""

# reverse function

"""
a=[1,3,4,5,6,10]
a.reverse()  # reverse the list
print(a)

a.append(31)  #insert the value at the end
print(a)

a.insert(2,45) # inserts the value at particular index
print(a)


a.pop(3)
print(a)  # delete the element at index 3 and returns it, unlike the sort() it return the deleted element

print(a.pop(3))  # will delete the element at index 3 and prints/return its value.

a.remove(1)  # deletes the particular element, here it will remove 1 from the list. Also it returns none.
print(a)

print(a.remove(31))  # returns none because the changes are made in original list.
print(a)
"""

# Tuple is immutable data type in python

"""
a=(1,2,3)
print(type(a))

b=(1)       # here it consider it as a single number inserted inside the bracket so will give "int " type
print(type(b))  

c=(1,)  # so to give single value inside the tuple use comma after giving value
print(type(c))
"""
# tuple methods

"""
a=(1,2,32,5,0,3,2)
print(a.count(2))  # gives how many times 2 is present in the tuple and also it returns value because tuples are immutable.
print(a) # no change in original tuple

print(a.count(23)) # returns  0 because there is no value 23 present in the tuple.
"""

# Can you sort tuple? 
"""
Original tuple cannot be sorted but you can use sorted() to sort the tuple and store it 
"""

"""
a=(1,4,2,0,2,5)
b=sorted(a)
print(b)  # will sort the tuple and give list as output, but the original tuple has not been changed new sorted tuple is stored in 'b' as a list.
print(a)

# to store new sorted tuple as tuple only see below
c=tuple(sorted(a))
print(c)
"""


# Other methods of tuples
# Concatenation: Combining two tuples using +
# Repetition: Repeating a tuple multiple times using *
# Membership: Checking if an element exists in a tuple using in or not in

t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
concatenated_tuple = t1 + t2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5)

# Repetition
repeated_tuple = t1 * 2
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)  # Output: True
print(6 not in t1)  # Output: True

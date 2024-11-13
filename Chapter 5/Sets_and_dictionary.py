# Dictionary is a collection of key value pairs
# It is unordered
# It is mutable
# It is indexed
# It cannot have duplicate keys
"""
a={"key":"value",
   "Vipul":"Samant",
   "c":(1,2,3),
   "b":[2,3,4],
   0:"vs"   # cannot use character without "" 
   }
print(a["b"])
"""

# Dictionary methods

"""
print(a.items())
print(a.keys())
print(a.values())
a.update({1:"ssss","VS":"asdsadsa"})
print(a)

# get method in dictionary
print(a.get("Vs1"))  # if the key is not present prints/returns none
print(a["svs"])  # gives error if the key is not present
"""

"""
d = {"a": 1, "b": 2}
value = d.pop("a","key not present")  #removes the key value pair and if not present gives the default value -- here it is -- "key not present"
print(value)  # Output: 1
print(d)  # Output: {'b': 2}

"""

# Sets is a collection of non repetitive elements.


"""
s={1,2,3}   # This is a set with some elements
s={}        # This is empty dictionary
a=set()     # This is empty set
a.add(1)
a.add(2)
a.add(2)    # set stores unique values so, 2 will be only shown 1 time when print is used.
a.add("Vipul")
print(a)
"""


# Sets are unordered
# Sets are unindexed
# There is no way to change item in the sets
# Sets cannot contain duplicate values


# Set methods/operations
"""
# remove function --- Removes the selected element from the set
a= {1,2,3,4,5}
a.remove(2)
print(a)

# Pop --- removes random element from the set
b={2,3,1,4,5}
b.pop()
print(b)

# clear -- clear the whole set and the result is empty set
b.clear()
print(b)

# Union

c={1,2,3}
d={3,4,5}
print(c.union(d))   # Combines the elements of both the set but removes the duplicates.

# Intersection
print(c.intersection(d))
"""
# Difference method
"""
s1={1,2,3,4}
s2={3,4,5,6,7}
print(s1.difference(s2))  # prints elements of s1 that are not present in s2
print(s2.difference(s1))  # prints elements of s2 that are not present in s1

print(s1-s2)  # above thing can be written as this way too
print(s2-s1)
"""
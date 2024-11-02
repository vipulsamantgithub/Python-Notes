# Len --- used to print the length of the string

a="VIPUL"
print(len(a))
b= "samant"
print(a.endswith("UL"))
print(a.startswith("VI"))   # checks whether word start with particular character and is case sensitive
print(b.capitalize())   # 1st letter of the word gets capitalize

c= " Vipul Samant is from UK"
print(c.find("is")) #finds the index of word --- 14th index , if index not found returns -1
print(c.find("i")) #finds the index of word  --- 2nd index 
print(c.title())  # capitalize every 1st letter of the word.

d= "vipul is good good boy"
print(d.replace("good","bad")) # replace all the occurence of the word with given word



# Escape sequence characters ---- 
# \n - for newline
# \t - for leaving space for tab
# \"  \" - If you want to insert inverted comma in sentence then use \" \" like below
e= "Vipul \" Samant \""
print(e)

# \\ - if you want to enter \ in a string near other sensitive characters like below

f= "Vipul \ Samant \\"  
print(f)


# F strings 

name = input("enter the name: ")

print(f"Hi {name}, how are you?")

# both above and below line will give the same results

print("Hi "+name+ ", how are you? ")
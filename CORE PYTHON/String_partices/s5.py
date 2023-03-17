#  Create a new string made of the first, middle, and last characters of each input string

str1 = str(input("Enter the First String"))
str2 = str(input("Enter the Second String"))

l = len(str1)
l1 = len(str2)
f1 = str1[0]
f2 = str2[0]
a = f1 + f2
print( "First String :",a)


# Middle String

mi = int(l /2)
mi1 = int(l1 / 2)

a = a + str1[mi] + str2[mi1]


print("Middle String :",a)

# last string

a =a + str1[l-1] + str2[l1-1]

print("Last String :",a)




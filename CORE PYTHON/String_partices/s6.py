# Arrange string characters such that lowercase letters should come first
str1 = str(input("Enter the String"))

l = []
u = []
for i in str1:
    if i.islower():
        l.append(i)
    else:
        u.append(i)
store = ''.join(l + u)
print(store)
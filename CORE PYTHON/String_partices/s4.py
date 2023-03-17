# Create a string made of the middle three

str = "JhonDipPeta"
print("Orginal String is :", str)

# middle three string
l = len(str)
# for i in range(l):
mi = int(l / 2)

res = str[mi-1:mi+2]
print(res)

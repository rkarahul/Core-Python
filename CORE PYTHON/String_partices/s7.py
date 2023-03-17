# Count all letters, digits, and special symbols from a given string
str1 = str(input("Enter The Charcter"))
letters = 0
digits = 0
symbols = 0

for char in str1:
    if char.isalpha():
        letters = letters + 1

    elif char.isdigit():
        digits = digits + 1

    else:
        symbols = symbols +1

store_str1 = letters 
store_str2 = digits 
store_str3 = symbols

print("Count all Letters :",store_str1)
print("Count all Digits :",store_str2)
print("Count all Symbols :", store_str3)

amt= 0
unit = int(input("Enter the Unit"))
if(unit<100):
    amt = 0
if(unit>100) and (unit<=200):
    amt = (unit-100)*5
if(unit>200):
    amt = 500+(unit-200)*10
print("total electricity bill :",amt)


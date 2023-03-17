# write a  program to accept the cost price of a bike and display the road tax to be paid according to the following criteria:
tax = 0
cost_Price = int(input("Enter the cost price(in Rs):"))
if (cost_Price > 100000):
    tax = (15/100)*cost_Price
elif(cost_Price > 50000 and cost_Price<=100000):
    tax = (10/100)*cost_Price
else:
    tax = (5/100)*cost_Price
print("The Road tax is :",tax)


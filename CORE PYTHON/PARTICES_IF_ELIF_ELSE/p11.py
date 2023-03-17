# A number  from 1 to 7 and display the name of the day like 1 for Sunday and so on 
num = int(input("Enter any number between 1 to 7 "))
if (num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7 ):
    if(num ==1):
        print(num,"for Sunday")
    if (num == 2):
        print(num, "for Monday")

    if(num ==3):
        print(num,"for Tuesday")
    
    if(num ==4):
        print(num,"for Wednesday")

    if(num ==5):
        print(num,"for Thuesday")

    if(num ==6):
        print(num,"for Friday")
    
    if(num ==7):
        print(num,"for Satuday")
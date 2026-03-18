print(">>>>Enter Card Details in the format 'XXXX XXXX XXXX XXXX'<<<<")
Card_Details=(input("Enter Your Card Number:"))
lastdigits=Card_Details[15:]
DisplayNumber='XXXX XXXX XXXX '+lastdigits   #we can also do DisplayNumber='X'*4 + ' ' 
print(DisplayNumber)
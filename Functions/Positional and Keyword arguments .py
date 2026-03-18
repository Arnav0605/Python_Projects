def volume(length,breadth,height):
    vol=length*breadth*height
    return vol

v=volume(10,20,30) #This is positional arguments where numbers are placed as given above in the function first length then breadth and then height
print("Volume is:",v)

a=volume(length=40,height=50,breadth=40) #This is keyword arguments everything is specified in the code
print("Volume is:",a)

def vol(l=1,b=1,h=1): #Default arguments if no value is given then these takes the values
    vol=l*b*h         #Default arguments can have any type of data
    return vol

A=vol()
print(A)
V=vol(l=5,b=10,h=20)
print(V)



def fun(a,b,/,c,d):       #The / specifies that before it only positional arguments can be used now
    print(a,b,c,d)         #If we use * instead of / then it works with keyword only arguments instead of positional arguments but in case of * it is after the * not before it

fun(5,10,15,20)
fun(5,10,c=20,d=50)
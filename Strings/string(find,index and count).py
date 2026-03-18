s1='Hello World How Are You'
x1=s1.find('W')
print(x1)
x2=s1.find('How')
print(x2)
x3=s1.find('o',6)
print(x3)
x4=s1.index('W') #rindex and rfind just starts from the reverse direction
print(x4) #Difference between index and find is if element is not present in the string then index shows error whereas find does not show any error
x5=s1.count('You')
print(x5)
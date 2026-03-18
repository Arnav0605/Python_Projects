L1=[5,6,10,11,15]
it=iter(L1)   #iter is an iterator
next(it)      #next moves the iterator to the next element but only when it is used
next(it)




def myrange(n):   #Generates the function in a loop and waits for us to call the function
    i=0
    while i<n:
        yield i   #this is used to return the values in place of return function
        i=i+1
        
a=myrange(5)
print(next(a))       
print(next(a))
print(next(a))
print(next(a))


#>>>>>> Mini Project on Generator function <<<<<<<<<<
def mirange():
    days= ["Sunday","Monday" ,"Tuesday","Wednesday","Thursday","Friday","Saturday"]
    i=0
    while True:
        yield days[i]
        i+=1
        if i==len(days):
            i=0

A=mirange()
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
print(next(A))
    
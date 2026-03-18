g=9.99  #Global Variable
print(g)


def fun():
    a=100  #Local Variable
    g=999
    print("Local Variable",a)
    print("Local Variable",g)
fun()


print("Global Variable",g)   #Global Variable Remains the same




G=100
print(G)




def function():
    global G     #global function is used
    A=500
    G=1000
    print("Local Variable",A)
    print("Global Variable",G)
   

function()

print("Global Variable",G)   #Global Variable changed due to the use of global variable function








# 🌍 Global variables
x = 10
y = 20
z = 30

print("Global variables:", globals())  # Shows all global variables as a dictionary

def show_scope():
    # Local variables
    a = 1
    b = 2
    c = 3
    print("Local variables:", locals())  # Shows all local variables as a dictionary

show_scope()

# Accessing specific global variables using globals()
print("Value of x from globals():", globals()['x'])
print("Value of y from globals():", globals()['y'])
print("Value of z from globals():", globals()['z'])

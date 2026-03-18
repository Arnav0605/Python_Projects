class Complex:
    def __init__(self,real,img):
        self.real=real 
        self.img=img

    def ShowNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):            #Dunder Functions are  __function__ like this
        NewReal=self.real+num2.real    #Using these we can use basic operators in our class
        NewImg=self.img+num2.img       #Example-__mul__ we can use the multiply operator
        return Complex(NewReal,NewImg)
    
    def __sub__(self,num2):
        NewReal=self.real-num2.real
        NewRealImg=self.img-num2.img
        return Complex(NewReal,NewRealImg)
    
num1=Complex(1,3)
num1.ShowNumber()
num2=Complex(9,4)
num2.ShowNumber()
num3= num1+num2
num3.ShowNumber()
print("This is Subtraction")
num4=num1-num2
num4.ShowNumber()

    


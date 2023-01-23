class Calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        return self.a/self.b
obj=Calculator(10,94)
while True:
    def menu():
        x=('1.Add\n2.Sub\n3.Multiply\n4.Divide')
        print(x)
    menu()
    choice=int(input('Please select onr of the following:'))
    if choice==1:
        print(obj.add())
    elif choice==2:
        print(obj.subtract())
    elif choice==3:
        print(obj.multiply())
    elif choice==4:
        print(obj.divide())
    elif choice==0:
        print('Try Again')
        break

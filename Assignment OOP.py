# challenge 1
# class Point:
#     def __init__(self,x,y,z):
#         self.x= x
#         self.y= y
#         self.z= z

#     def sqsum(self):
#         return(self.x*self.x+self.y*self.y+self.z*self.z)
# x=int(input('enter first num'))
# y=int(input('enter second num'))
# z=int(input('enter third num'))
# sqno=Point(x,y,z)
# print(sqno.sqsum())


# challenge 2
# class calculator():
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return self.num1+self.num2
#     def sub(self):
#         return self.num2-self.num1
#     def mult(self):
#         return self.num1*self.num2
#     def div(self):
#         return self.num2/self.num1
# num1=int(input('enter first no.='))
# num2=int(input('enter second no.='))
# obj=calculator(num1,num2)
# print(obj.add())
# print(obj.sub())
# print(obj.mult())
# print(obj.div())


# challenge 3
# class Student:
#     name=None
#     rollNumber=None

#     def setName (self,name):
#         self.name=name

#     def getName (self):
#         return self.name

#     def setRollNumber(self, rollNumber):
#         self.rollNumber=rollNumber
    
#     def getRollNumber(self):
#         return self.rollNumber

#     syntax1=Student()
#     syntax1.setName('anshul')
#     syntax1.setRollNumber(45)
#     print(syntax1.getRollNumber())


#challenge 4
class account:
    def __init__(self,title):
        self.title= title
        self.balance= balance

class savings_account (account):
    def __init__(self,title,balance,interest_rate):
        super().__init__(title,balance)
        self.interest_rate= interest_rate

account_obj = account('anshul',5000)
savings_account_obj=savings_account('anshul',5000,5)
print(savings_account_obj.title)
print(savings_account_obj.balance)
print(savings_account_obj.interest_rate)
        


        


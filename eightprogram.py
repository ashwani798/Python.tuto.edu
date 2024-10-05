# OOPS

# class Student:
#     name = "Ashwani"
# # creating object (instance)

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "blue"
#     model = "ola s1"
#     brand = "jaguar"

# car1 = Car()
# print(car1.color)
# print(car1.model)
# print(car1.brand)

# CONSTRUCTOR         __init__()

# class Student:
    
#     college_name = "REC college"

#     name = "anonymous" # class attr
    
    # # DEFULAT CONSTRUCTOR            # bydefault

    # def __init__(self):
    #     pass
    
    # PARAMETER CONSTRUCTOR 
    
    # def __init__(self, name, marks):
    #     self.name = name
    #     self.marks = marks
    #  # INSTANCE ATTRIBUTES   self.name 
    #  # INSTANCE ATTRIBUTES   self.marks 
    #     print('creating new data to add')
    
# creating object (instance)

# s1 = Student("Ashwani", 67)         # ashwani = Attributes
# print(s1.name, s1.marks)        # obj.attr > class.attr

# s2 = Student("mohit", 88)
# print(s2.name, s2.marks)

# print(s2.college_name)   #or   student.college_name

# CLASS & iNSTANCE aTTRABUTES    class.attr (common)     obj.attr (different-different)



# class == attraibutes(data) & method


# class Student:
    
#     college_name = "REC college"
    
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("Ashwani", 67)
# s1.welcome()
# print(s1.get_marks())



# LET'S PRACTICE

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hii", self.name, "your avg score is :", sum/3)

# s1 = Student("tappu", [99, 67, 99])
# s1.get_avg()


# s1.name = "gogi"           # change attributes by renaname here
# s1.get_avg()



# STATIC METHODS     @staticmethod   (don't use  (self) parameter )   work as class.attr

# class Student:

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


#     @staticmethod    # decorator    class level

#     def hello():               
#         print("REC College")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hii", self.name, "your avg score is :", sum/3)

# s1 = Student("tappu", [99, 67, 99])
# s1.get_avg()


# s1.name = "gogi"           # change attributes by renaname here
# s1.get_avg()
# s1.hello()


# ABSTRACTION  & ENCUPLATION

# class Car:

#     def __init__(self):
#         self.accelrator = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.accelrator = True
#         print("car started..")


# car1 = Car()
# car1.start()

# let's practice

class Account:

    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance :", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was debited")
        print("total balance :", self.get_balance())

    def get_balance(self):
        return self.balance
        
acc1 = Account(10000, 7890)
acc1.debit(1000)
acc1.credit(500)
# print(acc1.balance)
# print(acc1.account_no) 
acc1.credit(40000)
acc1.debit(20000)
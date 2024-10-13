# del s1.name

# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("ashwani")
# del s1.name                    # for delete
# print(s1.name)

# Private(like) Attribute & methods :-

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass            # __  = for private only under the class
    
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1 = Account("1234", "7980")

# print(acc1.acc_no) 
# print(acc1.reset_pass())

# class person:
#     __name = "anonymous"         # attributes private __

#     def __hello(self):
#         print("hello person")
    
#     def welcome(self):
#         self.__hello()           # method private  __

# p1 = person()
# # print(p1.__name)
# print(p1.welcome())


# class owl:
#     def __init__(self, father):
#         self.father = father

# f1 = owl("big_owl")
# print(f1.father)

# INHARITANCE  PASS ONENTO ANOTHER ONE (P&M - CLASS(CHILD/DERIVED) & CLASS(PARENT/BASE))

# 1. single inharitance  
# class Car:
#    # color = "black"
#     @staticmethod
#     def start():
#         print("car started :")
#     @staticmethod
#     def stop():
#         print("car stoped :")

# class toyotacar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = toyotacar("fortuner")
# car2 = toyotacar("prius")

# print(car1.start())
# print(car1.color)

# 2. MULTILEVEL INHERITANCE

# class Car:

#     @staticmethod
#     def start():
#         print("car started :")
#     @staticmethod
#     def stop():
#         print("car stoped :")

# class toyotacar(Car):
#     def __init__(self, brand):
#         self.brand = brand

# class fortuner(toyotacar):
#     def __init__(self, type):
#         self.type = type

# car1 = fortuner("disel")
# car1.start()

# 3, Multiple inhertaince

# class A:
#     varA = "welcome to class A"
# class B:
#     varB = 'welcome to class B'
# class C(A, B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)


# SUPER METHOD      super()   access method of parents class

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started :")
    @staticmethod
    def stop():
        print("car stoped :")

class toyotacar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
car1 = toyotacar("prius", "electric")
print(car1.type)
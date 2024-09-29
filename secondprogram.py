# str1 = "this is a string."
# str2 = 'ashwani'
# str3 = """"this is string."""

# str1 = "This is a string.\nwe are creating toy."
# print(str1)

#BASIC OPERATION

# 1. concatenation

# str1 = "Ash"
# str2 = "wani"
# final_str = str1+str2
# print(final_str)

#2. length of str

# str1 = "Ash"
# len1 = len(str1)
# print(len1)
# str2 = "wani"
# len2 = len(str2)
# print(len2)
# final_str = str1+ " " +str2
# print(final_str)

#3. Indexing 

# str = "Ash wani"
# ch = str[0]  # or print(str[2])
# print(ch)

#4. Slicing   str[starting_idx:ending_idx] ending idx not included

# str = "Ashwani Kumar"
# print(str[3:9]) #or print(str[6:) or  print(str[6:len(str)]) or  print(str[:12])

# 5. slicing  NEGATIVE INDEX

# str = "Apple"
# print(str[-3:-1])

# STRING FUNCTIONS
# str.(endwith("er.")) 

# str = "i am a student"
# print(str.endswith("nt"))


# # str.captalize()

# str = "i am a student"
# # print(str.capitalize()) create a new string , if want to create changement on original then write
# str = str.capitalize()
# print(str)

# #str.replace( old, new)

# str = "i am student, my name is ashwani"
# print(str.replace("student" , "Teacher"))

# # str.find(word)

# str = "i am a student"
# print(str.find("n"))

# # str..count("am")  count the occurance

# str = "i am a  am am student"
# print(str.count("am"))


# Let's practice

# name = input("enter your name : ")
# print("length of your name is :",len(name))


# str = "122$,200$,700$"
# print(str.count("$"))



#CONDITIONAL STATEMENTS

# age = 23
# if(age >= 18):
#     print("drive car")


# light = "pink"
# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("wait")

# else:
#     print("light is broken")  # indentation space 

# print("end of code")

# #marks = 74
# marks = int(input("marks of the stdent : "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the students ->", grade)

# NESTing

# age = 98

# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("cannot drive.")

# Let practice

num = 5

rem = num % 2

if(rem == 0):
    print("EVEN")
else:
    print("ODD")

a = int(input("enter your number"))
b = int(input("enter your number"))
c = int(input("enter your number"))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b >= c):
    print("second number is largest", b)
else:
    print("third number is largest", c)

x = int(input("enter number: "))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
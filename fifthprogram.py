# LOOPS IN PYTHON

# count = 1               # Iterator
# while count <= 5:
#     print("hello")        # iterarion
#     count = count +1

# print(count)

# i = 1
# while i <= 5:
#     print("hello", i)
#     i+=1

# print  umber from 1 to 5

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")


# # LET PRACTICE

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# Q =3

# n = int(input("enter number :"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# Q = 4

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1


# Q = 5

# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# x = 36
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("found", i)
    
#     i +=1

# BREAK & Continue


# i = 1
# while i <= 5:
#      print(i)
#      if(i ==3):
#           break
#      i += 1

# print("end of loop")

# i = 1
# while i <= 10:
     
#      if(i%2 != 0):
#           i += 1
#           continue     #skip
#      print(i)
#      i+=1

# FOR EL IN LIST:       loop in python

# num = [1, 3, 5, 4, 7, 9]
     
# for val in num:
#     print(val)


# tup = (2, 4, 6, 8, 7)

# for num in tup:
#     print(num)

# #for el in str:
# # else:

# str = "Ashwani kumar"

# for char in str:
#     print(char)
# else:
#     print("balle")

# LET'S PRACTICE

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49]

# x = 49
# idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at idx", idx)
#         break
#     idx += 1

    
# range() fun in python st from 0 & increments by 1 default stop before a specical num 

# seq = range(8)

# for i in seq:
#     print(i)

#or

# for i in range(10):
#     print(i)

# for i in range(10): # stop
#     print(i)

# for i in range(2, 10): #(start , stop)
#     print(i)

# for i in range(2, 10, 2): #(start, stop, step)
#     print(i)                # that's called "LINEAR SEARCH"

 # LET'S PRACTICE

#Q = 1

# for i in range(1, 101):
#     print(i)

# #Q = 2

# for i in range(100, 0, -1):
#     print(i)

# # Q = 3

# for i in range(1, 11, +1):
#     print(3*i)


# PASS STATEMENT 

# for i in range(5):
#     pass              # for past work for future code null type hold place
# print("some useful work")


# LET'S PRACTICE

# n = 5
# sum = 0
# for i in range(1, n+1):
#     print("total of ", sum)
    
# sum += i 

# n =5

# fac = 1

# i =1

# while i <= n:
#     print("factorial :", sum)
# fac *= i


n = 5

fact = 1

for i in range(1, n+1):
    fact *= i
    print("factorial =", fact)




# FUNCTION & RECURSION

# FUNCTIONs         redundanciy decrease to use of function


# function defination
# def calc_sum(a, b):   # a, b = called  "parameters"
#     return a+b

# sum = calc_sum(1666, 2)  #3     1, 2 = arguments
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# def cal_avg(a, b, c):
#     return a + b + c

# sum = cal_avg(12, 30, 8)
# avg = sum/3
# print(avg)


# Default Parameter 

# def cal_prod(a = 1, b = 3):
#     print(a * b)
#     return a * b
# cal_prod()

# def cal_prod(a, b = 3):
#     print(a * b)
#     return a * b
# cal_prod(1)




# LET'S PRACTICE

# cities = ["delhi", "lucknow", "mainpuri", "noida", "chennai", "mumbai"]
# heros = ["saktiman", "thor", "spiderman", "doremon"]

# def print_len(list):
#     print(len(list))

# # print_len(cities)
# # print_len(heros)

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
    

# print_list(heros)



# def cal_fact(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     print(fact)

# cal_fact(3)

# def convertor(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val, "usd =", inr_val, "INR")

# convertor(2)

# Recursion  

def show(n):
    if(n == 0):          # base case
        return
    print(n)
    show(n-1)
    print("end")
show(3)





def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n

print(fact(4))


def cal_sum(n):
    if(n == 0):
        return 0
    return cal_sum(n-1) +n
  
sum = cal_sum(5)
print(sum)


def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

heros = ["spiderman", "superman", "batman", "hulk", "thor"]
print_list(heros)
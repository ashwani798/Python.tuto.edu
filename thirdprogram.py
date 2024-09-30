# LISTS

# marks = [94.4, 87.7, 67.3, 44.3, 34.9]
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["karan", 87.9, 67, "delhi"]
# print(student[0])
# student[0] = "Gogi putr"

# print(student)

#LIST SILICING               STARTING_IDX : ENDING_IDX

# marks = [45, 55, 58, 98, 50]
# print(marks[1:4])

# LIST METHODS
# list = [2, 4, 3]
# list.append(5)          # add list = [2, 3, 4, 5]
# print(list)

# list.sort()         accending order
# list = [2, 4, 3]
# print(list.sort())
# print(list)

# decending order  list.sort(reverse=True)

# list = [2, 4, 3]
# print(list.sort(reverse=True))
# print(list)

# list = ["banana", "apple", "papaya"]
# print(list.sort())
# print(list)

# list = ["banana", "apple", "papaya"]
# print(list.sort(reverse=True))
# print(list)

# reverse method   list.reverse()
# list = ['n', 'a', 'p', 'o', 'p','y']
# list.reverse()
# print(list)


# insert method   list.insert(idx, el)

# list = [2, 1, 3]
# list.insert(1,6)
# print(list)

#  # list.remove(1)
# list = [2, 1, 4, 5]
# #list.remove(2)
# list.pop(2)
# print(list)

#TUPLES IN PYTHON          BUILT-IN DATA TYPE  ()

# tup = (1, 3, 5, 7, 9)
# print(tup[0])

# #tup = (1,) # or tup = ("apple",)
# print(tup)
# print(type(tup))
# print(tup[1:4])

# tup.index(el)

# tup = (1, 4, 5, 7, 9)
# print(tup.index(4))    # index of the value

# tup.count(el)

# tup = (1, 4, 5, 7, 1, 9, 1)
# print(tup.count(1))

# LET'S PRACTICE

# movies = []
# mov1 = input("enter first movie :")     #movies.append.input("enter 1st movie : ")
# mov2 = input("enter second movie :")
# mov3 = input("enter third movie :")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
#print(movies)

# num1 = [1, 2, 1]
# num2 = [2, 3, 5]

# copy_num1 = num1.copy()

# copy_num1.reverse()

# if(copy_num1 == num1):
#     print("palindrome")
# else:
#     print("not palindrome")

grade = ["C", "D", "A", "A", "B", "B", "A" ]
# print(grade.count("A"))
grade.sort()
print(grade)


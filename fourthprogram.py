# # Dictionary & set

# info = {
#     "key" : "value",
#     "name" : "goli",
#     "age" : "12",                  # key:value ,  key not change
#     "learning" : "python",
#     "subjects" : ["opps", "c", "java"],
#     "topics" : ("dictionary", "set")
# }

# print(type(info))               # mutable like list and not change any thing

# print(info["name"])

# info["name"] = "Ashwani"
# print(info)
# info["surname"] = "Pandey"
# print(info)

# null_dict = {}
# null_dict["name"] = "sonu"
# print(null_dict)

# # NESTED DICIIONARIES

# student = {
#     "name" : "Ashwani Kumar",
#     "subjects" : {
#         "phy" : 30,
#         "his" : 92,
#     }
# }
# print(student["subjects"]['his'])

# print(student.keys())           # myDict.keys()


# print(list(student.values()))   # myDict.value()


# print(list(student.items()))     #myDict.items()

# # print(student["name2"])
# print(student.get("name2"))      #myDict.get("key")


# student.update({"name" : "Gogi", "city" : "Delhi"})  #myDict.update(newDict)
# print(student)


# # SET IN PYTHON

# collection = {1, 2, 2, 9,  2, 3, "hello", "hello", 7}      # unorderd

# print(type(collection))
# print(collection)
# print(len(collection))

# collection = set()     # if not write set for null set its type is DICT

# # print(type(collection))

# # SET METHODS   

# collection.add(1)           #set.add(el)
# collection.add(2)
# collection.add(2)

# collection.remove(1)       #set.remove(el)
# collection.add("ashwani")
# collection.add((1, 2, 3))


# collection.clear()           #set.clear()
# # collection.remove(7)
# print(len(collection))




# collection = {1, 2, 2, 9,  2, 3, "hello", "hello", 7}
# print(collection.pop())
# print(collection.pop())          #set.pop()      for random value 

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}

# print(set1.union(set2))      #set.union(set2)
# # print(set2)
# print(set1.intersection(set2)) #set.intersection(set2)


# # LET'S PARCTICE

# dictionary = {
#     "cat" : "a small number",
#     "table" : ["a piece of furniture", "list of facts and figure"]
# }

# print(dictionary)

# subjects = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }
# print(len(subjects))
# print(type(subjects))

# marks = {}

# x = int(input("enter phy :"))
# marks.update({"phy" : x})

# x = int(input("enter math :"))
# marks.update({"math" : x})

# x = int(input("enter his :"))
# marks.update({"his" : x})

# print(marks)


value = {

    ("float", 9.0),
    ("int", 9)
}
print(value)
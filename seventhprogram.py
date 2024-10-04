# FILE I\O
# (read & write & delete)

# f = open("eightprogram.py" , "r")       # r & t mode is default mode
# data = f.read(5)
# line = f.readline(5)
# print(data)
# print(type(data))
# f.close()       

# line1 = f.readline()
# print(line1)

# line2 = f.readline()
# print(line2)

# f.close()


# f = open("eightprogram.py" , "a")

# f. write("\nthen i wll move to reactjs.")

# f.close()


# f = open("eightprogram.py" ,"w+")
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# with syntax

# with open("eightprogram.py", "r") as f:
#     data = f.read()
#     print(data)

# with open("eightprogram.py", "w") as f:
#     f.write("new data")


# Deleting 

# import os              # module

# import os

# os.remove("eightprogram.py")


# LET'S PRACTICE


word = "learning"
with open("practice.txt", "r") as f: 
    # data = f.read()

    #   f.write("hi everyone\nwe are learning file I/O\n")
    #   f.write("using java.\nI like programming in java.")
    
    
# new_data = data.replace("java", "python")
# print(new_data)

    data = f.read()
    if(data.find("learning")):
        print("found")
    else:
        print("not found")



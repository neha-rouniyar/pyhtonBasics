# # basics of file handling in python
# a. "a" => opens an existing file
# b. "w" => writes to a file
# c. "a" => used for appending content to a file - creates a new one if it doesnt exist
# d. "x" => creates a specified file. 


# readline() => this reads a single line of text from the file

# to delete a file , we must import the os module. 
# The OS module in Python is a standard library module that provides a way to interact with the operating system.
# other modules of OS module include : os.mkdir, os.rmdir, os.rename(old_path, new_path), os.listdir(path)
# import os
# os.remove("abc.txt")

# # reading contents of an existing file
# with open("text.txt", "r") as filecontent:
#     content=filecontent.read()
#     print(content)

# #reading contents line by line
# with open("text.txt","r") as filecontent:
#     for line in filecontent:
#         print(line.strip())

# # creating file and writing content into it
# with open("abc.txt","w") as file:
#     file.write("Hey nehuhuhu")
# print("File created and content written")

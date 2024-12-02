# # # tuple example - these are used for unchangeable collection of items sth like configuration files
# array=(1,2,3,4,5,6,7,8,9)
# array.append(6) 
# # we cannot append here as tuple doesnt support for anything addition after its creation
# # can only access then through indexing and sliicing
# # print(array[0])
# print(array[3])


# # tuples concatenation
# tuple1=(1,2,3,4)
# tuple2=(5,6,7,8)
# # print(tuple1+tuple2)

# #checking the existence of items inside the tuple
# tuple1=(1,2,3,4)
# tuple2=(5,6,7,8)
# print(2 in tuple1) #checks if 2 is present in tuple1 or not
# print(0 in tuple2)

# # checking length of a tuple
# tuple1=(1,2,3,4)
# print(len(tuple1))

# **************************************************************************************************************************************************

#learning dictionary --  it is an unordered collection of key-value pairs. keys are unique and values can be of any datatype. define using curly braces { }
# this is used when needed to store data in key value pair 
# # creating a simple dictionary
# neha={"name":"nehuuu",
#       "age":24,
#       "department":"QA"
#       }
# print(neha)

# #accessing above values
# print(neha["age"])

# # adding new key-value
# neha["address"]="chabahil"
# print(neha)

# # deleting a key-value pair
# del neha['age']
# print(neha)

# # checking for a key in dictionary
# print("name" in neha)
# print("hgiguk" in neha)



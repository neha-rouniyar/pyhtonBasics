# print("hello")


# #printing nehu in upper case
# name="nehu"
# print(name.upper())


# #simple addition including diff datatype
# a=18
# b=3.5
# print(a+b)

# #nehu names and appending 
# names=["nehu","neha","nehahaha","nehuhuhu"]
# names.append("neha DD")
# print(names)

# #tuple example - these are used for unchangeable collection of items sth like configuration files
# array=(1,5,2,8)
# # array.append(6) -- we cannot append here as tuple doesnt support for anything addition after its creation
# print(array[0])
# print(array[3])

#dictionary example -- its a collection of key value pairs like an associative arrray 
neha_details={"name":"neha DD",
              "is_dd":"true",
              }
# print(neha_details["name"])
#adding a new pair to above associative array
neha_details["is_working"]="YASSSSS"
# print(neha_details)

#looping through above key value pair
for key,value in neha_details.items():
    print(key,value)
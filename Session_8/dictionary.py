# dictionary is a key-value pair

# dict = {
#     "Fast" : "In a Quick manner",
#     "Harry" : "A coder",
#     "marks" : 100,
#     "mylist" : [2 , 4 , 7],
#     "anotherDict" : {"aditi" : "myFriend"}
# }

# print(dict)

# print(dict["Fast"])

# print(dict["anotherDict"]['aditi'])

# print(dict["mylist"])



# dictionary functions

# print(dict.keys()) # prints the keys of the dictionary

# print(dict.values()) # prints all the values of the dictionary


# updateDict = {
#     "Lovish" : "friend" ,
#     2 : "number"
# }

# dict.update(updateDict)
# print(dict)


# list - can be updated
# tuple - cannnot be updated
# dictionary - can also be updated


dict = {
    "Fast" : "In a Quick manner",
    "Harry" : "A coder",
    "marks" : 100,
    "mylist" : [2 , 4 , 7],
    "anotherDict" : {"aditi" : "myFriend"}
}

print(dict["Fast"]) # prints the corresponding value to "Fast"
print(dict.get("Fast")) # prints the corresponding value to "Fast"


# print(dict["slow"]) # throws an error as slow is not present in the dictionary
print(dict.get("slow")) # return None as slow is not present in the dictionary
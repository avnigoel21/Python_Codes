# Can we have a set with 18(int) and "18"(str) as a value in it.

# sets doesnot contain duplicate values
# a = {18 , "18"}
# print(a)
# yes we can store 18 as both are in different data types(one in integer and other in string)



# Create a empty dictionary(key-value pair).
# Allow 4 friends to enter their favourite fruit as values and use keys as their names. 
# Names of friends are unique.

myDictionary = {}

a = input("Enter your favourite fruit Shubham: ")
b = input("Enter your favourite fruit Aditi: ")
c = input("Enter your favourite fruit Harry: ")
d = input("Enter your favourite fruit Smriti: ")

myDictionary['Shubham'] = a
myDictionary['Aditi'] = b
myDictionary['Harry'] = c
myDictionary['Smriti'] = d

print(myDictionary)

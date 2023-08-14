# write a program to create a dictionary of Hindi words with values as their english translation.
# provide user with an option to look it up.

myDict = {
    "pankha" : "Fan",
    "dabba" : "Box",
    "vastu" : "item"
}

a = input("Enter the hindi word: ")

print("the meaning of your hindi word is: " , myDict.get(a))

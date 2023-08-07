# Write a program to detect double spaces in a string.

st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")
print(doubleSpaces)

# Replace the double spaces to format the following string
print(st)
st = st.replace("  " , " ")
print(st)
# Write a program to fill in a letter template given below with name and date

letter = '''Dear <|NAME|> , 
YOU ARE SELECTED FOR THE JOB ROLE
<|DATE|> '''

name = input("Enter the name: ")
date = input("Enter the date: ")

letter = letter.replace("<|NAME|>" , name)
letter = letter.replace("<|DATE|>" , date)

print(letter)


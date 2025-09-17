#Grade tracker. asks for input for grades and lists them. 

count = 0 


gradeCount = int(input('How many grades are you inputting?: '))

while count < gradeCount:
    count += 1
    grades_listed = []
    gradeInput = int(input('Please enter the grades: '))



grades_listed.append(gradeInput)
print("Here is the final list for grades:" )
print(grades_listed)


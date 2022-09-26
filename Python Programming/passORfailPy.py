grade1 = int(input('Enter first grade: '))
grade2 = int(input('Enter second grade: '))
grade3 = int(input('Enter third grade: '))

average = (grade1 + grade2 + grade3) / 3
round(average, 2)

print ('The average grade is ', average)

if average <= 70:
    print('Failed!')

else:  
    print ('Passed.')
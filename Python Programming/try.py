grade = int(input('Enter first grade: '))

print ('The average grade is ', grade)

if (grade >= 91 and < 100):
    print('Your equivalent grade is A')
elif (grade >= 81 and <= 90):
    print('Your equivalent grade is B')
elif (grade >= 70 and <= 80):
    print('Your equivalent grade is C')
else:
    print('Your equivalent grade is F')
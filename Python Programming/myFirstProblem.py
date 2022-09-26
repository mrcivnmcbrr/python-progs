print ('---- MACHINE PROBLEM #1 ----')
name = input ('Please enter your name: ')
print ('----------------------------------')
print ('Good day, ' + name + '! Kindly enter your Midterm Grade & Final Grade')

mg = float(input('Enter Midterm Grade: '))
fg = float(input('Enter Final Grade: '))

sg = (mg * .40) + (fg * .60)
print ('----------------------------------')
round(sg, 2)
print ('Your Semestral Grade is ', sg)
#CollectionsMp3: Write a python program that will ask the user to
#input a number and output is equivalent in words

thisList = {
    '8': 'Eight',
    '23': 'Twenty-three',
    '24': 'Twenty-four',
    '1': 'One',
}

choice = input('Enter a number <8, 23, 24, 1 ONLY>: ')

if choice == '8' in thisList:
    print(thisList['8'])
elif choice == '23' in thisList:
    print(thisList['23'])
elif choice == '24' in thisList:
    print(thisList['24'])
elif choice == '1' in thisList:
    print(thisList['1'])
else:
    print('Invalid Input!')




#Dictionary 
carDictionary = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964,
}
print(carDictionary)
print(carDictionary['model'])
carDictionary['year'] = 2020
print(carDictionary['year'])

thisCollection = {
    1: [1,2,3,4,5],
    2: ['apple', 'banana', 'orange'],
    3: 'I am a string',
    4: 125,
}
print(thisCollection)
print(thisCollection[1])

#Strings in Python
str = 'Hello World' 
str1 = '''Hello 
        World!
        Good 
        Day'''
print(str)
print(str1)

strName = 'Edward'
print(strName[0])
print(strName[-1])
print(strName[5])

#even positions strings
strAlphabet = 'abcdefghijklmnopqrstuvwxyz'
print('\n')

for alpha in strAlphabet:
    print(alpha)

print('\n')

ctr = 0 
while(ctr <= 25):
    print(strAlphabet[ctr])
    ctr+=2




thisList = [1,2,3,4,5]
fruitList = ['apple', 'banana', 'cherry']

#LIST
print(thisList[4])
print(fruitList[1])

#Negative Indexing
print(thisList[-1])
print(fruitList[-2])

#Range of Indexing
print(thisList[2:4])
print(thisList[2:5])
print(thisList[:4])

#Range of Negative Indexing
print(thisList[-3:-1])

#To Change the value of the Index in the given value
thisList[2] = 6
print(thisList)

#Loop Through the List
thisList = [1,2,3,4,5]
for num in thisList:
    print(num)
    print(num+5)

#Check if item exists 
thisList = [1,2,3,4,5]
fruitList = ['apple', 'banana', 'cherry']

if 'banana' in fruitList:
    print('Yes')
else:
    print('No')

#List Length
thisList = [1,2,3,4,5]
fruitList = ['apple', 'banana', 'cherry']

print(len(thisList))
print(len(fruitList))

#Add Items
fruitList.append('orange')
print(fruitList)

#Insert Item
fruitList.insert(1,'orange')
print(fruitList)

#Remove Item
fruitList.remove('banana')
print(fruitList)

#Join Two LIST
longList = fruitList + thisList
print(longList)
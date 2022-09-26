#ColloectionsMp1: Make a Python program that will reverse the string below:

str = ('Hello World!')
reversedString=[]

index = len(str) #calculate length of string and save in index

while index > 0: 
    reversedString += str [index - 1] #save the value of str[index-1] in reversedString
    index = index - 1 #decrement index

print(reversedString) #reversed String 
#CollectionMp2: Write a program that will ask the user to input 
#a string and count the number of vowels from the input string.

str = input('Enter a string: ')
vowels = 0
vowel = set('aeiouAEIOU')

for letters in str:
    if letters in vowel:
        vowels = vowels + 1

print('No. of vowels: ', vowels)


    


   





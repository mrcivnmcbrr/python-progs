print('\n')
print('- - - - MACHINE PROBLEM #2 - - - -')

numb1 = int(input("Input the first number: "))
numb2 = int(input("Input the second number: "))
numb3 = int(input("Input the third number: "))

asc1 = min(numb1, numb2, numb3)
asc3 = max(numb1, numb2, numb3)
asc2 = (numb1 + numb2 + numb2) - asc3
print("Numbers in ascending order: ", asc1, asc2, asc3) 

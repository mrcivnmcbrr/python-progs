#Print the sum of all even and odd numbers from 1 to input number

#WHILELoop

num = int(input('Enter the number of range: '))
sumEven = 0
sumOdd = 0

ctr = 1
while (ctr <= num):
    if(ctr %2== 0):
        sumEven = sumEven + ctr
        
    else: 
        sumOdd = sumOdd + ctr

    ctr+=1

print('The sum of Even Numbers from 1 to {0} = {1}'.format(num, sumEven))
print('The sum of Odd Numbers from 1 to {0} = {1}'.format(num, sumOdd))
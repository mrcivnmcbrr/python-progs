#Print the sum of all even and odd numbers from 1 to input number
        #use for and while loop


#FORLoop
num = int(input('Enter the number of range: '))
sum = 0


for ctr in range(2, num, 2):
    sum = sum + ctr
print('The sum of Even Numbers from 1 to {0} = {1}'.format(num, sum))

sum = 0 
for ctr in range(1, num, 2):
    sum = sum + ctr
print('The sum of Odd Numbers from 1 to {0} = {1}'.format(num, sum))





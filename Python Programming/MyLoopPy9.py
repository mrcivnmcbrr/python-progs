#print all the perfect number from 1 to 500
#a perfect number is a positive integer that is equal to the sum
#of its positive divisors excluding the number it self
#6 - positive divisors are 1 + 2 + 3 = 6

#Returns true if num is perfect
def NumPerfect (num):
    #To store sum of divisors
    sum = 1
    #Find all divisors and add them
    ctr = 2

    while (ctr * ctr <= num):
        if (num % ctr == 0):
            sum = sum + ctr + num / ctr
        ctr += 1
    #If sum of divisors is equal to
    #n, then is a perfect number
    return (True if sum == num and num != 1 else False)
#Driver Program
print('All perfect numbers until 500')
num = 2

for num in range (500):
    if NumPerfect (num):
        print(num, ' is a perfect number')

#MPLoop3

#print all odd numbers from 1 to 20

#Solution 1
ctr = 1
while ctr <= 20:
   print(ctr)
   ctr = ctr + 2

#Solution 2
ctr = 1
while ctr <= 20:
   if ctr%2 == 1:
      print(ctr)
   ctr += 1

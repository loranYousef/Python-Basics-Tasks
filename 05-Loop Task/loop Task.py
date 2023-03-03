#1. Print numbers from 0 to 10 using while

'''
x=0
while x < 11 :
    print(x)
    x +=1
'''
    
#2. Print numbers from 0 to 1o using for
'''
for x in range(0,11):
    print(x)

'''

#3. Stop the loop if the number = 5
'''

for x in range(0,11):
    if x == 5 :
        break
    print(x)
'''
#4. Skip the 5 iteration from print
'''

for x in range(0,11):
    if x == 5 :
        continue
    print(x)

'''
#5. Print multiplication table from 1 to 5
'''

for x in range(1,6):
    print('-----------------')
    for y in range(1,6):
        print(f"{x} x {y} = {x*y}")

'''

#6. How to get numbers from 10 to 20 using range

'''
for x in range(9,20):
  print(x+1)
'''

#7. How to get numbers from 10 to 100 with 3 at each step using range

'''
for x in range(9,100,3):
  print(x+1)
'''


#8. Get a list of even numbers from 1 to 100 using for
'''

for x in range(0,102,2):
    
    print(x, end =',')

'''
#9. Get a list of even numbers from 1 to 100 using while

'''
x=0
while x in range(0,100):
    x+=2
    print(x, end =',')
'''
#10. Get a list of even numbers from 1 to 100 using range



#1.Check if 10 is bigger than 15 or not?

x = 10
if x > 15 :
    print('x is bigger than 15')
if x < 15 :
    print('x is less than 15')


#2. If 10 is not bigger than15 print x is smaller than 15

x = 10
if x > 15 :
    print('x is bigger than 15')
else  :
    print('x is smaller than 15')

#3. In which cases we will use all?

 #if we have to many and in line.
a = 10
b = 20
c = 30
if a == 10 and b ==20 and c == 30 :
    print('done')
a = 10
b = 20
c = 30
if all([a == 10 ,b == 20 ,c == 30 ]) :
    print('done')


#4. What is the differences between all, and

''all : takes all variables in list with comma all value should be true.
''and : put every variable with value than and next variables with value. all value shuld be true.

#5. What is the differences between any, or

any its like or but takes list of variable with comma

a = 10
b = 20
c = 30
if a == 10 or b ==255 or c == 300 :
    print('done')
a = 10
b = 20
c = 30
if any([a == 10 ,b == 205 ,c == 300 ]) :

#6. If we need all the conditions to be true we will use ....

'''and '''

#7. What is the differences between if, elif

'''if : it used just one time if the condition was true of false and used with else '''
'''elif: you can use as much you want. '''

#8. What is the differences between elif else 

'''else : it used just one time if the condition was not true of false'''
'''elif: you can use as much you want.'''

#9. Can we use more than one elif?

'''yes '''
 
#10. Can we use more than one else?

'''no just one time '''

#11. write s simple ternary operator

x = 10
print('x = 10') if x == 10 else print('x != 10')

#12. in elif, python will check all the conditions no matter what? 

'''yeah if the condition(if) was false and elif commes next line'''

#13. in elif we use else for ... ?

'''else condition commes with if and elif if both of them was false then else will be true.'''

#14. if we have this list [2,4,6,8,10]:

#1. check to see if 4 in this list or not

if  4  in a:
    print('4 in the list ')

#2. check to see if 4 and 6 in this list on not

if  4 and 6 in a:
    print('4,6 in the list ')


#3. check to see if 3 or 6 in this list

print(' 3 is in the list ')if  3 in a else print(' 3 is in not the list ')
    
print(' 6 is in the list ')if  6 in a else print(' 6 is not in the list ')



#4. check to see if 2, 4 and 5 in this list 

print(' 2 is in the list ')if  2 in a else print(' 2 is in not the list ')
    
print(' 4 is in the list ')if  4 in a else print(' 4 is not in the list ')
print(' 5 is in the list ')if  5 in a else print(' 5 is not in the list ')

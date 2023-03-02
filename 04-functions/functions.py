
#Python Functions Tasks



#1. Create a simple function that takes 2 numbers and print their values

def mysum(x,y):
    print(x)
    print (y)

mysum(5,6)


#2. Create a simple function that takes 2 numbers and return their values

def mysum(x,y):
    return x
    return y
    
    
l = mysum(5,6)
print(l)



#3. In the above return function, use keyword arguments when calling the function

def mysum(x,y):
    return x+y
   
    
l = mysum(x=2,y=3)
print(l)
    


#4. In the above return function, give x and y default values of O and call the function with no arguments

def mysum(x =0,y=0):
    return x+y
   
    
l = mysum()
print(l)
    

#5. Create a function that can take any number of arguments and print the sum of them

def mysum(arg,*vartuple):
    result = arg + sum(vartuple)
    return result 

   
    
l = mysum(1,2,3,4,5,6)
print(l)

 


#6. Create the same sum function using the lambda 

def mysum(arg,*vartuple):
    result = arg + sum(vartuple)
    return result 

    
l = mysum(1,2,3,4,5,6)
print(l)

 
mysum = lambda x,y: x+y
l = mysum(5,6)
print(l)


#7. Call the lambda function at the same definition line
(lambda x,y :x+y)(50,60)

#8. Write the difference between the local variable and global variable 

 '''global : variable is variable defined out of the functions.
 local: variable is variable defined in functions.'''





# Python oop Task 2


#1. Create a new class names SciCalc with 3 methods , sum , mull , power all of them takes 2 argument x, y
class Scicalc:
    def sum(self,x,y):
        pass
        
    def mull(self,x,y):
        pass
    
    def power(self,x,y):
        pass
c1 = Scicalc()

#2. Sum return the sum of x and y
class Scicalc:
    def sum(self,x,y):
        return x+y
    def mull(self,x,y):
    def power(self,x,y):
c1 = Scicalc()
c1.sum(5,6)


#3. Mull return the multiplication of x and y

class Scicalc:
    def sum(self,x,y):
        
    def mull(self,x,y):
        return x*y
    def power(self,x,y):
        return x,y
c1 = Scicalc()
c1.mull(5,6)


#4. The power return x power y

class Scicalc:
    def sum(self,x,y):
        
    def mull(self,x,y):
        
    def power(self,x,y):
        return x,y
c1 = Scicalc()
c1.power(0,1)


#5. Take an object from the class and call the 3 methodswith any numbers

class Scicalc:
    def sum(self,x,y):
        return x+y
    def mull(self,x,y):
        return x*y
    def power(self,x,y):
        return x,y

class Calc

c1 = Scicalc()
c1.sum(5,6)
c1.mull(5,6)
c1.power(0,1)


#6. Can we inherit from the class we created in the firsttask Calc
yeah could we


#7. Inherit from the Calc class , now remove the unneeded code the the SciCalc after inheriting
class Calc:
        def sum(self,x,y):
        return x+y
    def mull(self,x,y):
        return x*y
    def power(self,x,y):
        return x,y



class Scicalc(Calc):


c1 = Scicalc()
c1.sum(5,6)
c1.mull(5,6)
c1.power(0,1)

#8. call the 3 methods again from the SciCalc object
class Calc:
    def sum(self, x, y):
        return x + y
    def mull(self, x, y):
        return x * y
   

class Scicalc(Calc):
    def power(self, x, y):
        return x ** y
c1 = Scicalc()
c1.sum(5,6)
c1.mull(5,6)
c1.power(0,1)

#9. Now you should see the same result as before

class Calc:
    def sum(self, x, y):
        return x + y
    def mull(self, x, y):
        return x * y
   

class Scicalc(Calc):
    def power(self, x, y):
        return x ** y
c1 = Scicalc()
c1.sum(5,6)
c1.mull(5,6)
c1.power(0,1)



#10. Explain in few words what happened after inheriting
after inheriting if we need a function in Calc and we dont have it in SciCalc we can simply use inherting Calc in Scicalc



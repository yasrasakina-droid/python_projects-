#print ("bultin function ")
#a= 56
#b= 67
#c=sum((a,b))
#print(c)

#("user defined function ")
# user defined functions

def function1(a, b):
    """this is my function1 """
    multiply = a * b
   # print("Multiplication is:", multiply)
    return multiply
def function2(a, b):
    average = (a + b) / 2
    #print("Average is:", average)
    return average
# function calls
v=function1(5, 6)
y=function2(34, 45)
#print(v)
#print(y)
print (function1.__doc__)

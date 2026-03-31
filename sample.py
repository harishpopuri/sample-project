print("Hello World")
a= 1,2,3,4
b= 5,6,7,8
c=a+b
print("Tuple=" , c)
x=10
y=20        
z=x+y
print("Sum=" , z)
## A1 Function to add two numbers 
def add(a,b):
    return a+b
result=add(5,10)
print("Result=" , result)
## A2 Function to find the factorial of a number
try:
    num1=10
    num2=0
    result=num1/num2
    print("Result=" , result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


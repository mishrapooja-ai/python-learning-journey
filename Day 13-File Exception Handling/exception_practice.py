try:
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    result=num1/num2
    print(result)
except:
    print("Something went wrong") 


#Another Example
try:
    number=int(input("Enter a number:"))
    print(number)
except ValueError:
    print("Enter Valid number")    


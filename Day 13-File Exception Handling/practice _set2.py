try:
    num1=int(input("Enter a number 1:"))
    num2=int(input("Enter a number 2:"))
    result=num1/num2
except ZeroDivisionError:
    print("Cannot Divided by Zero")
except ValueError:
    print("Enter Valid Value")
else:
    print("Valid Number Entered Successfully")      
    print("The Answer is",result) 
finally:
    print("Thankyou for Using Calculator")         
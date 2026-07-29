try:
    number=int(input("Enter your Account Balance:"))    
    withdraw=int(input("Enter the withdrawel amount:"))
    result=number/withdraw
    print(result)
except ValueError:
    print("Enter Valid Value")
except ZeroDivisionError:
    print("Cannot be divided by zero")
else:
    print("Valid Number Entered Succssfully")  
finally:
    print("Congratulations!!")      


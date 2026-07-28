try:
    number=int(input("Enter a number:"))
    print(number)
except ValueError:
    print("Enetr Valid Number") 
else:
    print("Valid number Entered Successfully")      

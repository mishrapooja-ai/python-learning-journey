print("\n IF-Else in Python")
age=20
if age>=18:
    print("You are eligible to vote.")


age=15
if age>=18:
    print("You can Vote.") 
else:
    print("You cannot vote yet.")  


print("\n User Input with If-Else")
age=int(input("Enter a number:"))    
if age>=18:
    print("Congratulation! You are eligible to Vote.")
else:
    print("Sorry! You are not eligible to Vote.")


print("\n Even or Odd Number")
number=int(input("Enter a number:"))
if number%2==0:
    print("Even Number")
else:
    print("Odd Number")   

print("\n Positive or Negative NUmbers")   
number=int(input("Enter a number:"))
if number>=0:
    print("Positive Number")  
else:
    print("Negative Number") 


print("\n Grading System")
marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Need Improvement")           


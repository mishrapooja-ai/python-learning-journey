age=int(input("Enter your age:"))
if age<18:
    raise ValueError("You must be 18 years old")
print("Welcome")
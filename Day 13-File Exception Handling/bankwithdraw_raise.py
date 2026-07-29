balance=7000
withdraw=int(input("Enter the withdrawel amount:"))
if withdraw>balance:
    raise ValueError("Insufficient Balance")
print("ThankYou")
def calculate_gst(price):
    gst=price*18/100
    total=price+gst
    return total
price=float(input("Enter product price"))
final_price=calculate_gst(price)
print("Final Price is:",final_price)


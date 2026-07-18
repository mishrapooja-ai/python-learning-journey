shopping_list=["Milk","Bread","Toast"]
print("My Shopping Lists:")
print(shopping_list)
shopping_list.append("Apple")
print("My Updated Shopping Lists:")
print(shopping_list)
shopping_list.remove("Toast")
print(shopping_list)
#count the total items in the list
print("Total Items:",len(shopping_list))

#print one item at a time
print("My Shopping Items are:")
for item in shopping_list:
    print(item)

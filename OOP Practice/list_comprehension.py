numbers=[1,2,3,4,5]
squares=[num*num for num in numbers]
print(squares)
#multiiply every number by 5
numbers=[2,3,4,6,8]
result=[num*5 for num in numbers]
print(result)

#Convert every word to uppercase
names=["python","pooja","ai","mumbai"]
result=[name.upper() for name in names]
print(result)

#print only even numbers
numbers=[1,2,3,4,5,6,7,8,9]
even=[num for num in numbers if num%2==0 ]
print(even)


numbers=[10,20,25,35,45]
result=filter(lambda x:x>20,numbers)
print(list(result))

#keep only even numbers
even=[1,2,3,4,5,6,7,8,9]
answer=filter(lambda y:y%2==0,even)
print(list(answer))

#keep only numbers greater than 50
num=[10,20,30,40,50,60,70]
greater=filter(lambda z:z>50,num)
print(list(greater))


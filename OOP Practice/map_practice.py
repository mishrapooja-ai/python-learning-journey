#square every number
numbers=[1,2,3,4,5]
result=map(lambda x:x*x,numbers)
print(list(result))

#multiply every number by 10
numbers=[5,10,15,20]
result=map(lambda y:y*10,numbers)
print(list(result))

#convert names into uppercase
names=["pooja","rahul","amit"]
result=map(lambda name:name.upper(),names)
print(list(result))


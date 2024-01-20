#tuple is also the collection,element are in order,allow duplicate value and immutable(element inside tuple cannot be changed)
fruits=('orange','mango','guava','banana','apple','mango')
print(fruits)
print(fruits[1])
print(fruits[-1]) # last- apple
print(fruits[1:3])# 1,2

print(len(fruits)) #5
print(type(fruits))

print(fruits.count('mango')) # mango 2 time
print(fruits.count('berry')) #-0

print(fruits.index('orange')) # 0-first
print(fruits.index('mango')) # first mango position 

for x in fruits:
    print(x) 

y=list(fruits)
print(y)

  
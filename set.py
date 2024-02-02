#set is a unorder collection of unique elements

x=set()
x.add(1)
x.add(2)
x.add(1) # Adding duplicate elements won't be added (sets only store unique elements)
print(x) #{1,2}
fruits=('orange','mango','guava','banana','apple','mango')
print(set(fruits))

x=set(fruits)
print(x)

for a in x:
    print(a,end=' ')


#.union()
y={1,2,3,4}
set1=x.union(y)
print('\n',set1)
#  #update -add
x.update(y)
print(x)
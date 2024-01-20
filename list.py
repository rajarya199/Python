#list- collection of element,they are in order and mutable(i.e element inside list are changeable)
fruits=['apple','banana','guava','mango','orange']
print(fruits)
print(len(fruits))
#indexing
print(fruits[0])
print(fruits[0][0])
print(fruits[:3]) #0,1,2
print(fruits[2:]) # 2 to last
print(fruits[-1]) #last

#add item in list
#.append()
fruits.append('grapes')
print(fruits)
#.insert(index,'value') index-where to put
fruits.insert(2,'berry') # berry in 3rd
print (fruits)

#remove item from list
#1 pop()-> remove last element
#2 pop(index)-> remove from index position
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)

#.remove('value')
fruits.remove('apple')
print(fruits)
#sort() -ascending
fruits.sort()
print(fruits)
#reverse()--reverse the list
fruits.reverse()
print(fruits)

test=[1,2,3,4,5,6,7]
#clean()-empty the list but list will remain
test.clear() 
print(test)
#del()
del test
#print(test)-

# for loop
fruits1=['apple','banana','guava','mango','orange']
# x for no of iteration in fruits1
for x in fruits1:
    print(x)

#arithmetic operator
# +,-,*,/,%,//(floor division -no decimal point)
    a=5//2
print(a) # 2 (not 2.5)

#assignment operator
#+= -> x+=y is same as x= x+y
#-=

x=50
y=20
x+=y
print(x)
x-=10
print(x)

#comparision operator
#<,<=,==,!=
print(12<10)

#logical operator
#or,and,not
a=15>10 and 10>12
print(a)
a=not(15>10 and 10>12)
print(a)

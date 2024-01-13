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

#additem in list
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
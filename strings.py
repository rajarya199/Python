text='python is a high level programming languages'
print(text)
#len()- no of character with space
print(len(text))
print(type(text))

#indexing
print(text[0])
print(text[0:10]) #0-9
print(text[:10]) # default start 0
print(text[:20])
print(text[5:])# 5 to last
print(text[:])# 0- last
 
 #built in string methods
#upper()- uppercase
print(text.upper())
#lower()
print(text.lower())
#split() dydefault split from space and return in forms of list
print(text.split())
print(text.split('high')) # split from high 
#format string with placeholder
lang='python'
print('we are learning %s'%lang) # %s-->%lang
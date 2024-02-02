#dictionary is key value pair
# 'key':value
#key -unique
student={
    'first_name':'ram',
    'last_name':'karki',
    'age':30,
    'gender':'male',
    'subject':['html','css','js','python']
}
#student['key']
print (student['first_name'])
print(student['subject'])
print(type(student))
print(len(student))  

#loop 
for x in student:
    print(student[x]) # value

for x in student:
        print(x,student[x]) #key with value

for x in student:
          print(x,':',student[x])

# .keys()-return all key of the dictionary
# .values()->return all value of the dictionary
    
d={} 
d['fruits']='apple'
d['veg']='potato'
print(d)
#nesting with dictionary
nest_dict={'key1':{'nestkey':{'subnestkey':'final result'}}}
print(nest_dict)
print(nest_dict['key1'])
print(nest_dict['key1']['nestkey'])
print(nest_dict['key1']['nestkey']['subnestkey'])
# nested list


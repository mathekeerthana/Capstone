# unordered collection of items. It has key-value pair

dict_a={'name':'keerthi', 'age':12}
print(dict_a)

print(dict_a['name'])

# Member check

dict_b={'name':'keerthi', 'age':12}
result='age' in dict_b
print(result)

# add a key value for dictionary

dict_c={'name':'keerthi', 'age':12}
dict_c['country']='India'
dict_c['state']='AP'
print(dict_c)

# delete item

dict_c={'name':'keerthi', 'age':12}
del dict_c['age']
print(dict_c)

# update a value of particular Key

dict_d={'name':'keerthi', 'age':12,'country':'India','city':'AP'}
dict_d['city']='Vijayawada'
print(dict_d)


#delete a particular key

dict_e={'name':'keerthi', 'age':12,'country':'India','city':'AP'}

print("Dictionary before deleting",dict_e)

del dict_e['city']

print("Dictionary after deleting",dict_e)

print(dict_e)

# delete a key by using loops

dict_f={'name':'keerthi', 'age':12,'country':'India','city':'AP'}
#print(dict_f)

for each in list(dict_f):
    if each =='age':
        del dict_f[each]
key=dict(list(dict_f))
print(key)


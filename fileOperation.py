# sample program
'''
file =open('Dummy.txt','r')
print(file.read())
print(file)
print(file.mode)
print(file.name)

#file =close('Dummy')

# context manager

with open('Dummy.txt','r') as file:    # context manager
    print(file.read())
    print(file.readline(), end='')
    print(file.readline(), end='')
    print(file.tell())       # tells the last position in file
    #print(file.readlines())

with open('Dummy.txt','r') as file:
    for line in file:
        print(line, end='')


with open('Dummy.txt','r') as file:
    #file_content =file.read(80)
    #print(file_content,end='')

    file_content=file.readline()
    print(file_content,end='')
    print(file.tell)
'''

# Appending data from one file to another file
with open('Dummy.txt','r') as file1,open('keerthana.txt','a') as file2:
    for data in file1:
        file2.write(data)
#file2.close()
#file1.close()

# Alphabets code

for int in range(97,123):
    c= chr(int)
    with open(c+".txt",'w') as k:
        k.write(c)









i = 20
j = 30
k = 10
l = i + j + k
print(l)

# length of string
s = "keerthana"
print(len(s))

# int example
i = 20
print(i)
print(type(i))

# float example
f = 20.4
print(f)
print(type(f))

# complex example
c = 4 + 5j
print(c)
print(type(c))

# list example
l = [10, 'keerthi', 5.3]
print(l)
print(type(l))

# referring the same object
list_a = [1, 2, 3, 4]
list_b = list_a
print(id(list_a))
print(id(list_b))

# update one list
list_b[3] = 6
print(list_a)
print(list_b)

# slicing & indexing strings
s = "welcome"
s1 = s[5:0:-1]
print(s1)
# example os slicing
a = "abcdefghij"
a1 = a[10:0:-4]
print(a1)

# 2 integers M & N
m = 3
n = '6'
print(list(n * m))

# reverse of list
s = "Hello world"
s1 = s[::-1]
print(s1)

# first three characters of a string same or not
s = str(input())
s1 = str(input())
for i in s:
    for j in s1:
        if(j[0:2] ==i[0:2]):
            print("same")



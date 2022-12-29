# while loop
a=int(input())
counter=0
while counter<8:
    a=a+1
    print(a)
    counter =counter+1

# for loop

sentence ="python programmimg"
for i in sentence:
    print(i)

word="python"
for j in range(len(word)):
    print(j)

# sum of given numbers
list =[11,12,13,24,45,56,67]
sum=0
for i in list:
    sum=sum+i
print(sum)


sum=0
for i in range(0,7):
    sum=sum+i
print(sum)

# sum of N natural numbers
sum=0
for i in range(1,8):
    sum=sum+i
print(sum)

a=int(input())
sum=0
for i in a:
    sum =sum+i
print(sum)

# product of given numbers
product=1
list =[2,3,4,5,6]
for i in list:
    product =product*i
print(product)

# patterns
# solid rectangle

for i in range(1,3):
    for j in range(1,5):
        print("*",end=" ")
    print()
print("\n")

# solid square

 for each in range(0,4):
     for each2 in range(0,4):
         print("*", end=" ")
     print()
 print("\n")

 #solid Right angle triangle

 for each in range(0,4):
     for each2 in range(0,each+1):
         print("*" ,end=" ")
     print()
 print("\n")

# diagonal

n1 =int(input())
n2 =int(input())
for i in range(n1):
    for j in range(n2):
        if (i==j):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()

# mirror right angle triangle

for each in range(5):
    for each2 in range(5):
        if (each2>=each):
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
            print()

# Triangle

n1=int(input())
n2=int(input())
for each in range(n1):
    for each2 in range(n2):
        if(each + each2 == 2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
            print()


































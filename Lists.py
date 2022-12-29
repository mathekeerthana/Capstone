# remove duplicate elememts from list

list_l=[1,3,7,5,6,4,7,8,6,4]
list_set=set(list_l)
print(list(list_set))

# dynamic
list_l=[]
list_b=int(input())
for i in range(list_b):
    list_c=int(input("enter the values"))
    list_l.append(list_c)
    print(list_l)


# read N lines of input and create a nested list each lines as a list
list_a=[1,2,3]
list_b=[4,5,6]
list_c=[6,7,3]

list_d=list[list[list_a],list[list_b],list[list_c]]
print(list_d)



# Min and Max values in the list of Tuples
tuple_1=(22,13,24,15)
tuple_2=(23,45,67,46)
list_tup=list(tuple_1)
list_tup1=list(tuple_2)
for each in list_tup:
    for each2 in list_tup1:
        if each<each2:
            print("max Number")
        else:
            print("Min Number")
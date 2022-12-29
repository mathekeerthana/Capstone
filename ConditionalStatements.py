# if-else

a=int(input())
if a>0:
    print("positive")
else:
    print("negative")
print("end")

# Nested conditional blocks

Matches_Won =int(input())
Goals=int(input())
if Matches_Won>8:
    if Goals>20:
        print("Hii")
    print("Hello")

# Nested condition in else block
a=int(input())
b=int(input())
c=int(input())
is_a_greatest=(a>b) and (a>c)
if is_a_greatest:
    print(a)
else:
    is_b_greatest=(b>c)
    if is_b_greatest:
        print(b)
    else:
        print(c)

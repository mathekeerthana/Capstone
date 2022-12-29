# Functions

# Block of reusable code to perform specific action

def name():
    print("Hello")
name()

# arguments

def greeting(word):
    msg="Hello"+word
    print(msg)
name=input()
greeting(word=name)

# return the given argument

def argument(arg):
    print("My name is:"+arg)
argument( arg="keerthana")

# concatenate the messages

def concatenate(name):
    print("welcome" +name)
concatenate(name="welcome HCL")

# divisible by 7

def divisible(arg):

    if arg%7==0:
        print("True")
    else:
        print("False")
divisible(10)


# divisible by 3,5, 3&5
key=int(input())
def divi(key):
    if key%3==0 and key%5==0:
        print("MarcoPolo")
    elif key%5==0:
        print("Polo")
    elif key %3 ==0:
        print("Marco")
    else:
        print("no")
divi(key)

# square of each number

def square():
    int_a=list(map(int,input("enter the values").split(" ")))
    #print(int_a)
    list_a=[]
    #str_s=str(int_a)
    #int_b=list(str_s.split())
    for i in int_a:
        int_d = i**2
        list_a.append((int_d))
    print(list_a)
square()


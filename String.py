# slicing
s="keerthana"
x=s[0:8:2]
print(x)

# isdigit()

m="12345".isdigit()
print(m)

m="12345ae".isdigit()
print(m)

# strip
m="   9876543134  "
n=m.strip()
print(n)

name=". ,raji, ."
name1=name.strip(". ,")
print(name1)

# replace
Replace ="teh is python programming"
Repl = Replace.replace("teh" ,"the")
print(Repl)

# swap cases

Sentence="WelCoMe tO pYtHoN PRogrAMming"
print(Sentence.swapcase())

# convert date from one format to another format
Date ="11-08-2022"
Date_Form=Date.replace("-","/")
print(Date_Form)

# palindrome
Palindrome ="madam"
Palin_Drome=Palindrome[::-1]
if Palindrome == Palin_Drome:
    print("yes")
else:
    print("No")

a="python   java  c++"
print(a.replace(" ",""))


# character frequency
from collections import Counter
string_s="tic tac toe"
#for each in string_s:
list_string=list(string_s)
print(Counter(list_string))
  #  counter+=1


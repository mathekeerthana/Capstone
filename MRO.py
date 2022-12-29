class Higher_parentclass:
    def something(self):
        print("This is Higher parent class")

class Lower_parentclass1(Higher_parentclass):
    def something(self):
        print("This is Lower parentclass1")

class Lower_parentclass2(Higher_parentclass):
    def something(self):
        print("This is Lower parentclass2")

class Child_class(Lower_parentclass1,Lower_parentclass2):
    pass
   # def something(self):
       # print("This is childclass")


childObj=Child_class()
childObj.something()

import unittest
from student123 import Student     # Here we import classes

class teststudent(unittest.TestCase):

    def setUp(self):
        print("\nsetup")

    def tearDown(self):
        print("\nteardown")

    def test_email(self):
        print("test email")
        ob=Student("hi","hello",233)
        obj=Student("mani","chandana",21)
        self.assertEqual(ob.email,"hi.hello@gmail.com")
        self.assertEqual(obj.email,"mani.chandana@gmail.com")

        ob.first="john"
        self.assertEqual(ob.email,"john.hello@gmail.com")

        ob.last="paul"
        self.assertEqual(ob.email,"john.paul@gmail.com")

    def test_fullname(self):
        print("test fullname")
        ob1=Student("hi","helllo",34)
        self.assertEqual(ob1.fullname,"hi helllo")

    def test_apply_bonus(self):
        ob1=Student("hi","helllo",60)
        self.assertEqual(ob1.marks,60)
        ob1.apply_bonus()
        self.assertEqual(ob1.marks,90)

    def test_something(self):
        ob1=Student("keerthi","reddy",34)
        self.assertEqual(ob1.somevalue," ")
        ob1.something("middlename")
        self.assertEqual(ob1.somevalue,"keerthi.reddy@gmail.comkeerthi reddymiddlename")



if __name__=="__main__":
    unittest.main()

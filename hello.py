#import EmployeeScheme
import pyodbc
server = 'HCL-02-49\SQLEXPRESS01'
database = 'capstone123'
username = 'Keerthana'
password = 'Keerthireddy@77'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
class AlreadyExisted(Exception):
    pass
class Not_in_Rangeof_Bonus(Exception):
    pass
class Employee_Info:
    Bonus=2
    Projects=['Python','C','Java']
    def __init__(self,Name,Salary,Project,Emp_Id):
        self.Name=Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id
    def insert_values_in_table(self):
        query = '''INSERT INTO Employee_Table (Name, Salary, Project,Emp_Id)
                            VALUES('{0}',{1},'{2}',{3})  '''
        insertQuery = query.format(self.Name, self.Salary, self.Project,self.Emp_Id)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("1 row inserted")


obj1=Employee_Info('keerthana',50000,'JAVA',1)
obj1.insert_values_in_table()
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
    Projects=["Python","C","Java"]
    def __init__(self,Emp_Name,Salary,Project,Emp_Id):
        self.Emp_Name=Emp_Name
        self.Salary=Salary
        self.Project=Project
        self.Emp_Id=Emp_Id
    def insert_values_in_table(self):
        query = '''INSERT INTO Employee_Table (Emp_Name, Salary, Project,Emp_Id)
                            VALUES('{0}',{1},'{2}',{3})  '''
        insertQuery = query.format(self.Emp_Name, self.Salary, self.Project,self.Emp_Id)
        cursor.execute(insertQuery)
        cnxn.commit()
        print("1 row inserted")

    def Update_Salary_in_table(self,New_Salary,Emp_Name):
        try:
            self.New_Salary = New_Salary
            self.Emp_Name=Emp_Name
            if self.New_Salary != self.Salary:
                fileinfoQuery = '''Update Employee_Table SET Salary ='{0}' WHERE Emp_Name = '{1}' '''
                updateQuery = fileinfoQuery.format(New_Salary,self.Emp_Name)
                cursor.execute(updateQuery)
                cursor.commit()
            else:
                raise AlreadyExisted
        except AlreadyExisted:
            print("No Change in the Salary")
    def Add_Bonus_to_salary(self,bonus,Emp_Name):
        self.bonus=bonus
        self.Emp_Name=Emp_Name
        try:
            if self.bonus not in range(1,self.Bonus+1):
                raise Not_in_Rangeof_Bonus
            else:
                self.Salary=self.Salary+self.Salary*self.bonus
                Query = '''Update Employee_Table SET Salary ='{0}' WHERE Emp_Name = '{1}' '''
                updateQuery = Query.format(self.Salary, self.Emp_Name)
                cursor.execute(updateQuery)
                cursor.commit()
        except Not_in_Rangeof_Bonus:
            print("Bonus is Not in Range")
    def Change_Project_of_Emp(self,project,Emp_Name):
        self.project=project
        self.Emp_Name=Emp_Name
        if self.project in self.Projects:
            if self.project == self.Project:
                print("Project is Already exists")
            else:
                Query = ''' Update Employee_Table SET Project ='{0}' WHERE Emp_name = '{1}' '''
                updateQuery = Query.format(project, Emp_Name)
                cursor.execute(updateQuery)
                cursor.commit()
        else:
            print("Project is not in list")
    def Display_details_of_Emp(self):
        query=''' select * from Employee_Table WHERE Emp_Name='{0}' '''
        query1=query.format(self.Emp_Name)
        values=cursor.execute(query1)
        for details in values:
            print("Name:{0}  Salary:{1}  Project:{2}".format(details.Emp_Name , details.Salary , details.Project))
    def Delete_Employee_table(self):
        Query = ''' delete from Employee_Table where Emp_Name='keerthana'  '''
        cursor.execute(Query)
        cursor.commit()
        print("Employee has been deleted")

obj1=Employee_Info('srihari',50000,'python',2)
obj1.insert_values_in_table()
#obj=EmployeeScheme.Emp_Scheme()
#obj.employe_table()

obj1.insert_values_in_table()
obj1.Update_Salary_in_table(30000,'keerthana')
obj1.Add_Bonus_to_salary(1,'keerthana')
obj1.Change_Project_of_Emp('Java','python')
obj1.Display_details_of_Emp()
obj1.Delete_Employee_table()
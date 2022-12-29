class TableError(Exception):
    pass
import pyodbc
# Hardcoded Global variables used connect to DB
server = 'HCL-02-49\SQLEXPRESS01'
database = 'capstone123'
username = 'Keerthana'
password = 'Keerthireddy@77'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()

class Emp_Scheme:
    def employe_table(self):
            try:
                query1 = cursor.execute('''use capstone123''')
                query2 = cursor.execute('''create table Employee_Table
                                                       (
                                                       Emp_Id int NOT NULL,
                                                       Emp_Name varchar(50),
                                                       project varchar(50),
                                                       salary int,
                                                       primary key (Emp_Id)
                                                       )
                                                       ''')
                query3 = cursor.execute('''select * from Employee_Details''')
                cnxn.commit()
                print("Table created sucessfully")
            except TableError:
                print("Table already Exists")
obj = Emp_Scheme()
obj.employe_table()










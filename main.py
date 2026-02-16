import mysql.connector as connector

class DbHelper():
    def __init__(self):
        self.con = connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "Vikesh@2000",
            database = "Pytest"
        )
        print("Connection successful")
        
        cur = self.con.cursor()
        query = "CREATE TABLE IF NOT EXISTS Employee(Id INT PRIMARY KEY, Name VARCHAR(50), City VARCHAR(50))"
        cur.execute(query)
        print("Table created successfully")
    
    def insert_employee(self):
        cur = self.con.cursor()
        ID = int(input("Enter Employee ID: "))
        Name = input("Enter Employee Name: ")
        City = input("Enter Employee City: ")
        query = "INSERT INTO Employee(Id, Name, City) VALUES (%s,%s,%s)"
        cur.execute(query, (ID, Name, City))
        self.con.commit()
        print("Employee inserted successfully")

    def show_employees(self):
        cur = self.con.cursor()
        query = "SELECT * FROM Employee"
        cur.execute(query)
        for row in cur.fetchall():
            print(row)    

helper = DbHelper()
helper.insert_employee()
helper.show_employees()
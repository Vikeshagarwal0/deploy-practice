import mysql.connector as connector
class Student:
    def __init__(self):
        self.con = connector.connect(
        host = "localhost",
        user = "root",
        password = "Vikesh@2000",
        database = "pytest",
    )

    def create_table(self):
        query = "CREATE TABLE IF NOT EXISTS student(Id INT PRIMARY KEY, Name VARCHAR(20), Age INT)"
        cur = self.con.cursor()
        cur.execute(query)
        print("Table created successfully")

    def add_student(self,id, name, age):
        query = "INSERT INTO student(Id, Name, Age) VALUES(%s, %s, %s)"
        values = (id, name, age)
        cur = self.con.cursor()
        cur.execute(query,  values)
        self.con.commit()
        print("Student added successfully")

    def update_student(self,id, name, age):
        query = "UPDATE student SET Name = %s, Age = %s WHERE Id = %s"
        values = (name, age, id)
        cur = self.con.cursor()
        cur.execute(query, values)
        self.con.commit()
        print("Student updated successfully")

    def show_student(self):
        query = "SELECT * FROM student"
        cur = self.con.cursor()
        cur.execute(query)
        for student in cur:
            print(student)

    def delete_student(self,id):
        query = "DELETE FROM student WHERE Id = %s"
        value = (id,)
        cur = self.con.cursor()
        cur.execute(query, value)
        self.con.commit()
        print("Student deleted successfully")


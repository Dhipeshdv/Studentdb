import mysql.connector
from mysql.connector import Error


class Main:
    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="1234",
                database="school"  
            )
            print("Connected to MySQL Database!")
        except Error as e:
            print(f"Error: '{e}'")

    def insert_student(self, student):
        cursor = self.connection.cursor()
        try:
            query = """
            INSERT INTO students (student_id, name, age, gender, math, science, social, english, tamil, total)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, student)
            self.connection.commit()
            print("Student inserted successfully!")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def search(self, student_id):
        cursor = self.connection.cursor()
        try:
            query = "SELECT student_id, name, total FROM students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            data = cursor.fetchone()
            return data
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def delete_student(self, student_id):
        cursor = self.connection.cursor()
        try:
            query = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(query, (student_id,))
            self.connection.commit()
            print("Student deleted successfully!")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()
            
    def get_class_average(self):
        cursor = self.connection.cursor()
        try:
            query = "SELECT AVG(total) FROM students"
            cursor.execute(query)
            average = cursor.fetchone()[0]
            return average
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

    def update_marks(self, student_id, subject, new_mark):
        cursor = self.connection.cursor()
        try:
            query = f"UPDATE students SET {subject} = %s WHERE student_id = %s"
            cursor.execute(query, (new_mark, student_id))
            recalculate_query = """
            UPDATE students SET total = (math + science + social + english + tamil)
            WHERE student_id = %s
            """
            cursor.execute(recalculate_query, (student_id,))
            self.connection.commit()
            print(f"{subject.capitalize()} marks updated successfully!")
        except Error as e:
            print(f"Error: '{e}'")
            self.connection.rollback()

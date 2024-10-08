import tkinter as tk
from tkinter import messagebox  
import studentdb


class GUI:
    def firstwindow(self):
        self.myobj = studentdb.Main()
        self.win = tk.Tk()
        self.win.geometry("500x500")
        self.win.title("Student Data")
        b1 = tk.Button(self.win, text="ADD STUDENT DATA", command=self.add_stud)
        b1.place(x=150, y=50)
        b2 = tk.Button(self.win, text="SEARCH STUDENT DATA", command=self.search)
        b2.place(x=150, y=150)
        b3 = tk.Button(self.win, text="UPDATE STUDENT MARKS", command=self.update_marks)
        b3.place(x=150, y=250)
        b4 = tk.Button(self.win, text="CLASS AVERAGE", command=self.class_average)
        b4.place(x=150, y=350)
        b5 = tk.Button(self.win, text="DELETE", command=self.delete_student)
        b5.place(x=150, y=450)

        self.win.mainloop()

    def add_stud(self):
        self.win2 = tk.Tk()
        self.win2.geometry("500x500")
        self.win2.title("Add Student Data")

        l1 = tk.Label(self.win2, text='Student ID')
        l1.place(x=100, y=10)
        global e1, e2, e3, e4, e5, e6, e7, e8, e9
        e1 = tk.Entry(self.win2)
        e1.place(x=200, y=10)
        l2 = tk.Label(self.win2, text='Name')
        l2.place(x=100, y=60)
        e2 = tk.Entry(self.win2)
        e2.place(x=200, y=60)
        l3 = tk.Label(self.win2, text='Age')
        l3.place(x=100, y=110)
        e3 = tk.Entry(self.win2)
        e3.place(x=200, y=110)
        l4 = tk.Label(self.win2, text='Gender')
        l4.place(x=100, y=160)
        e4 = tk.Entry(self.win2)
        e4.place(x=200, y=160)
        l5 = tk.Label(self.win2, text='Math')
        l5.place(x=100, y=210)
        e5 = tk.Entry(self.win2)
        e5.place(x=200, y=210)
        l6 = tk.Label(self.win2, text='Science')
        l6.place(x=100, y=260)
        e6 = tk.Entry(self.win2)
        e6.place(x=200, y=260)
        l7 = tk.Label(self.win2, text='Social')
        l7.place(x=100, y=310)
        e7 = tk.Entry(self.win2)
        e7.place(x=200, y=310)
        l8 = tk.Label(self.win2, text='English')
        l8.place(x=100, y=360)
        e8 = tk.Entry(self.win2)
        e8.place(x=200, y=360)
        l9 = tk.Label(self.win2, text='Tamil')
        l9.place(x=100, y=410)
        e9 = tk.Entry(self.win2)
        e9.place(x=200, y=410)
        
        bt = tk.Button(self.win2, text="SUBMIT", command=self.submit)
        bt.place(x=250, y=450)
        
        back_btn = tk.Button(self.win2, text="Back", command=self.win2.destroy)
        back_btn.place(x=100, y=450)

        self.win2.mainloop()

    def submit(self):
        data = [e1.get(), e2.get(), e3.get(), e4.get(), int(e5.get()), int(e6.get()), int(e7.get()), int(e8.get()), int(e9.get())]
        total = sum(data[4:])
        data.append(total)
        self.myobj.insert_student(tuple(data))
        
        # Clear all entry fields
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e5.delete(0, tk.END)
        e6.delete(0, tk.END)
        e7.delete(0, tk.END)
        e8.delete(0, tk.END)
        e9.delete(0, tk.END)

        # Show success message
        messagebox.showinfo("Success", "Student data submitted successfully!")

    def search_back(self):
        self.win.destroy()
        self.win3.destroy()
        self.firstwindow()

    def search(self):
        self.win3 = tk.Tk()
        self.win3.geometry("500x500")
        self.win3.title("Search")

        l1 = tk.Label(self.win3, text='Student ID')
        l1.place(x=50, y=150)
        global e10
        e10 = tk.Entry(self.win3)
        e10.place(x=150, y=150)
        b1 = tk.Button(self.win3, text="Search", command=self.display_search)
        b1.place(x=300, y=150)

        back_btn = tk.Button(self.win3, text="Back", command=self.search_back)
        back_btn.place(x=100, y=450)
        

    def display_search(self):
        student_id = e10.get()
        result = self.myobj.search(student_id)
        if result:
            
            messagebox.showinfo("Search Result", f"Student ID: {result[0]}, Name: {result[1]}, Total: {result[2]}")
            
            
            e10.delete(0, tk.END)
        else:
            messagebox.showerror("Not Found", "Student not found")


    def delete_student(self):
        self.win4 = tk.Tk()
        self.win4.geometry("500x500")
        self.win4.title("Delete Student")

        l1 = tk.Label(self.win4, text='Student ID')
        l1.place(x=50, y=150)
        global e11
        e11 = tk.Entry(self.win4)
        e11.place(x=150, y=150)
        b1 = tk.Button(self.win4, text="Delete", command=self.delete)
        b1.place(x=300, y=150)

        back_btn = tk.Button(self.win4, text="Back", command=self.win4.destroy)
        back_btn.place(x=100, y=450)

    def delete(self):
        try:
            student_id = e11.get()
            self.myobj.delete_student(student_id)
            messagebox.showinfo("Success", f"Student {student_id} deleted successfully!")
            
            
            e11.delete(0, tk.END)
        except Exception as ex:
            messagebox.showerror("Error", f"Error deleting student: {ex}")


    def class_average(self):
        try:
            avg = self.myobj.get_class_average()
            messagebox.showinfo("Class Average", f"Class Average: {avg:.2f}")
        except Exception as ex:
            messagebox.showerror("Error", f"Error retrieving class average: {ex}")

    def update_marks(self):
        self.win5 = tk.Tk()
        self.win5.geometry("500x500")
        self.win5.title("Update Marks")

        l1 = tk.Label(self.win5, text="Student ID")
        l1.place(x=50, y=100)
        global e12
        e12 = tk.Entry(self.win5)
        e12.place(x=150, y=100)

        l2 = tk.Label(self.win5, text="Select Subject")
        l2.place(x=50, y=150)
        global subject_var
        subject_var = tk.StringVar(self.win5)
        subject_var.set("Math") 
        subjects = ['math', 'science', 'social', 'english', 'tamil']
        subject_menu = tk.OptionMenu(self.win5, subject_var, *subjects)
        subject_menu.place(x=150, y=150)

        l3 = tk.Label(self.win5, text="New Marks")
        l3.place(x=50, y=200)
        global e13
        e13 = tk.Entry(self.win5)
        e13.place(x=150, y=200)

        b1 = tk.Button(self.win5, text="Submit", command=self.update_student_marks)
        b1.place(x=300, y=250)

        back_btn = tk.Button(self.win5, text="Back", command=self.win5.destroy)
        back_btn.place(x=100, y=450)

    def update_student_marks(self):
        try:
            student_id = e12.get()
            subject = subject_var.get()
            new_marks = e13.get()
            
            self.myobj.update_marks(student_id, subject, new_marks)
            messagebox.showinfo("Success", f"{subject.capitalize()} marks updated successfully!")
            
            
            e12.delete(0, tk.END)
            e13.delete(0, tk.END)
        except Exception as ex:
            messagebox.showerror("Error", f"Error updating marks: {ex}")

            

G = GUI()
G.firstwindow()

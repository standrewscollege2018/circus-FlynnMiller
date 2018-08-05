from tkinter import *


def delivery():
    print("Delivery")

root =Tk()
root.title("Option menu")

student_list = ["John", "James", "Steve"]

selected_student = StringVar()
selected_student.set(student_list[0])

student_menu = OptionMenu(root, selected_student, *student_list)
student_menu.config(bg='red')
student_menu['menu'].config(fg='black', bg='pink')
student_menu.grid(row=0)


root.mainloop()

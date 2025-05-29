from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import os
import pickle
import re



class User:
    def __init__(self, id, name, family, username, password, active=True):
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.password = password
        self.active = active

    def save(self):
        print (f"{self.id}: {self.name} {self.family} ({'Active' if self.active else 'Inactive'})saved")


def check_file(filename):
    return os.path.exists(filename)


def read_from_file(filename):
    if check_file(filename):
        file = open(filename, "rb")
        data_list = pickle.load(file)
        file.close()
        return data_list
    else:
        file = open(filename, "wb")
        file.close()
        return []

def write_to_file(filename, data_list):
    file = open(filename, "wb")
    pickle.dump(data_list, file)
    file.close()


def user_validator(user):
    errors = []
    if not (type(user[1]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user[1])):
        errors.append("user Name is Invalid.")

    if not (type(user[2]) == str and re.match(r"^[a-zA-Z\s]{3,30}$", user[2])):
        errors.append("user Family is Invalid.")

    if not (type(user[3]) == str , user[3]):
        errors.append("username is Invalid.")

    if not (type(user[4]) == int and user[4] > 0):
        errors.append("Password is Invalid.")
    return errors
user_list = read_from_file("users.dat")
def load_data(user_list):

    user_list = read_from_file("users.dat")
    for row in table.get_children():
        table.delete(row)
    for user in user_list:
        table.insert("", END, values=user)

def reset_form():
    id.set(len(user_list) + 1)
    name.set("")
    family.set("")
    username.set("")
    password.set("")
    active.set(True)
    load_data(user_list)

def save_btn_click():
    user = (id.get(), name.get(), family.get(), username.get(), password.get(), active.get())
    errors = user_validator(user)
    if errors:
        msg.showerror(title="Error", message="\n".join(errors))
    else:
        msg.showinfo(title="Saved", message="User successfully saved")
        user_list.append(user)
        write_to_file("users.dat", user_list)
        reset_form()

def edit_btn_click():
    selected = table.focus()
    if not selected:
        msg.showerror("Error", "Please select a user to edit")
        return
    updated_user = (id.get(), name.get(), family.get(), username.get(), password.get(), active.get())
    index = int(id.get()) - 1
    user_list[index] = updated_user
    write_to_file("users.dat", user_list)
    msg.showinfo("Edited", "User info updated")
    reset_form()

def remove_btn_click():
    selected = table.focus()
    if not selected:
        msg.showerror("Error", "Please select a user to remove")
        return
    selected_user = table.item(selected)["values"]
    user_list.remove(tuple(selected_user))
    write_to_file("users.dat", user_list)
    msg.showinfo("Removed", "User removed")
    reset_form()

def table_select(x):
    selected_user = table.item(table.focus())["values"]
    if selected_user:
        id.set(selected_user[0])
        name.set(selected_user[1])
        family.set(selected_user[2])
        username.set(selected_user[3])
        password.set(selected_user[4])
        active.set(selected_user[5])


window = Tk()
window.title("User Management")
window.geometry("800x300")

#ID
Label(window, text="ID").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=20)

#NAME
Label(window, text="Name").place(x=20, y=50)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=50)

#FAMILY
Label(window, text="Family").place(x=20, y=80)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=80)

#USERNAME
Label(window, text="Username").place(x=20, y=110)
username = StringVar()
Entry(window, textvariable=username).place(x=100, y=110)

#PASSWORD
Label(window, text="Password").place(x=20, y=140)
password = StringVar()
Entry(window, textvariable=password, show="*").place(x=100, y=140)

active = BooleanVar()
Radiobutton(window, text="Active", variable=active, value=True).place(x=100, y=170)
Radiobutton(window, text="Inactive", variable=active, value=False).place(x=160, y=170)

Button(window, text="Save", width=8, command=save_btn_click).place(x=20, y=210)
Button(window, text="Edit", width=8, command=edit_btn_click).place(x=100, y=210)
Button(window, text="Remove", width=8, command=remove_btn_click).place(x=180, y=210)
Button(window, text="Clear", width=25, command=reset_form).place(x=20, y=250)


table = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6), show="headings")
table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="Username")
table.heading(5, text="Password")
table.heading(6, text="Active")

table.column(1, width=40)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=60)

table.bind("<<TreeviewSelect>>", table_select)
table.place(x=300, y=20, width=470, height=220)


load_data(user_list)
reset_form()

window.mainloop()

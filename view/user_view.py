from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from model.repository.file_manager import *
from model.entity.user import User
from model.tools.validation import user_validator

FILENAME = "../model/repository/users.dat"
user_list = read_from_file(FILENAME)

def load_data():
    user_list = read_from_file(FILENAME)
    for row in table.get_children():
        table.delete(row)
    for user in user_list:
        if isinstance(user,User):
            table.insert("", END, values=user.to_tuple())


def reset_form():
    id.set(len(user_list) + 1)
    name.set("")
    family.set("")
    username.set("")
    password.set("")
    active.set(True)
    load_data()


def save_btn_click():
    user = User(id.get(), name.get(), family.get(), username.get(), password.get(), active.get())
    errors = user_validator(user)
    if errors:
        msg.showerror("validation Error", "\n".join(errors))
        return
    else:
        table.insert("", END, values=(user.id, user.name, user.family, user.username, user.password, user.active))
        msg.showinfo(title="Saved", message="User successfully saved")
        user_list.append(user)
        write_to_file(FILENAME, user_list)
        reset_form()



def edit_btn_click():
    selected = table.focus()
    if not selected:
        msg.showerror("Error", "Please select a user to edit")
        return
    updated_user =User(id.get(),name.get(),family.get(),username.get(),password.get(),active.get())
    index = int(id.get()) - 1
    user_list[index] = updated_user
    write_to_file(FILENAME, user_list)
    msg.showinfo("Edited", "User info updated")
    load_data()
    reset_form()


def remove_btn_click():
    selected = table.focus()
    if not selected:
        msg.showerror("Error", "Please select a user to remove.")
        return
    index = int(table.index(selected))
    del user_list[index]
    write_to_file(FILENAME, user_list)
    msg.showinfo("Removed", "User removed")
    reset_form()

def table_select(x):
    selected= table.item(table.focus())["values"]
    if selected:
        selected_user = User(*selected)
        if selected_user:
            id.set(selected_user.id)
            name.set(selected_user.name)
            family.set(selected_user.family)
            username.set(selected_user.username)
            password.set(selected_user.password)
            active.set(selected_user.active)


window = Tk()
window.title("User Management")
window.geometry("800x360")

# ID
Label(window, text="ID").place(x=20, y=20)
id = IntVar(value=1)
Entry(window, textvariable=id, state="readonly").place(x=100, y=20)

# NAME
Label(window, text="Name").place(x=20, y=50)
name = StringVar()
Entry(window, textvariable=name).place(x=100, y=50)

# FAMILY
Label(window, text="Family").place(x=20, y=80)
family = StringVar()
Entry(window, textvariable=family).place(x=100, y=80)

# USERNAME
Label(window, text="Username").place(x=20, y=110)
username = StringVar()
Entry(window, textvariable=username).place(x=100, y=110)

# PASSWORD
Label(window, text="Password").place(x=20, y=140)
password = StringVar()
Entry(window, textvariable=password, show="*").place(x=100, y=140)

active = BooleanVar()
Radiobutton(window, text="Active", variable=active, value=True).place(x=100, y=170)
Radiobutton(window, text="Inactive", variable=active, value=False).place(x=160, y=170)

Button(window, text="Save", width=8, command=save_btn_click).place(x=20, y=210)
Button(window, text="Edit", width=8, command=edit_btn_click).place(x=100, y=210)
Button(window, text="remove", width=8, command=remove_btn_click).place(x=180, y=210)
Button(window, text="Clear", width=25, command=reset_form).place(x=20, y=250)

table = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6), show="headings")
table.heading(1, text="ID")
table.heading(2, text="Name")
table.heading(3, text="Family")
table.heading(4, text="Username")
table.heading(5, text="Password")
table.heading(6, text="Active")

table.column(1, width=50)
table.column(2, width=100)
table.column(3, width=100)
table.column(4, width=100)
table.column(5, width=100)
table.column(6, width=60)

table.bind("<<TreeviewSelect>>", table_select)
table.place(x=300, y=20, width=480, height=220)

reset_form()
window.mainloop()

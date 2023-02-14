from tkinter import *
import tkinter as tk
from tkinter import messagebox
import json


# ---------------- User section function----------------

def incorrect(message):
    """
    A function who gives alert messages in case of an error or shortage in
    filling in the data and sends it in the form of a message box.
    :param message: The message should appear on the screen
    :return: Message box.
    """
    top.geometry("800x550")
    messagebox.showinfo("information", message)


def user_pass():
    """
    Converts the password and username fields in the user section to normal
        and log as admin and log as user to display
    """
    sbmitbtn1['state'] = tk.DISABLED
    sbmitbtn2['state'] = tk.DISABLED
    sbmitbtn3['state'] = tk.NORMAL
    e1['state'] = tk.NORMAL
    e2['state'] = tk.NORMAL


def check():
    global ya
    try:
        with open('json/user.json', 'r') as infile:
            data = json.load(infile)
        for x in data["user"]:
            if x["username"] == u_name.get().lower() and x["password"] == passw.get():
                order()
                ya = 1
            else:
                continue
        if ya != 1:
            message = "The password or username is incorrect, please try again"
            incorrect(message)
            user_pass()
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    ya = 0
    e1.delete(0, 'end')
    e2.delete(0, 'end')


def order():
    """
    Converts all fields and buttons within the section part
    to status normal. Where it becomes possible to use it

    """
    sbmitbtn3['state'] = tk.DISABLED
    sbmitbtn4['state'] = tk.NORMAL
    sbmitbtn5['state'] = tk.NORMAL
    sbmitbtn6['state'] = tk.NORMAL
    sbmitbtn8['state'] = tk.NORMAL
    e1['state'] = tk.DISABLED
    e2['state'] = tk.DISABLED
    e3['state'] = tk.NORMAL
    e4['state'] = tk.NORMAL
    e5['state'] = tk.NORMAL


def log_out():
    """
    It returns all fields and buttons to the state they were in when starting the program
    """
    sbmitbtn1['state'] = tk.NORMAL
    sbmitbtn2['state'] = tk.NORMAL
    sbmitbtn3['state'] = tk.DISABLED
    sbmitbtn4['state'] = tk.DISABLED
    sbmitbtn5['state'] = tk.DISABLED
    sbmitbtn6['state'] = tk.DISABLED
    sbmitbtn8['state'] = tk.DISABLED
    sbmitbtn9['state'] = tk.DISABLED
    sbmitbtn10['state'] = tk.DISABLED
    sbmitbtn11['state'] = tk.DISABLED
    sbmitbtn12['state'] = tk.DISABLED
    sbmitbtn13['state'] = tk.DISABLED
    e1['state'] = tk.DISABLED
    e2['state'] = tk.DISABLED
    e3['state'] = tk.DISABLED
    e4['state'] = tk.DISABLED
    e5['state'] = tk.DISABLED
    e6['state'] = tk.DISABLED
    e7['state'] = tk.DISABLED
    e8['state'] = tk.DISABLED
    e9['state'] = tk.DISABLED
    e10['state'] = tk.DISABLED
    e11['state'] = tk.DISABLED
    e12['state'] = tk.DISABLED
    e13['state'] = tk.DISABLED
    e14['state'] = tk.DISABLED
    e15['state'] = tk.DISABLED
    e16['state'] = tk.DISABLED
    e17['state'] = tk.DISABLED


def search_book():
    """
    This function searches for a book in the library if it exists, then it sends
    the information about the book in the form of a message box.
    If it is not exists, it sends a warning message.
    """
    global ya
    try:
        with open('json/books.json', 'r') as infile:
            data = json.load(infile)
        for x in data["books"]:
            if x["bookname"] == b_search.get().lower():
                message = x["bookname"] + "\nAuthor is" + x["author"] + "\nLouker number " \
                          + str(x["locker"]) + "\n Collon number " + str(x["col"]) + "\nRow number " \
                          + str(x["row"]) + "\nNumber of book " + str(x["number"])
                incorrect(message)
                ya = 1
            else:
                continue
        if ya != 1:
            message = "The book is not found"
            incorrect(message)
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    ya = 0
    e3.delete(0, 'end')


def abut():
    """
    This function shows information about the user
    The number and names of the books he borrowed
    """
    try:
        with open('json/user.json', 'r') as infile:
            data = json.load(infile)
        for x in data["user"]:
            if x["username"] == u_name.get().lower():
                message = str(x["books number"]) + "\n" + ", ".join(x["books"])
                incorrect(message)
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)


def check_out():
    """
    This function is a bit long and complicated
    It checks three conditions
      1- The name of the book in the library
      2- Sufficient copies of this book are available in the library
      3- User does not have this book on his file at the moment
    If the book meets conditions, the program deletes one copy from the main library and adds it to the user's file
    If one of the previous conditions is not met, the program sends a warning message about the problem.
    """
    global ya, yb, yc
    q, p, r, s = 0, 0, 0, 0
    try:
        with open('json/books.json', 'r') as infile:
            data = json.load(infile)
            for x in data["books"]:
                if x["bookname"] == out_book.get().lower():
                    r = p
                    ya = 1
                    if data["books"][p]["number"] == 0:
                        yb = 1
                    else:
                        continue
                else:
                    p += 1
                    continue
        with open('json/user.json', 'r') as infile:
            data = json.load(infile)
            for x in data["user"]:
                if x["username"] == u_name.get().lower():
                    s = q
                    for z in data["user"][q]["books"]:
                        if z == out_book.get().lower():
                            yc = 1
                else:
                    q += 1
        if ya == 1:
            if yb == 0:
                if yc == 0:
                    data["user"][s]["books number"] += 1
                    data["user"][s]["books"].append(out_book.get().lower())
                    with open('json/user.json', 'w') as outfile:
                        json.dump(data, outfile, ensure_ascii=False)
                    with open('json/books.json', 'r') as infile:
                        data = json.load(infile)
                    data["books"][r]["number"] -= 1
                    with open('json/books.json', 'w') as outfile:
                        json.dump(data, outfile, ensure_ascii=False)
                        message = "Processing was successful"
                        incorrect(message)
                else:
                    message = "You have a copy of this book already"
                    incorrect(message)
            else:
                message = "There are no copies of this book available"
                incorrect(message)
        else:
            message = "The book is not found"
            incorrect(message)

    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    e4.delete(0, 'end')
    ya, yb, yc = 0, 0, 0


def check_in():
    """
    This function checks two conditions
        1 The name of the book in the library
        2  a copy of this book are in the user's file
    If the previous two conditions are met, the program will delete the
     book from the user's file and add a copy to the user's file
    If one of the previous conditions is not met, the program sends
    a warning message about the problem
    """
    global ya, yb, yc
    q, p, r, s, t = 0, 0, 0, 0, 0
    try:
        with open('json/books.json', 'r') as infile:
            data = json.load(infile)
            for x in data["books"]:
                if x["bookname"] == in_book.get().lower():
                    r = p
                    ya = 1
                else:
                    p += 1
        with open('json/user.json', 'r') as infile:
            data = json.load(infile)
            for x in data["user"]:
                if x["username"] == u_name.get().lower():
                    s = q
                    for z in data["user"][s]["books"]:
                        if z == in_book.get().lower():
                            yb = 1
                            t = yc
                        else:
                            yc += 1
                else:
                    q += 1
        if ya == 1:
            if yb == 1:
                data["user"][s]["books number"] -= 1
                del data["user"][s]["books"][t]
                with open('json/user.json', 'w') as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
                with open('json/books.json', 'r') as infile:
                    data = json.load(infile)
                    data["books"][r]["number"] += 1
                    with open('json/books.json', 'w') as outfile:
                        json.dump(data, outfile, ensure_ascii=False)
                        message = "Processing was successful"
                        incorrect(message)
            else:
                message = "You don't have this book in your profile"
                incorrect(message)
        else:
            message = "The book is not found"
            incorrect(message)
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    ya, yb, yc = 0, 0, 0
    e5.delete(0, 'end')


# ---------------- Admin section function----------------
def admin_pass():
    """
    Converts the password and username fields in the admin section to normal
        and log as admin and log as user to display
    """
    sbmitbtn1['state'] = tk.DISABLED
    sbmitbtn2['state'] = tk.DISABLED
    sbmitbtn9['state'] = tk.NORMAL
    e6['state'] = tk.NORMAL
    e7['state'] = tk.NORMAL


def check_admin():
    """
    Checks the admin name and password
    And that is via the json file that contains the name and passwords of the admin.
    In the event that the name or password does not match, a warning message will be sent
    """
    global ya
    try:
        with open('json/admin.json', 'r') as infile:
            data = json.load(infile)
        for x in data["admins"]:
            if x["adminname"] == admin_name.get().lower() and x["password"] == admin_pass.get():
                order_a()
                ya = 1
            else:
                continue
        if ya != 1:
            message = "The password or adminname is incorrect, please try again"
            incorrect(message)
        ya = 0
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    e6.delete(0, 'end')
    e7.delete(0, 'end')


def order_a():
    """
    The state changes to normal in all fields and button in admin section
    """
    sbmitbtn9['state'] = tk.DISABLED
    sbmitbtn10['state'] = tk.NORMAL
    sbmitbtn11['state'] = tk.NORMAL
    sbmitbtn12['state'] = tk.NORMAL
    sbmitbtn13['state'] = tk.NORMAL
    e6['state'] = tk.DISABLED
    e7['state'] = tk.DISABLED
    e8['state'] = tk.NORMAL
    e9['state'] = tk.NORMAL
    e10['state'] = tk.NORMAL
    e11['state'] = tk.NORMAL
    e12['state'] = tk.NORMAL
    e13['state'] = tk.NORMAL
    e14['state'] = tk.NORMAL
    e15['state'] = tk.NORMAL
    e16['state'] = tk.NORMAL
    e17['state'] = tk.NORMAL


def add_user():
    """
     This function checks two conditions.
      1- Username does not exist before.
      2-Both the name and password fields are full.
    If the new user meets conditions, The program adds a new user.
    If one of the previous conditions is not met, the program sends a warning message about the problem.
    """
    global ya
    try:
        if new_pass.get() != "" and new_name.get().lower() != "":
            with open('json/user.json', 'r') as infile:
                data = json.load(infile)
                for x in data["user"]:
                    if x["username"] == new_name.get().lower():
                        ya = 1
                    else:
                        continue
                if ya == 1:
                    message = "This name is used, please choose another name"
                    incorrect(message)
                else:
                    data["user"].append({"username": new_name.get().lower(),
                                         "password": new_pass.get(), "books": [], "books number": 0})
                    with open('json/user.json', 'w') as outfile:
                        json.dump(data, outfile, ensure_ascii=False)
                        message = "Name successfully added"
                        incorrect(message)
        else:
            message = "Please fill in all fields"
            incorrect(message)
        ya = 0
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    e8.delete(0, 'end')
    e9.delete(0, 'end')


def delete_user():
    """
    The program searches for the username and deletes it along with its entire file
    In the absence of this name, the program sends a warning message
    """
    global ya, yb, yc
    try:
        with open('json/user.json', 'r') as infile:
            data = json.load(infile)
            for x in data["user"]:
                if x["username"] == del_user.get().lower():
                    ya = yb
                    yc = 1
                else:
                    yb += 1
                    continue
            if yc == 1:
                del data["user"][ya]
                with open('json/user.json', 'w') as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
                    message = "The deletion was successful"
                    incorrect(message)
            else:
                message = "Username does not exist. Please verify the username"
                incorrect(message)
        ya, yb, yc = 0, 0, 0
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    e10.delete(0, 'end')


def add_book():
    """
     This function checks two conditions.
      1-  Bookname does not exist before
      2-  All the new book fields er full
      3- The locker, column and row number, and number of books must be integer numbers
    If the new user meets conditions, The program adds the new book.
    If one of the previous conditions is not met, the program sends a warning message about the problem.
    """
    global ya
    try:
        if new_book.get() != "" and author_name.get() != "":
            try:
                with open('json/books.json', 'r') as infile:
                    data = json.load(infile)
                    for x in data["books"]:
                        if x["bookname"] == new_book.get().lower():
                            ya = 1
                        else:
                            continue
                    if ya == 1:
                        message = "This book was previously registered. You can delete the" \
                                  " book and re-register it again."
                        incorrect(message)
                    else:
                        data["books"].append({"bookname": new_book.get().lower(),
                                              "author": author_name.get().lower(),
                                              "locker": locker_num.get(),
                                              "col": Col_num.get(),
                                              "row": row_num.get(),
                                              "number": num_book.get()})
                        with open('json/books.json', 'w') as outfile:
                            json.dump(data, outfile, ensure_ascii=False)
                            message = "New book successfully added"
                            incorrect(message)
                ya = 0
            except Exception:
                message = "you should write Locker number, Column number, Row number and Number of books as integers"
                incorrect(message)
        else:
            message = "Please fill in all fields"
            incorrect(message)
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    e11.delete(0, 'end')
    e12.delete(0, 'end')
    e13.delete(0, 'end')
    e14.delete(0, 'end')
    e15.delete(0, 'end')
    e16.delete(0, 'end')


def delete_book():
    """
    The program searches for the book name in the library and deletes it.
    In the absence of this book name, the program sends a warning message
    """
    global ya, yb, yc
    try:
        with open('json/books.json', 'r') as infile:
            data = json.load(infile)
            for x in data["books"]:
                if x["bookname"] == del_book.get().lower():
                    ya = yb
                    yc = 1
                else:
                    yb += 1
                    continue
            if yc == 1:
                del data["books"][ya]
                with open('json/books.json', 'w') as outfile:
                    json.dump(data, outfile, ensure_ascii=False)
                    message = "The deletion was successful"
                    incorrect(message)
            else:
                message = "This book does not exist."
                incorrect(message)
        ya, yb, yc = 0, 0, 0
    except FileNotFoundError:
        message = "Some files is not found"
        incorrect(message)
    e17.delete(0, 'end')


ya, yb, yc = 0, 0, 0  # I used this veriable in functions

color1 = "#f4f3ee"
color2 = "#faf3dd"

top = Tk()
top.geometry("800x550")

# ------------ add title --------------

top.title("Easy Library")

# ---------------- add menu ---------------------

menubar = Menu(top)
file = Menu(menubar, tearoff=0)
file.add_command(label="Log out", command=log_out)

file.add_separator()

file.add_command(label="Exit", command=top.quit)

menubar.add_cascade(label="File", menu=file)

top.config(menu=menubar)

# ------------------ General buttons ------------

sbmitbtn1 = Button(top, text="Log in as user", command=user_pass, bg=color1)  # Log in as user button
sbmitbtn1.place(x=200, y=5)

sbmitbtn2 = Button(top, text="Log in as admin", command=admin_pass, bg=color1)  # Log in as admin button
sbmitbtn2.place(x=650, y=5)

sbmitbtn7 = Button(top, text="Log out", state=NORMAL, command=log_out, bg=color1, padx=10)  # log out button
sbmitbtn7.place(x=350, y=5)

sbmitbtn14 = Button(top, text="Exit", state=NORMAL, command=top.quit, bg=color1, padx=25)  # Exit button
sbmitbtn14.place(x=500, y=5)

sbmitbtn8 = Button(top, text="Patron status", state=DISABLED, command=abut, bg=color1)  # informasjon about user books
sbmitbtn8.place(x=50, y=5)

# -------------- labelframe1 / log in user --------------

labelframe1 = LabelFrame(top, text="Log in user", bg=color2)
labelframe1.place(width=300, height=90, x=7, y=40)

name = Label(top, text="Username", bg=color2)  # Username Label
name.place(x=10, y=60)

u_name = StringVar()  # writing field to Username
e1 = Entry(top, state=DISABLED, textvariable=u_name)
e1.place(x=90, y=60)

password = Label(top, text="Password", bg=color2)  # password Label
password.place(x=10, y=90)

passw = StringVar()  # writing field to password
e2 = Entry(top, state=DISABLED, textvariable=passw, show='*')
e2.place(x=90, y=90)

sbmitbtn3 = Button(top, text="Log in", state=DISABLED, command=check, bg=color1)
sbmitbtn3.place(x=250, y=63)  # check if password and username is correct

# -------------- labelframe2 / Looking for book --------------

labelframe2 = LabelFrame(top, text="Looking for book", bg=color2)
labelframe2.place(width=300, height=120, x=7, y=140)

search = Label(top, text="Enter the name of the book you are looking for", bg=color2)
search.place(x=30, y=160)

b_search = StringVar()
e3 = Entry(top, state=DISABLED, textvariable=b_search)
e3.place(x=90, y=193)

sbmitbtn4 = Button(top, text="Search", state=DISABLED, command=search_book, bg=color1)
sbmitbtn4.place(x=125, y=225)

# -------------- labelframe3 / Checking out a book --------------

labelframe3 = LabelFrame(top, text="Checking out", bg=color2)
labelframe3.place(width=300, height=120, x=7, y=265)

check = Label(top, text="Enter the name of the book you want to borrow", bg=color2)
check.place(x=22, y=285)

out_book = StringVar()
e4 = Entry(top, state=DISABLED, textvariable=out_book)
e4.place(x=90, y=318)

sbmitbtn5 = Button(top, text="Check out", state=DISABLED, command=check_out, bg=color1)
sbmitbtn5.place(x=120, y=348)

# -------------- labelframe4 / Checking in a book --------------

labelframe4 = LabelFrame(top, text="Checking in", bg=color2)
labelframe4.place(width=300, height=120, x=7, y=390)

return0 = Label(top, text="Enter the name of the book you want to return", bg=color2)
return0.place(x=22, y=410)

in_book = StringVar()
e5 = Entry(top, state=DISABLED, textvariable=in_book)
e5.place(x=90, y=443)

sbmitbtn6 = Button(top, text="Check in", state=DISABLED, command=check_in, bg=color1)
sbmitbtn6.place(x=125, y=476)

# -------------- labelframe5 / log in admin --------------

labelframe5 = LabelFrame(top, text="Log in admin", bg=color2)
labelframe5.place(width=475, height=90, x=315, y=40)

a_name = Label(top, text="Adminname", bg=color2)
a_name.place(x=450, y=55)

admin_name = StringVar()
e6 = Entry(top, state=DISABLED, textvariable=admin_name)
e6.place(x=550, y=55)

password1 = Label(top, text="Password", bg=color2)
password1.place(x=450, y=88)

admin_pass = StringVar()
e7 = Entry(top, state=DISABLED, textvariable=admin_pass, show='*')
e7.place(x=550, y=88)

sbmitbtn9 = Button(top, text="Log in", state=DISABLED, command=check_admin, bg=color1)
sbmitbtn9.place(x=700, y=65)

# -------------- labelframe6 / Add new user --------------

labelframe6 = LabelFrame(top, text="Add new user", bg=color2)
labelframe6.place(width=230, height=245, x=315, y=140)

newname = Label(top, text="New Username", bg=color2)
newname.place(x=390, y=165)

new_name = StringVar()
e8 = Entry(top, state=DISABLED, textvariable=new_name)
e8.place(x=365, y=205)

newpassword = Label(top, text="Password", bg=color2)
newpassword.place(x=400, y=245)

new_pass = StringVar()
e9 = Entry(top, state=DISABLED, textvariable=new_pass)
e9.place(x=365, y=285)

sbmitbtn10 = Button(top, text="add new user", state=DISABLED, command=add_user, bg=color1)
sbmitbtn10.place(x=380, y=325)

# -------------- labelframe7 / Add new book --------------

labelframe7 = LabelFrame(top, text="Add new book", bg=color2)
labelframe7.place(width=240, height=245, x=550, y=140)

n_book = Label(top, text="Book's name", bg=color2)
n_book.place(x=555, y=165)

new_book = StringVar()
e11 = Entry(top, state=DISABLED, textvariable=new_book)
e11.place(x=655, y=165)

author = Label(top, text="Author name", bg=color2)
author.place(x=555, y=195)

author_name = StringVar()
e12 = Entry(top, state=DISABLED, textvariable=author_name)
e12.place(x=655, y=195)

locker = Label(top, text="Locker number", bg=color2)
locker.place(x=555, y=225)

locker_num = IntVar()
e13 = Entry(top, state=DISABLED, textvariable=locker_num)
e13.place(x=655, y=225)

Column_number = Label(top, text="Column number", bg=color2)
Column_number.place(x=555, y=255)

Col_num = IntVar()
e14 = Entry(top, state=DISABLED, textvariable=Col_num)
e14.place(x=655, y=255)

row_number = Label(top, text="Row number", bg=color2)
row_number.place(x=555, y=285)

row_num = IntVar()
e15 = Entry(top, state=DISABLED, textvariable=row_num)
e15.place(x=655, y=285)

number_book = Label(top, text="Number of books", bg=color2)
number_book.place(x=555, y=315)

num_book = IntVar()
e16 = Entry(top, state=DISABLED, textvariable=num_book)
e16.place(x=655, y=315)

sbmitbtn12 = Button(top, text="Add new book", state=DISABLED, command=add_book, bg=color1)
sbmitbtn12.place(x=630, y=345)

# -------------- labelframe8 / Delete a user --------------

labelframe8 = LabelFrame(top, text="Delete a user", bg=color2)
labelframe8.place(width=230, height=120, x=315, y=390)

deluser = Label(top, text="The user you want to delete", bg=color2)
deluser.place(x=350, y=410)

del_user = StringVar()
e10 = Entry(top, state=DISABLED, textvariable=del_user)
e10.place(x=370, y=440)

sbmitbtn11 = Button(top, text="Delete user", state=DISABLED, command=delete_user, bg=color1)
sbmitbtn11.place(x=395, y=470)

# -------------- labelframe9 / Delete a book --------------

labelframe9 = LabelFrame(top, text="Delete a book", bg=color2, )
labelframe9.place(width=240, height=120, x=550, y=390)

deletbook = Label(top, text="Book name", bg=color2)
deletbook.place(x=630, y=405)
del_book = StringVar()
e17 = Entry(top, state=DISABLED, textvariable=del_book)
e17.place(x=610, y=438)

sbmitbtn13 = Button(top, text="Delete a book", state=DISABLED, command=delete_book, bg=color1)
sbmitbtn13.place(x=625, y=470)

# -------------------- status bar ----------------------
status_bar = Label(top, anchor=N, text="Ihsan Tawila © Ehsan2ila91@gmail.com", bg="#e0fbfc", bd=3)
status_bar.pack(fill=X, side=BOTTOM)

top.configure(bg="#457b9d")
top.mainloop()

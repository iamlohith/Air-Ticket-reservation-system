# import modules
from tkinter import *
from tkinter.font import Font
from tkinter.ttk import Combobox
from airfunction import default
import random
import mysql.connector
import time
from mysql.connector import Error

# genrate ticket report
def gen():
    top4 = Toplevel()
    l1 = "REPORT"
    default(top4, l1)
    Label(top4, text="").pack()
    Label(top4, text="").pack()
    frame = Frame(top4)
    frame.pack()
    l1 = Label(frame, text=" enter TICKET NO", font=label_font)
    l1.grid(row=0, column=0)
    l2 = Label(frame, text="enter PASSPORT NO", font=label_font)
    l2.grid(row=0, column=1)
    l3 = Label(frame, text="AIRLINE NO", font=label_font)
    l3.grid(row=0, column=2)
    list1 = Listbox(frame, height=20, width=60)
    list1.grid(row=2, column=0, rowspan=15, columnspan=15)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="lohith",
        database="airregister"
    )
    mycursor = mydb.cursor()
    sql = "select * from ticket"
    mycursor.execute(sql)
    data = mycursor.fetchall()

    for val in data:
        list1.insert(END, ' {}                      {}                            {} '.format(*val))

# update user password
def updateuser():
    top2 = Toplevel()
    l1 = "ENTER THE DETAILS"
    default(top2, l1)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add2 = Label(top2, text="PASSPORT_NO", font=label_font, bg="#BCBCBE")
    add2.pack()
    entry2 = Entry(top2)
    entry2.pack()
    add3 = Label(top2, text="PASSWORD", font=label_font, bg="#BCBCBE")
    add3.pack()
    entry3 = Entry(top2)
    entry3.pack()

    def upu():
        no = str(entry2.get())
        pas = str(entry3.get())
        checkP = Label(top2, text="")
        checkP.pack()

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="lohith",
                database="airregister"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT passport FROM `user` WHERE `passport` =%s ",
                             (no,))
            if mycursor.fetchone() is not None:
                mycursor.execute("UPDATE  user SET password=%s WHERE passport=%s", (pas, no))
                mydb.commit()
                mydb.close()
                Label(top2, text="").pack()
                checkP.config(text="SUCCESSFULLY UPDATED", fg="green", font=label_font)
                top2.update()
                time.sleep(2)
                checkP.config(text="")
                clr()
            else:
                Label(top2, text="").pack()
                checkP.config(text="USERNAME NOT FOUND ON DATABASE", fg="red", font=label_font)
                top2.update()
                time.sleep(2)
                checkP.config(text="")
                clr()

        except Error as error:
            print(error)

        Label(top2, text="").pack()
        Label(top2, text="").pack()

    login1 = Button(top2, text="UPDATE", font=label_font, command=upu)
    login1.pack()

    def clr():

        entry3.delete(0, 'end')
        entry2.delete(0, 'end')


def update():
    top2 = Toplevel()
    l4 = 'SELECT YOUR CHOCIE'
    default(top2, l4)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add2 = Button(top2, text="UPDATE USER", font=label_font, width="20", height="2", command=updateuser)
    add2.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()

# delete user
def deluser():
    top2 = Toplevel()
    l1 = "ENTER THE DETAILS"
    default(top2, l1)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add1 = Label(top2, text="ENTER USER NAME", font=label_font, bg="#BCBCBE")
    add1.pack()
    entry1 = Entry(top2)
    entry1.pack()
    add2 = Label(top2, text="PASSPORT_NO", font=label_font, bg="#BCBCBE")
    add2.pack()
    entry2 = Entry(top2)
    entry2.pack()
    add3 = Label(top2, text="PASSWORD", font=label_font, bg="#BCBCBE")
    add3.pack()
    entry3 = Entry(top2)
    entry3.pack()

    def delu():
        no = str(entry2.get())
        checkP = Label(top2, text="")
        checkP.pack()

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="lohith",
                database="airregister"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT passport FROM `user` WHERE `passport` =%s ",
                             (no,))
            if mycursor.fetchone() is not None:
                mycursor.execute("DELETE FROM user WHERE passport=%s", (no,))
                mydb.commit()
                mydb.close()
                Label(top2, text="").pack()
                checkP.config(text="SUCCESSFULLY DELETED", fg="green", font=label_font)
                top2.update()
                time.sleep(2)
                checkP.config(text="")
                clr()
            else:
                Label(top2, text="").pack()
                checkP.config(text="USER NOT FOUND ON DATABASE", fg="red", font=label_font)
                top2.update()
                time.sleep(2)
                checkP.config(text="")
                clr()

        except Error as error:
            print(error)

        Label(top2, text="").pack()
        Label(top2, text="").pack()

    login1 = Button(top2, text="DELETE", font=label_font, command=delu)
    login1.pack()

    def clr():

        entry3.delete(0, 'end')
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')

# delete ticket
def delticket():
    top2 = Toplevel()
    l2 = 'ENTER THE DETAILS'
    default(top2, l2)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add1 = Label(top2, text=" ENTER TICKET NO", font=label_font, bg="#BCBCBE")
    add1.pack()
    entry1 = Entry(top2)
    entry1.pack()
    add2 = Label(top2, text="ENTER PASSPORT_NO", font=label_font, bg="#BCBCBE")
    add2.pack()
    entry2 = Entry(top2)
    entry2.pack()
    add3 = Label(top2, text="SELECT THE AIR no", font=label_font, bg="#BCBCBE")
    add3.pack()
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="lohith",
        database="airregister"
    )
    mycursor = mydb.cursor()
    sql = mycursor.execute("SELECT air_no FROM airline")
    v = mycursor.fetchall()
    entry3 = Combobox(top2, values=v, text="AIR NUMBER")
    entry3.pack()

    def delt():
        no = str(entry1.get())
        checkP = Label(top2, text="")
        checkP.pack()

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="lohith",
                database="airregister"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT ticket_no FROM `ticket` WHERE `ticket_no` =%s ",
                             (no,))
            if mycursor.fetchone() is not None:
                mycursor.execute("DELETE FROM ticket WHERE ticket_no=%s", (no,))
                mydb.commit()
                mydb.close()
                Label(top2, text="").pack()
                checkP.config(text="SUCCESSFULLY DELETED", fg="green", font=label_font)
                top2.update()
                time.sleep(2)
                checkP.config(text="")
                clr()
            else:
                Label(top2, text="").pack()
                checkP.config(text="TICKET NOT FOUND ON DATABASE", fg="red", font=label_font)
                top2.update()
                time.sleep(2)
                checkP.config(text="")
                clr()

        except Error as error:
            print(error)

        Label(top2, text="").pack()
        Label(top2, text="").pack()

    login1 = Button(top2, text="DELETE", font=label_font, command=delt)
    login1.pack()

    def clr():

        entry3.delete(0, 'end')

# delete airline
def delairline():
    top1 = Toplevel()
    l3 = 'ENTER THE DETAILS'
    default(top1, l3)
    Label(top1, text="").pack()
    Label(top1, text="").pack()
    add3 = Label(top1, text="AIRLINE NO", font=label_font, bg="#BCBCBE")
    add3.pack()
    entry3 = Entry(top1)
    entry3.pack()

    def dela():
        no = str(entry3.get())
        checkP = Label(top1, text="")
        checkP.pack()

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="lohith",
                database="airregister"
            )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT air_no FROM `airline` WHERE `air_no` =%s ",
                             (no,))
            if mycursor.fetchone() is not None:
                mycursor.execute("DELETE FROM airline WHERE air_no=%s", (no,))
                mydb.commit()
                mydb.close()
                Label(top1, text="").pack()
                checkP.config(text="SUCCESSFULLY DELETED", fg="green", font=label_font)
                top1.update()
                time.sleep(2)
                checkP.config(text="")
                clr()
            else:
                Label(top1, text="").pack()
                checkP.config(text="AIRLINE NOT FOUND ON DATABASE", fg="red", font=label_font)
                top1.update()
                time.sleep(2)
                checkP.config(text="")
                clr()

        except Error as error:
            print(error)

        Label(top1, text="").pack()
        Label(top1, text="").pack()

    login1 = Button(top1, text="DELETE", font=label_font, command=dela)
    login1.pack()

    def clr():

        entry3.delete(0, 'end')

# delete option
def delete():
    top2 = Toplevel()
    l4 = 'SELECT YOUR CHOCIE'
    default(top2, l4)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add1 = Button(top2, text="CANCEL TICKET", font=label_font, width="20", height="2", command=delticket)
    add1.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add2 = Button(top2, text="DELETE USER", font=label_font, width="20", height="2", command=deluser)
    add2.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add3 = Button(top2, text="DELETE AIRLINE", font=label_font, width="20", height="2", command=delairline)
    add3.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()

# add user
def adduser():
    top2 = Toplevel()
    l1 = "ENTER THE DETAILS"
    default(top2, l1)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add1 = Label(top2, text="ENTER USER NAME", font=label_font, bg="#BCBCBE")
    add1.pack()
    entry1 = Entry(top2)
    entry1.pack()
    add2 = Label(top2, text="PASSPORT_NO", font=label_font, bg="#BCBCBE")
    add2.pack()
    entry2 = Entry(top2)
    entry2.pack()
    add3 = Label(top2, text="PASSWORD", font=label_font, bg="#BCBCBE")
    add3.pack()
    entry3 = Entry(top2)
    entry3.pack()

    def addu():
        pas = str(entry2.get())
        password = str(entry3.get())
        name = str(entry1.get())
        checkP = Label(top2, text="")
        checkP.pack()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="lohith",
            database="airregister"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            ''' INSERT INTO user (name,passport,password) VALUES (%s,%s,%s)''',
            (name, pas, password))
        mydb.commit()
        mydb.close()
        checkP.config(text="USER SUCCESSFULLY ADDED ", fg="green", font=label_font)
        top2.update()
        time.sleep(2)
        checkP.config(text="")
        clr()

    b2 = Button(top2, text="SUBMIT", font=label_font, bg="#BCBCBE", command=addu)
    b2.pack()

    def clr():
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')

# add ticket
def addticket():
    global ran
    top2 = Toplevel()
    l2 = 'ENTER THE DETAILS'
    default(top2, l2)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add1 = Label(top2, text="TICKET NO", font=label_font, bg="#BCBCBE")
    add1.pack()
    s1 = StringVar()
    for x in range(1):
        ran = random.randint(100000, 999999)
    entry1 = Entry(top2, textvariable=s1, state=DISABLED)
    s1.set(ran)
    entry1.pack()
    add2 = Label(top2, text="PASSPORT_NO", font=label_font, bg="#BCBCBE")
    add2.pack()
    entry2 = Entry(top2)
    entry2.pack()
    add4 = Label(top2, text="ENTER THE NO SEATS ", font=label_font, bg="#BCBCBE")
    add4.pack()
    entry4 = Entry(top2)
    entry4.pack()
    air = Label(top2, text="SELECT THE AIR NO", font=label_font, bg="#BCBCBE")
    air.pack()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="lohith",
        database="airregister"
    )
    mycursor = mydb.cursor()
    sql = mycursor.execute("SELECT air_no FROM airline")
    v = mycursor.fetchall()
    entry3 = Combobox(top2, values=v, text="AIR NUMBER")
    entry3.pack()

    def addt():
        pas = str(entry2.get())
        a = str(entry3.get())
        seat = int(entry4.get())
        checkP = Label(top2, text="")
        checkP.pack()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="lohith",
            database="airregister"
        )
        mycursor = mydb.cursor()
        sql1 = mycursor.execute(" SELECT COUNT(`ticket_no`) from `ticket` WHERE air_no=%s", (a,))
        s1 = mycursor.fetchone()
        mydb.close()
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="lohith",
            database="airregister"
        )
        mycursor = mydb.cursor()
        sql2 = mycursor.execute(" SELECT `air_seat` from `airline` WHERE air_no=%s", (a,))
        s = mycursor.fetchone()
        a1 = []
        for i in s:
            a1.append(i)
        b = a1[0]
        print(b)

        d = 0
        c = 0
        c = seat
        print(c)
        d = b - c
        if d > 0:

            mycursor.execute(
                ''' INSERT INTO ticket (ticket_no,passport_no,air_no) VALUES (%s,%s,%s)''',
                (ran, pas, a))
            mycursor.execute("UPDATE  airline SET air_seat=%s WHERE air_no=%s", (d, a))
            mydb.commit()
            mydb.close()
            checkP.config(text="TICKET SUCCESSFULLY ADDED ", fg="green", font=label_font)
            top2.update()
            time.sleep(2)
            checkP.config(text="")
            clr()
        else:
            checkP.config(text="TICKETS ARE FULL ", fg="green", font=label_font)
            top2.update()
            time.sleep(2)
            checkP.config(text="")
            clr()

    b2 = Button(top2, text="SUBMIT", font=label_font, bg="#BCBCBE", command=addt)
    b2.pack()

    def clr():
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')

# add airline to database


def addairline():
    top1 = Toplevel()
    l3 = 'ENTER THE DETAILS'
    default(top1, l3)
    Label(top1, text="").pack()
    Label(top1, text="").pack()

    add3 = Label(top1, text="AIRLINE NO", font=label_font, bg="#BCBCBE")
    add3.pack()
    entry3 = Entry(top1)
    entry3.pack()
    add2 = Label(top1, text="AIRLINE NAME", font=label_font, bg="#BCBCBE")
    add2.pack()
    entry2 = Entry(top1)
    entry2.pack()
    add1 = Label(top1, text="SEATS AVAIABLE", font=label_font, bg="#BCBCBE")
    add1.pack()
    entry1 = Entry(top1)
    entry1.pack()

    def adda():
        no = str(entry3.get())
        name = str(entry2.get())
        seat = str(entry1.get())
        checkP = Label(top1, text="")
        checkP.pack()

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="lohith",
            database="airregister"
        )
        mycursor = mydb.cursor()
        mycursor.execute(
            ''' INSERT INTO airline (air_name,air_seat,air_no) VALUES (%s,%s,%s)''',
            (name, seat, no))
        mydb.commit()
        mydb.close()
        checkP.config(text="AIRLINE  SUCCESSFULLY ADDED ", fg="green", font=label_font)
        top1.update()
        time.sleep(2)
        checkP.config(text="")
        clr()

    b2 = Button(top1, text="SUBMIT", font=label_font, bg="#BCBCBE", command=adda)
    b2.pack()

    def clr():
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')

# add option
def add():
    top2 = Toplevel()
    l4 = 'SELECT YOUR CHOCIE'
    default(top2, l4)
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add1 = Button(top2, text="ADD TICKET", font=label_font, width="20", height="2", command=addticket)
    add1.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add2 = Button(top2, text="ADD USER", font=label_font, width="20", height="2", command=adduser)
    add2.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()
    add3 = Button(top2, text="ADD AIRLINE", font=label_font, width="20", height="2", command=addairline)
    add3.pack()
    Label(top2, text="").pack()
    Label(top2, text="").pack()

# main window
root = Tk()
label_font = Font(family="Bold", size=13)
head_font = Font(family="Times New Roman", size=30)
win_font = Font(family="Arial", size=20)
l = 'SELECT YOUR CHOICE'
default(root, l)
Label(root, text="").pack()
Label(root, text="").pack()
login = Button(root, text="ADD", font=label_font, width="20", height="2", command=add).pack()
Label(text="").pack()
Label(text="").pack()
register = Button(root, text="DELETE", font=label_font, width="20", height="2", command=delete).pack()
Label(text="").pack()
Label(text="").pack()
gen = Button(root, text="GENRATE REPORT", font=label_font, width="20", height="2", command=gen).pack()
Label(text="").pack()
Label(text="").pack()
update = Button(root, text="UPDATE", font=label_font, width="20", height="2", command=update).pack()
root.mainloop()

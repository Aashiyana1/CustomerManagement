from tkinter import *
from tkinter import ttk
import sqlite3
import datetime

def add_customer():
    r = e_id.get()
    n = e_name.get()
    e = e_email.get()
    m = e_mobile.get()
    prod_name = e_prod_name.get()
    prod_price =e_prod_price.get()
    time= datetime.datetime.now()
    d = e_dob.get()
    a = t_address.get("1.0",END)

    conn = sqlite3.connect('customerdatabase.db')
    c = conn.cursor()
    c.execute('INSERT INTO customer VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?)' , (r, n, e, m, prod_name,prod_price,time, d, a))
    conn.commit()
    conn.close()

    show_all()

    clear_all()

def show_all():
    e_search.delete(0, END)
    conn = sqlite3.connect('customerdatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM customer')
    customer_table.delete(*customer_table.get_children())
    for r in c:
        customer_table.insert("", "end", values=r)
    conn.commit()
    conn.close()

def clear_all():
    e_id.delete(0, END)
    e_name.delete(0, END)
    e_email.delete(0, END)
    e_mobile.delete(0, END)
    e_prod_name.delete(0, END)
    e_prod_price.delete(0, END)
    e_dob.delete(0, END)
    t_address.delete(1.0, END)


def get_data(event):
    current = customer_table.item(customer_table.focus())
    row = current["values"] #focussed row stored in current as a dictionary

    clear_all()

    e_id.insert(0, row[0])
    e_name.insert(0, row[1])
    e_email.insert(0, row[2])
    e_mobile.insert(0, row[3])
    e_prod_name.insert(0, row[4])
    e_prod_price.insert(0, row[5])
    e_dob.insert(0, row[7])
    t_address.insert(1.0, row[8])
    

    
def update_customer():
    n = e_name.get()
    e = e_email.get()
    m = e_mobile.get()
    prod_name = e_prod_name.get()
    prod_price = e_prod_price.get()
    time  = datetime.datetime.now()
    u = e_dob.get()
    a = t_address.get("1.0",END)
    r = e_id.get()
    
    
    conn = sqlite3.connect('customerdatabase.db')
    c = conn.cursor()
    c.execute('UPDATE customer SET name= ?, email = ? , mobile = ?, prod_name= ? ,prod_price= ?, time= ?, dob= ?, address= ? WHERE id= ?' , (n,e,m,prod_name,prod_price,time,u,a,r))
    conn.commit()
    conn.close()
    show_all()
    clear_all()

def delete_customer():
    r = e_id.get()
    
    conn = sqlite3.connect('customerdatabase.db')
    c = conn.cursor()
    c.execute('DELETE FROM customer WHERE id = ?' , (r,) )
    conn.commit()
    conn.close()
    show_all()
    clear_all()

def search_customer():
    s = c_search.get()
    key = e_search.get()

    conn = sqlite3.connect('customerdatabase.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customer WHERE "+s+"= ?", (key,))
    customer_table.delete(*customer_table.get_children())
    for r in c:
            customer_table.insert("", "end", values=r)
    conn.commit()
    conn.close()
    
    
master = Tk()
master.title('Customer Management System')
master.geometry('1400x900')


title = Label(master, text="Customer Management System", font=("Roman",40,"bold"), bg="crimson", fg="white", bd=7, relief=GROOVE)
title.pack(side=TOP, fill=X)

left_frame = Frame(master, bg="crimson", bd=4, relief=RIDGE)
left_frame.place(x=20, y=90, width=550, height=700)

left_frame_title = Label(left_frame, text="Manage Customer", font=("Calibri",30,"bold"), bg="white", fg="crimson", bd=4, relief=GROOVE)
left_frame_title.pack(side=TOP, fill=X)

l_id = Label(left_frame, text="ID.", font=("Calibri",25,"bold"), fg="white", bg="crimson") #why bg
l_id.place(x=20, y=60)
e_id = Entry(left_frame, font=("Calibri",18))
e_id.place(x=230, y=70)

l_name = Label(left_frame, text="Name", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_name.place(x=20, y=110)
e_name = Entry(left_frame, font=("Calibri",18))
e_name.place(x=230, y=120)

l_email = Label(left_frame, text="Email", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_email.place(x=20, y=160)
e_email = Entry(left_frame, font=("Calibri",18))
e_email.place(x=230, y=170)

l_mobile = Label(left_frame, text="Mobile", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_mobile.place(x=20, y=215)
e_mobile = Entry(left_frame, font=("Calibri",18))
e_mobile.place(x=230, y=220)

l_prod_name = Label(left_frame, text="Product Name", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_prod_name.place(x=20, y=265)
e_prod_name = Entry(left_frame, font=("Calibri",18))
e_prod_name.place(x=230, y=270)

l_prod_price = Label(left_frame, text="Product Price", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_prod_price.place(x=20, y=310)
e_prod_price = Entry(left_frame, font=("Calibri",18))
e_prod_price.place(x=230, y=320)

l_dob1 = Label(left_frame, text="DOB", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_dob1.place(x=20, y=370)
l_dob2 = Label(left_frame, text="(dd/mm/yyyy)", font=("Calibri",20), fg="white", bg="crimson")
l_dob2.place(x=20, y=410)
e_dob = Entry(left_frame, font=("Calibri",18))
e_dob.place(x=230, y=390)

l_address = Label(left_frame, text="Address", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_address.place(x=20, y=460)
t_address = Text(left_frame, font=("Calibri",18), width=20, height=3)
t_address.place(x=230, y=460)



b_add = Button(left_frame, text='Add', width=8, height=1, command=add_customer)
b_add.place(x=130, y=585)

b_update = Button(left_frame, text='Update', width=8, height=1, command=update_customer)
b_update.place(x=230, y=585)

b_delete = Button(left_frame, text='Delete', width=8, height=1, command=delete_customer)
b_delete.place(x=330, y=585)

right_frame = Frame(master, bg="crimson", bd=4, relief=RIDGE)
right_frame.place(x=590, y=90, width=750, height=700)

l_search = Label(right_frame, text="Search by", font=("Calibri",25,"bold"), fg="white", bg="crimson")
l_search.place(x=11, y=8)
c_search = ttk.Combobox(right_frame, width=7, font=("Calibri",15), state='readonly')
c_search["values"] = ("id","name","mobile")
c_search.current(0)
c_search.place(x=170, y=18)
e_search = Entry(right_frame, font=("Calibri",16), width=10)
e_search.place(x=280, y=18)
b_search = Button(right_frame, text="Search", font=("Calibri",13), width=7, command=search_customer)
b_search.place(x=420, y=16)
b_showall = Button(right_frame, text="Show All", font=("Calibri",13), width=7, command=show_all)
b_showall.place(x=520, y=16)

table_frame = Frame(right_frame, bg="crimson", bd=4, relief=RIDGE)
table_frame.place(x=20, y=70, width=720, height=500)

hs = Scrollbar(table_frame, orient=HORIZONTAL)
hs.pack(side=BOTTOM, fill=X)
vs = Scrollbar(table_frame, orient=VERTICAL)
vs.pack(side=RIGHT, fill=Y)
customer_table = ttk.Treeview(table_frame, columns=("r", "n", "e", "m","prod_name","prod_price","time", "d", "a"))
hs.config(command=customer_table.xview)
vs.config(command=customer_table.yview)

customer_table.heading("r", text="ID.")
customer_table.heading("n", text="Name")
customer_table.heading("e", text="Email ID")
customer_table.heading("m", text="Mobile")
customer_table.heading("prod_name", text="prod name")
customer_table.heading("prod_price", text="price")
customer_table.heading("time", text="time")

customer_table.heading("d", text="DOB")
customer_table.heading("a", text="Address")
customer_table["show"] = "headings"
#shows only those columns in which headings are present, does not show the default index column.
customer_table.pack(fill=Y, expand=1)
#customer_table.pack(fill=BOTH, expand=1)
customer_table.column("r", width=30)
customer_table.column("n", width=100)
customer_table.column("e", width=150)
customer_table.column("m", width=100)
customer_table.column("prod_name", width=100)
customer_table.column("prod_price", width=75)
customer_table.column("time", width=75)
customer_table.column("d", width=90)
customer_table.column("a", width=180)
customer_table["show"] = "headings"
customer_table.bind("<ButtonRelease-1>", get_data)

try:
    conn = sqlite3.connect('customerdatabase.db')
    c = conn.cursor()
    c.execute('CREATE TABLE customer (id CHAR(3), name VARCHAR(20), email VARCHAR(20), mobile CHAR(10),prod_name varchar(30),prod_price varchar(30),time varchar(30), dob CHAR(10), address VARCHAR(30))')
    conn.commit()
    conn.close()
except sqlite3.OperationalError:
    pass

master.mainloop()



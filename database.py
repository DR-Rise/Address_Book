from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk()
root.title('Address Book')
root.iconbitmap("img/icon.ico")
root.geometry("360x600")

#Databases

#Create a database or connect to one
conn = sqlite3.connect('address_book.db')

#Create cursor
c = conn.cursor()

#Create table
c.execute("""CREATE TABLE IF NOT EXISTS addressess (
        first_name text,
        last_name text,
        nationality text,
        number text,
        address text,
        zipcode interger
        )""")


#Create submit function

def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    # Insert Into Tale
    c.execute("INSERT INTO addressess VALUES (:f_name, :l_name, :natio, :num, :add, :zipco)",
              {
                  'f_name':f_name.get(),
                  'l_name': l_name.get(),
                  'natio': natio.get(),
                  'num': num.get(),
                  'add': add.get(),
                  'zipco': zipco.get()
              })

    conn.commit()
    conn.close()

    #Clear The Text Boxes
    f_name.delete(0,END)
    l_name.delete(0, END)
    natio.delete(0, END)
    num.delete(0, END)
    add.delete(0, END)
    zipco.delete(0, END)


#Create Query Function
def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT oid,* FROM addressess")
    records = c.fetchall()

    #Loop Thru Results
    str_records = ''
    for record in records:
        str_records += str(record) +"\n"

    query_label = Label(root, text=str_records)
    query_label.grid(row=8, column=0, columnspan=2 , pady=20)

    conn.commit()
    conn.close()



#Create TExt Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

natio = Entry(root, width=30)
natio.grid(row=2, column=1)

num = Entry(root, width=30)
num.grid(row=3, column=1)

add = Entry(root, width=30)
add.grid(row=4, column=1)

zipco = Entry(root, width=30)
zipco.grid(row=5, column=1)

# Create Text Box Labels
f_name_label = Label(root, text="First Name ").grid(row=0, column=0)
l_name_label = Label(root, text="Last Name ").grid(row=1, column=0)
natio_label = Label(root, text="nationality ").grid(row=2, column=0)
num_label = Label(root, text="Phone number ").grid(row=3, column=0)
add_label = Label(root, text="Address ").grid(row=4, column=0)
zipco_label = Label(root, text="Zipe Code ").grid(row=5, column=0)



#Create Submit Button
Submit_btn = Button(root,text="Add Record to Database",command=submit)
Submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#Create Query Button
query_Button = Button(root,text="Show Records", fg="Blue", command=query)
query_Button.grid(row=7,column=0,columnspan=2, pady=10, padx=10, ipadx=100)

#Comit Changes
conn.commit()

#Close Connection
conn.close()

root.mainloop()
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import mysql.connector as mysql


def openTeacherWindow():

    def displayStudentList():
        con = mysql.connect( host = 'localhost' , user = 'root' , password = '' , database = 'readydb')
        cur = con.cursor()
        cur.execute("select * from Student")
        sd = cur.fetchall()

        for s in sd:
            insertData = str(s[0])+ '    '+ str(s[1])
            list.insert(list.size()+1, insertData)

        con.close()

    def addStudent():
        sname = e_name.get()
        srno = e_rno.get()

        if(sname == '' or srno == ''):
            mbox.showinfo('Alert', 'Please enter both name and roll number')
        else:
            con = mysql.connect( host = 'localhost' , user = 'root' , password = '' , database = 'readydb')
            cur = con.cursor()
            cur.execute("insert into student values('"+ sname +"','"+srno+"')")
            cur.execute('commit')

            e_name.delete(0, 'end')
            e_rno.delete(0, 'end')
            mbox.showinfo('add student','Student inserted successfully')
            con.close()

    teachwindow = Toplevel(a)
    teachwindow.title('Teacher Login')
    teachwindow.geometry('500x500')
    teachwindow['bg']='LemonChiffon3'

    lb1 = Label(teachwindow, text = 'To add new student, Enter student name and roll number and click on Add,',font=('bold', 12))
    lb1.place(x=20 ,y=30)

    name = Label(teachwindow, text = 'Name',font=('bold', 12))
    name.place(x=20,y=60)

    rno = Label(teachwindow, text = 'Roll Number',font=('bold', 12))
    rno.place(x=20,y=90)

    e_name = Entry(teachwindow)
    e_name.place(x=200,y=60)
    e_rno = Entry(teachwindow)
    e_rno.place(x=200,y=90)

    Add = Button(teachwindow, text = "Add Student", font=('bold',10), bg='white', command = addStudent)
    Add.place(x=140,y=140)

    stdlist = Button(teachwindow, text = "Student List", font=('bold',10), bg='white', command = displayStudentList)
    stdlist.place(x=20,y=200)

    list = Listbox(teachwindow)
    list.place(x=200 , y=200)
    
def login():
    ID = e_id.get()
    Pas = e_pas.get()

    if(ID == '' or Pas == ''):
        mbox.showinfo('Alert', 'Please enter both id and password')

    else:
        con = mysql.connect( host = 'localhost' , user = 'root' , password = '' , database = 'readydb')
        ID = e_id.get()
        Pas = e_pas.get()
        cur = con.cursor()
        cur.execute("select tid,tpass  from teachers where tid= "+ID+" ")
        t=cur.fetchall()
        for row in t:
            x=row[0]
            y=row[1]
            
        if ID == str(x) and Pas == y :
            login = True
                #break
        else:
            login = False
        
        e_id.delete(0, 'end')
        e_pas.delete(0, 'end')
            
        if login == True:
            mbox.showinfo('Alert', 'Login Succesful')
            openTeacherWindow()

        else:
            mbox.showinfo('Alert', 'Invalid ID or Password')
        con.close()

def displayNotes():
    noteswindow = Toplevel(a)
    noteswindow.title('Notes')
    noteswindow.geometry('400x400')
    noteswindow['bg']='PaleTurquoise3'

    lb3 = Label(noteswindow, text = 'All Subjects notes is given here',font=('bold', 12))
    lb3.place(x=20 ,y=30)

    nS = tk.Scrollbar(noteswindow)
    nT = tk.Text(noteswindow, height = 200, width = 200)
    nS.pack(side=tk.RIGHT, fill=tk.Y)
    nT.pack(side=tk.LEFT, fill=tk.Y)
    nS.config(command= nT.yview)
    nT.config(yscrollcommand= nS.set)

    con = mysql.connect( host = 'localhost' , user = 'root' , password = '' , database = 'readydb')
    cur = con.cursor()
    cur.execute("select * from notes")
    notes = cur.fetchall()
    nT.insert(tk.END, notes)


    con.close()

def displayAss():
    asswindow = Toplevel(a)
    asswindow.title('Assignments')
    asswindow.geometry('220x200')
    asswindow['bg']='SlateGray2'

    lb4 = Label(asswindow, text = 'All Subjects assignments are given here',font=('bold', 12))
    lb4.place(x=20 ,y=30)

    aS = tk.Scrollbar(asswindow)
    aT = tk.Text(asswindow, height = 200, width = 200)
    aS.pack(side=tk.RIGHT, fill=tk.Y)
    aT.pack(side=tk.LEFT, fill=tk.Y)
    aS.config(command= aT.yview)
    aT.config(yscrollcommand= aS.set)

    con = mysql.connect( host = 'localhost' , user = 'root' , password = '' , database = 'readydb')
    cur = con.cursor()
    cur.execute("select * from assignments")
    ass = cur.fetchall()
    aT.insert(tk.END, ass)
    

    con.close()

def displayGrades():    
    gradeswindow = Toplevel(a)
    gradeswindow.title('Grades')
    gradeswindow.geometry('220x200')
    gradeswindow['bg']='light steel blue'

    lb5 = Label(gradeswindow, text = 'All Students grades are given here',font=('bold', 12))
    lb5.place(x=20 ,y=30)

    gS = tk.Scrollbar(gradeswindow)
    gT = tk.Text(gradeswindow, height = 200, width = 200)
    gS.pack(side=tk.RIGHT, fill=tk.Y)
    gT.pack(side=tk.LEFT, fill=tk.Y)
    gS.config(command= gT.yview)
    gT.config(yscrollcommand= gS.set)

    con = mysql.connect( host = 'localhost' , user = 'root' , password = '' , database = 'readydb')
    cur = con.cursor()
    cur.execute("select * from grades")
    grades = cur.fetchall()

    gT.insert(tk.END, grades)
    '''for grade in grades:
        insertData3 = str(grade[0])+ '    '+ str(grade[1] +'    '+ str(grade[3]))
        listG.insert(listG.size()+1, insertData3)'''

    con.close()


a = Tk()
a.geometry('500x500')
a.title('Home Class')
a.configure(bg='#49A')

lb = Label(a, text = 'To add new student, Please Login here',font=('bold', 12))
lb.place(x=20 ,y=30)

id = Label(a, text = 'Enter Teacher ID',font=('bold', 12))
id.place(x=20,y=60)

pas = Label(a, text = 'Enter Password',font=('bold', 12))
pas.place(x=20,y=90)

e_id = Entry()
e_id.place(x=200,y=60)

e_pas = Entry()
e_pas.place(x=200,y=90)

lg = Button(a, text = "Login", font=('bold',10), bg='white', command = login)
lg.place(x=140,y=140)

lb2 = Label(a, text = 'Students can refer Notes, Assignments and Grades here',font=('bold', 12))
lb2.place(x=20 ,y=200)

N = Button(a, text = "Notes", font=('bold',10), bg='white', command = displayNotes)
N.place(x=200,y=230)

A = Button(a, text = "Assignments", font=('bold',10), bg='white', command = displayAss)
A.place(x=200,y=260)

G = Button(a, text = "Grades", font=('bold',10), bg='white', command = displayGrades)
G.place(x=200,y=290)


a.mainloop()

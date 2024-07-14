from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
win = Tk()
win.state('zoomed')
win.config(bg='black')
#=================================Button function =====================
def pd():
    if e1.get()=="" or e2.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        con=mysql.connector.connect(host="localhost",username="root",password="Ravi$9708985194",database="mydata")
        my_cursor =con.cursor()
        my_cursor.execute("insert into hospital value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
            nameoftablets.get(),
            ref.get(),
            dose.get(),
            nooftablets.get(),
            lot.get(),
            issuedate.get(),
            expdate.get(),
            dailydose.get(),
            sideeffect.get(),
            furtherinformation.get(),
            bloodpressure.get(),
            storageadvice.get(),
            medication.get(),
            patientid.get(),
            nhsnumbers.get(),
            patientname.get(),
            dateofbirth.get(),
            patientaddress.get()
        ))
        con.commit()
        fetch_data() 
        con.close()
        messagebox.showinfo("Success","Record has been inserted")

def fetch_data():
    con=mysql.connector.connect(host="localhost",username="root",password="Ravi$9708985194",database="mydata")
    my_cursor =con.cursor()
    my_cursor.execute('select * from hospital')
    rows = my_cursor.fetchall()
    if len(rows)!=0:
        table.delete(* table.get_children())
        for items in rows:
            table.insert('',END,values=items)
        con.commit()
    con.close()

def get_data(event=''):
    cursor_row=table.focus()
    data =table.item(cursor_row)
    row = data['values']
    nameoftablets.set(row[0])
    ref.set(row[1])
    dose.set(row[2])
    nooftablets.set(row[3])
    lot.set(row[4])
    issuedate.set(set(row[5]))
    expdate.set(row[6])
    dailydose.set(row[7])
    sideeffect.set(row[8])
    furtherinformation.set(row[9])
    bloodpressure.set(row[10])
    storageadvice.set(row[11])
    medication.set(row[12])
    patientid.set(row[13])
    nhsnumbers.set(row[14])
    patientname.set(row[15])
    dateofbirth.set(row[16])
    patientaddress.set(row[17])

#~~~~~~~~~~~~~~~~~~~~prescription data~~~~~~~~~~~~
def pre():
    txt_frame.insert(END,'Name of Tablets:\t\t\t'+nameoftablets.get()+'\n')
    txt_frame.insert(END,'Reference :\t\t\t'+ref.get()+'\n')
    txt_frame.insert(END,'Dose:\t\t\t'+dose.get()+'\n')
    txt_frame.insert(END,'No.of Tablets:\t\t\t'+nooftablets.get()+'\n')
    txt_frame.insert(END,'Lot:\t\t\t'+lot.get()+'\n')
    txt_frame.insert(END,'Issue Date:\t\t\t'+issuedate.get()+'\n')
    txt_frame.insert(END,'Exp. Date:\t\t\t'+expdate.get()+'\n')
    txt_frame.insert(END,'Daily Dose:\t\t\t'+dailydose.get()+'\n')
    txt_frame.insert(END,'Side Effect:\t\t\t'+sideeffect.get()+'\n')
    txt_frame.insert(END,'Further Information:\t\t\t'+furtherinformation.get()+'\n')
    txt_frame.insert(END,'Blood Pressure:\t\t\t'+bloodpressure.get()+'\n')
    txt_frame.insert(END,'Storage Advice:\t\t\t'+storageadvice.get()+'\n')
    txt_frame.insert(END,'Medication:\t\t\t'+medication.get()+'\n')
    txt_frame.insert(END,'Patient Id:\t\t\t'+patientid.get()+'\n')
    txt_frame.insert(END,'NHS Numbers:\t\t\t'+nhsnumbers.get()+'\n')
    txt_frame.insert(END,'Patient Name:\t\t\t'+patientname.get()+'\n')
    txt_frame.insert(END,'Date of Birth:\t\t\t'+dateofbirth.get()+'\n')
    txt_frame.insert(END,'Patient Address:\t\t\t'+patientaddress.get()+'\n')

#==========Delete Button===================
def delete():
    con=mysql.connector.connect(host="localhost",username="root",password="Ravi$9708985194",database="mydata")
    my_cursor =con.cursor()
    querry = ('delete from hospital where Reference = %s')
    value=(ref.get(),)
    my_cursor.execute(querry,value)
    con.commit()
    con.close()
    fetch_data()
    messagebox.showinfo('Deleted','Patient data has been deleted')
#======================clear button================
def clear():
    nameoftablets.set('')
    ref.set('')
    dose.set('')
    nooftablets.set('')
    lot.set('')
    issuedate.set('')
    expdate.set('')
    dailydose.set('')
    sideeffect.set('')
    furtherinformation.set('')
    bloodpressure.set('')
    storageadvice.set('')
    medication.set('')
    patientid.set('')
    nhsnumbers.set('')
    patientname.set('')
    nhsnumbers.set('')
    patientname.set('')
    dateofbirth.set('')
    patientaddress.set('')
    txt_frame.delete(1.0,END)

#===================Exits Button================================
def exit():
    confirm = messagebox.askyesno('confirmatiion','Are you sure you want to Exit')
    if confirm >0:
        win.destroy()
        return

#heading
Label(win,text='Hospital Management System',font='impack 31 bold',bg='red',fg='white').pack(fill=X)

#frame1
frame1 = Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1280,height=310)

#label frame for patient info.
lf1 =LabelFrame(frame1,text='Patient Information',font='ariel 10 bold',bd=10)
lf1.place(x=10,y=0,width=750,height=280)
#labels for patient information
Label(lf1,text='Name of Tablets').place(x=5,y=10)
Label(lf1,text='Reference').place(x=5,y=36)
Label(lf1,text='Dose').place(x=5,y=62)
Label(lf1,text='No.of Tablets').place(x=5,y=88)
Label(lf1,text='Lot').place(x=5,y=114)
Label(lf1,text='Issue Date').place(x=5,y=140)
Label(lf1,text='Exp. Date').place(x=5,y=166)
Label(lf1,text='Daily Dose').place(x=5,y=192)
Label(lf1,text='Side Effect').place(x=5,y=218)
Label(lf1,text='Further Information').place(x=370,y=10)
Label(lf1,text='Blood Pressure').place(x=370,y=36)
Label(lf1,text='Storage Advice').place(x=370,y=66)
Label(lf1,text='Medication').place(x=370,y=88)
Label(lf1,text='Patient Id').place(x=370,y=114)
Label(lf1,text='NHS Numbers').place(x=370,y=140)
Label(lf1,text='Patient Name').place(x=370,y=166)
Label(lf1,text='Date of Birth').place(x=370,y=192)
Label(lf1,text='Patient Address').place(x=370,y=218)
#TextVariable for Every Entry field
nameoftablets=StringVar()
ref=StringVar()
dose =StringVar()
nooftablets=StringVar()
lot=StringVar()
issuedate=StringVar()
expdate=StringVar()
dailydose=StringVar()
sideeffect=StringVar()
furtherinformation=StringVar()
bloodpressure=StringVar()
storageadvice=StringVar()
medication=StringVar()
patientid=StringVar()
nhsnumbers=StringVar()
patientname=StringVar()
dateofbirth=StringVar()
patientaddress=StringVar()

#ENTRY field for all labels
e1 = Entry(lf1,bd=4,textvariable=nameoftablets)
e1.place(x=130,y=10,width=200)
e2 = Entry(lf1,bd=4,textvariable=ref)
e2.place(x=130,y=36,width=200)
e3 = Entry(lf1,bd=4,textvariable=dose)
e3.place(x=130,y=62,width=200)
e4 = Entry(lf1,bd=4,textvariable=nooftablets)
e4.place(x=130,y=88,width=200)
e5 = Entry(lf1,bd=4,textvariable=lot)
e5.place(x=130,y=114,width=200)
e6 = Entry(lf1,bd=4,textvariable=issuedate)
e6.place(x=130,y=140,width=200)
e7 = Entry(lf1,bd=4,textvariable=expdate)
e7.place(x=130,y=166,width=200)
e8 = Entry(lf1,bd=4,textvariable=dailydose)
e8.place(x=130,y=192,width=200)
e9 = Entry(lf1,bd=4,textvariable=sideeffect)
e9.place(x=130,y=218,width=200)
e10 = Entry(lf1,bd=4,textvariable=furtherinformation)
e10.place(x=500,y=10,width=200)
e11 = Entry(lf1,bd=4,textvariable=bloodpressure)
e11.place(x=500,y=36,width=200)
e12 = Entry(lf1,bd=4,textvariable=storageadvice)
e12.place(x=500,y=62,width=200)
e13 = Entry(lf1,bd=4,textvariable=medication)
e13.place(x=500,y=88,width=200)
e14 = Entry(lf1,bd=4,textvariable=patientid)
e14.place(x=500,y=114,width=200)
e15 = Entry(lf1,bd=4,textvariable=nhsnumbers)
e15.place(x=500,y=140,width=200)
e16 = Entry(lf1,bd=4,textvariable=patientname)
e16.place(x=500,y=166,width=200)
e17 = Entry(lf1,bd=4,textvariable=dateofbirth)
e17.place(x=500,y=192,width=200)
e18 = Entry(lf1,bd=4,textvariable=patientaddress)
e18.place(x=500,y=218,width=200)


#label frame for prescription
lf2 =LabelFrame(frame1,text='Prescription',font='ariel 12 bold',bd=10)
lf2.place(x=770,y=0,width=470,height=280)

#text box for prescription
txt_frame =Text(lf2,font='impacK 10 bold',width=40,height=30,bg='white')
txt_frame.pack(fill=BOTH)

#frame2
frame2=Frame(win,bd=15,relief=RIDGE) 
frame2.place(x=0,y=360,width=1280,height=250)

#Button
##prescription
p_btn = Button(win,text='Prescription',font='ariel 15 bold', bg='brown',fg='white',bd=6,cursor='hand2',command=pre)
p_btn.place(x=0,y=600,width=270)

#prescription data
pd_btn = Button(win,text='Prescription Data',font='ariel 15 bold', bg='purple',fg='white',bd=6,cursor='hand2',command=pd)
pd_btn.place(x=270,y=600,width=330)

# #Exite Button
# ex_btn = Button(win, text='Exit', font='ariel 15 bold', bg='Green', fg='white', bd=6, cursor='hand2',command=exit)
# ex_btn.place(x=600, y=600, width=340)

#delete
d_btn = Button(win, text='Delete', font='ariel 15 bold', bg='blue', fg='white', bd=6, cursor='hand2',command=delete)
d_btn.place(x=600, y=600, width=340)

#clear
c_btn = Button(win, text='Clear', font='ariel 15 bold', bg='Red', fg='white', bd=6, cursor='hand2',command=clear)
c_btn.place(x=1110, y=600, width=170)

#Exite Button
ex_btn = Button(win, text='Exit', font='ariel 15 bold', bg='Green', fg='white', bd=6, cursor='hand2',command=exit)
ex_btn.place(x=940, y=600, width=170)


#scrollbar
scroll_x = ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y = ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')
#table
table =ttk.Treeview(frame2,columns=('not','ref','dose','nots','lot','id','ed','dd','se','fi','bp','sa','med','ptid','nhs','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)
#heading of prescription data
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference')
table.heading('dose',text='Dose')
table.heading('nots',text='No of Tablets')
table.heading('lot',text='Lot')
table.heading('id',text='Issue Date')
table.heading('ed',text='Exp Date')
table.heading('dd',text='Daily Dose')
table.heading('se',text='Side Effects')
table.heading('fi',text='Further Information')
table.heading('bp',text='Blood Pressure')
table.heading('sa',text='Storage Advice')
table.heading('med',text='Medication')
table.heading('ptid',text='Patient Id')
table.heading('nhs',text='NHS Number')
table.heading('pn',text='Patient Name')
table.heading('dob',text='Date of Birth')
table.heading('pa',text='Patient Address')

table['show']='headings'
table.pack(fill=BOTH,expand=1)
#==================================================
table.column('not',width=90)
table.column('ref',width=90)
table.column('dose',width=40)
table.column('nots',width=90)
table.column('lot',width=30)
table.column('id',width=80)
table.column('ed',width=80)
table.column('dd',width=80)
table.column('se',width=80)
table.column('fi',width=115)
table.column('bp',width=90)
table.column('sa',width=90)
table.column('med',width=80)
table.column('ptid',width=90)
table.column('nhs',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)
table.bind('<ButtonRelease->',get_data)
fetch_data()
mainloop()

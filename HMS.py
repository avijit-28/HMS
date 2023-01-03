from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")


        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.Numberoftablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientID=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


    #=======================Dataframe============================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE,bg="blue")
        Dataframe.place(x=0,y=130,width=1360,height=350)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",14,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=800,height=300)

        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",14,"bold"),text="Prescription")
        DataframeRight.place(x=810,y=5,width=460,height=300)

    #==============================buttons frame=================================


        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=485,width=1360,height=70)

    #==============================details frame=================================


        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=555,width=1360,height=150)

    #=============================================DtataframeLeft==================================

        lblNameTablet=Label(DataframeLeft,text="Names of Tablet",font=("times new roman",10,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        

        comNameTablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="randomly",font=("times new roman",10,"bold"),width=33)
        comNameTablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNameTablet.current()
        comNameTablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Reference Number",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=("times new roman",10,"bold"),text="No. Of Tablets",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.Numberoftablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Lot",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Issue Date",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Exp Date",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.Expdate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Daily Dose",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Side Effect",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)
    
        lblFurtherInfo=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Further Info",padx=2)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblDrivingMachine=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Blood Pressure",padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Storage",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Medicine",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)

        lblPatientId=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.PatientID,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Nhs Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Patient Name",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Date Of Birth",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=("times new roman",10,"bold"),text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("times new roman",10,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

    #===================================================DataframeRight=======================================================

        self.txtPrescription=Text(DataframeRight,font=("ariel",12,"bold"),width=46,height=13,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

    #============================================buttons===============================

        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("ariel",12,"bold"),width=20,height=0,padx=2,pady=0,
                               command=self.iPrescription)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("ariel",12,"bold"),width=20,height=0,padx=2,pady=0,
                                   command = self.iPrescriptionData)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("ariel",12,"bold"),width=20,height=0,padx=2,pady=0,
                         command=self.update_data)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("ariel",12,"bold"),width=20,height=0,padx=2,pady=0,
                         command=self.idelete)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("ariel",12,"bold"),width=20,height=0,padx=2,pady=0,
                        command=self.clear)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("ariel",12,"bold"),width=20,height=0,padx=2,pady=0,
                       command=self.iExit)
        btnExit.grid(row=0,column=5)

    #===============================================Table========================================


    #=============================================Scroll Bar====================================================
        #scroll_x=ttk.Scrollbar(Dataframe,orient=HORIZONTAL)
        #scroll_y=ttk.Scrollbar(Dataframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftablet","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage",
                                                              "nhsnumber","pname","dob","address"))#,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #scroll_x.pack(side=BOTTOM,fill=X)
        #scroll_y.pack(side=RIGHT,fill=Y)

        #scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        #scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet",text="Name of Tablet")
        self.hospital_table.heading("ref",text="Referencr No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No. Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"

        
        self.hospital_table.column("nameoftablet",width=90)
        self.hospital_table.column("ref",width=90)
        self.hospital_table.column("dose",width=90)
        self.hospital_table.heading("nooftablets",text="Dose")
        self.hospital_table.column("lot",width=90)
        self.hospital_table.column("issuedate",width=90)
        self.hospital_table.column("expdate",width=90)
        self.hospital_table.column("dailydose",width=90)
        self.hospital_table.column("storage",width=90)
        self.hospital_table.column("nhsnumber",width=90)
        self.hospital_table.column("pname",width=90)
        self.hospital_table.column("dob",width=90)
        self.hospital_table.column("address",width=90)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.fetch_data()

        #========================================functioanality declaration=========================

    def iPrescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required.")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="hms")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                                                     self.ref.get(),
                                                                                                     self.Dose.get(),
                                                                                                     self.Numberoftablets.get(),
                                                                                                     self.Lot.get(),
                                                                                                     self.Issuedate.get(),
                                                                                                     self.Expdate.get(),
                                                                                                     self.DailyDose.get(),
                                                                                                     self.StorageAdvice.get(),
                                                                                                     self.nhsNumber.get(),
                                                                                                     self.PatientName.get(),
                                                                                                     self.DateOfBirth.get(),
                                                                                                     self.PatientAddress.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted.")


    def update_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="hms")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,Dose=%s,Numberoftablets=%s,Lot=%s,Issuedate=%s,Expdate=%s,DailyDose=%s,Storage=%s,nhsNumber=%s,PatientName=%s,DOB=%s,PatientAddress=%s where Reference_No=%s",
                          (self.Nameoftablets.get(),
                           self.Dose.get(),
                           self.Numberoftablets.get(),
                           self.Lot.get(),
                           self.Issuedate.get(),
                           self.Expdate.get(),
                           self.DailyDose.get(),
                           self.StorageAdvice.get(),
                           self.nhsNumber.get(),
                           self.PatientName.get(),
                           self.DateOfBirth.get(),
                           self.PatientAddress.get(),
                           self.ref.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success","Record updated Successfully!")



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="HMS")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            #self.hospital_table.delete("self.hospital_table.get_children()")
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.Numberoftablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.Expdate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrescription(self):
        self.txtPrescription.insert(END,"Name Of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t"+self.Numberoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get()+"\n")
        self.txtPrescription.insert(END,"daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEffect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"PatientID:\t\t\t"+self.PatientID.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"PatientName:\t\t\t"+self.PatientName.get()+"\n")
        self.txtPrescription.insert(END,"DateOfBirth:\t\t\t"+self.DateOfBirth.get()+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+self.PatientAddress.get()+"\n")
    
    def idelete(self):
        conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="HMS")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully.")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.PatientID.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)


    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return
        
root=Tk()
ob=Hospital(root)
root.mainloop()

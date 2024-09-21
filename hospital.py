from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title('Hospital Management System')
        self.width = root.winfo_screenwidth()#1280
        self.height = root.winfo_screenheight()#720
        self.root.geometry(f"{int(self.width)}x{int(self.height)}+0+0")#h*w+x-axis+y-axis
        
        # self.root.geometry("1540x800+0+0")#h*w+x-axis+y-axis
        
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text='HOSPITAL MANAGEMENT SYSTEM', fg = "red", bg="gray", font=('times new roman',20,'bold'))
        lbltitle.pack(side=TOP,fill=X)
        
        # ---------------------------------------Dataframe----------------------------------
        Dataframe = Frame(self.root, bd = 10, relief=RIDGE,bg='gray')
        Dataframe.place(x=0,y=80,width=self.width,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=5,relief=GROOVE,padx=10,
                                font=('times new roman',10,'bold'),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=int(self.width*0.70),height= 360)
        
        DataframeRight=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,
                                font=('times new roman',10,'bold'),text="Prescription")
        DataframeRight.place(x=947,y=5,width=int(self.width*0.24),height= 360)
        #------------------------------------buttons frame---------------------------------------------
        ButtonFrame = Frame(self.root, bd = 5, relief = RIDGE)
        ButtonFrame.place(x=0,y=480,width=1530,height=30)
        #------------------------------------details frame---------------------------------------------
        DetailsFrame = Frame(self.root, bd = 5, relief = RIDGE,bg="brown")
        DetailsFrame.place(x=0,y=511,width=1530,height=120)
        
        #-------------------------------------DataFrame Left-------------------------------------------
        
        lblNameTablet=Label(DataframeLeft, text="Names of Tablet", font=('times new roman',10,'bold'),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet = ttk.Combobox(DataframeLeft, state='readonly',font=('times new roman',10,'bold'), 
                                     width=33)
        comNametablet['values']=('Nice', 'Corona Vaccine', 'Acetaminophen', 'Adderall','Amlodipine','Ativan')
        comNametablet.grid(row=0, column=1)
        
        #referecne
        lblref=Label(DataframeLeft,font=('arial', 12, 'bold'), text='Reference no.:',padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft, font=('arial', 13, 'bold'), width=35)
        txtref.grid(row=1, column=1)
        
        #Dose
        lblDose=Label(DataframeLeft,font=('arial',12,'bold'), text='Dose:',padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=('arial',13,'bold'),width=35)
        txtDose.grid(row=2,column=1)
        
        #No. of tablets
        lblNooftablets=Label(DataframeLeft, font=('arial',12,'bold'),text='No of tablets::',padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=('arial', 13,'bold'), width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        #Lot
        lblLot = Label(DataframeLeft,font=('arial',12,'bold'), text='Lot:',padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=('arial',13,'bold'),width=35)
        txtLot.grid(row=4,column=1)
        
        #Issue Date
        lblissueDate=Label(DataframeLeft,font=('arial',12,'bold'),text='Issue Date:', padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,font=('arial',13,'bold'),width=35)
        txtissueDate.grid(row=5,column=1)
        
        #Exp Date
        lblExpDate = Label(DataframeLeft,font=('arial',12,'bold'), text='Exp Date:', padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=('arial',13,'bold'),width=35)
        txtExpDate.grid(row=6,column=1)
        
        #Daily Dose
        lblDailyDose=Label(DataframeLeft,font=('arial',12,'bold'),text='Daily Dose:', padx=2, pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft, font=('arial', 13,'bold'), width = 35)
        txtDailyDose.grid(row=7,column=1)
        
        #Side Effect
        lblSideEffect = Label(DataframeLeft,font=('arial',12,'bold'),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=('arial',13,'bold'),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        #Further Info
        lblFurtherinfo = Label(DataframeLeft,font=('arial',12,'bold'),text='Further Information',padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=('arial',12,'bold'),width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        #Blood Pressure
        lblBloodPressure = Label(DataframeLeft,font=('arial',12,'bold'),text='Blood Pressure',padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=('arial',12,'bold'),width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        #Storage Advice
        lblStorage=Label(DataframeLeft, font=('arial',12,'bold'),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft, font=('arial', 12,'bold'), width=35)
        txtStorage.grid(row=2,column=3)
        
        #Medication
        lblMedicine=Label(DataframeLeft,font=('arial',12,'bold'),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=('arial',12,'bold'),width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)
        
        #Patient Id
        lblPatientId= Label(DataframeLeft,font=('arial',12,'bold'),text="Patient Id", padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=('arial',12,'bold'),width=35)
        txtPatientId.grid(row=4,column=3)
        
        #NHS Number
        lblNhsNumber = Label(DataframeLeft,font=('arial',12,'bold'),text="NHS Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=('arial',12,'bold'),width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        #Patient Name
        lblPatientname = Label(DataframeLeft, font=('arial',12,'bold'),text="Patient Name",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname= Entry(DataframeLeft, font=('arial',12,'bold'),width=35)
        txtPatientname.grid(row=6,column=5)
        
        #Date of Birth
        lblDateofBirth = Label(DataframeLeft, font=('arial',12,'bold'), text="Date of Birth", padx=2, pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=('arial',12,'bold'),width=35)
        txtDateOfBirth.grid(row=7,column=3)
        
        #Patient Address
        lblPatientAddress = Label(DataframeLeft, font=('arial',12,'bold'),text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=('arial', 12, 'bold'), width = 35)
        txtPatientAddress.grid(row=8,column=3)
    def __str__(self):
        return f'width is {self.width} and height is {self.height}'

root = Tk()
ob = Hospital(root)
print(ob)
root.mainloop()
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

        #####################-Declaration of variables-############################
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowtoUseMedication = StringVar()
        self.PatientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()
        #############################################################################
        
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text='HOSPITAL MANAGEMENT SYSTEM', fg = "red", bg="gray", font=('times new roman',20,'bold'))
        lbltitle.pack(side=TOP,fill=X)
        
        # ---------------------------------------Dataframe----------------------------------
        Dataframe = Frame(self.root, bd = 10, relief=RIDGE,bg='gray')
        Dataframe.place(x=0,y=80,width=self.width,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=5,relief=GROOVE,padx=10,
                                font=('times new roman',10,'bold'),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=int(self.width*0.74),height= 360)
        
        DataframeRight=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=5,
                                font=('times new roman',10,'bold'),text="Prescription")
        DataframeRight.place(x=947,y=5,width=int(self.width*0.24),height= 360)
        #------------------------------------buttons frame---------------------------------------------
        ButtonFrame = Frame(self.root, bd = 5, relief = RIDGE)
        ButtonFrame.place(x=0,y=480,width=1530,height=30)
        #------------------------------------details frame---------------------------------------------
        DetailsFrame = Frame(self.root, bd = 5, relief = RIDGE,bg="white")
        DetailsFrame.place(x=0,y=515,width=1530,height=120)
        
        #-------------------------------------DataFrame Left-------------------------------------------
        
        #Names of tablet
        lblNameTablet=Label(DataframeLeft, text="Names of Tablet", font=('times new roman',13,'bold'),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets,state='readonly',font=('times new roman',10,'bold'), 
                                     width=35)
        comNametablet['values']=('Nice', 'Corona Vaccine', 'Acetaminophen', 'Adderall','Amlodipine','Ativan')
        comNametablet.grid(row=0, column=1)
        
        #referecne
        lblref=Label(DataframeLeft,font=('arial', 12, 'bold'), text='Reference no.:',padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft, textvariable=self.ref,font=('arial', 13, 'bold'), width=35)
        txtref.grid(row=1, column=1)
        
        #Dose
        lblDose=Label(DataframeLeft,font=('arial',12,'bold'), text='Dose:',padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,textvariable=self.Dose,font=('arial',13,'bold'),width=35)
        txtDose.grid(row=2,column=1)
        
        #No. of tablets
        lblNooftablets=Label(DataframeLeft, font=('arial',12,'bold'),text='No of tablets::',padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataframeLeft, textvariable=self.NumberofTablets,font=('arial', 13,'bold'), width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        #Lot
        lblLot = Label(DataframeLeft,font=('arial',12,'bold'), text='Lot:',padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,textvariable=self.Lot,font=('arial',13,'bold'),width=35)
        txtLot.grid(row=4,column=1)
        
        #Issue Date
        lblissueDate=Label(DataframeLeft,font=('arial',12,'bold'),text='Issue Date:', padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataframeLeft,textvariable=self.IssueDate,font=('arial',13,'bold'),width=35)
        txtissueDate.grid(row=5,column=1)
        
        #Exp Date
        lblExpDate = Label(DataframeLeft,font=('arial',12,'bold'), text='Exp Date:', padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,textvariable=self.ExpDate,font=('arial',13,'bold'),width=35)
        txtExpDate.grid(row=6,column=1)
        
        #Daily Dose
        lblDailyDose=Label(DataframeLeft,font=('arial',12,'bold'),text='Daily Dose:', padx=2, pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft, textvariable=self.DailyDose,font=('arial', 13,'bold'), width = 35)
        txtDailyDose.grid(row=7,column=1)
        
        #Side Effect
        lblSideEffect = Label(DataframeLeft,font=('arial',12,'bold'),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,textvariable=self.sideEffect,font=('arial',13,'bold'),width=35)
        txtSideEffect.grid(row=8,column=1)
        
        #Further Info
        lblFurtherinfo = Label(DataframeLeft,font=('arial',12,'bold'),text='Further Information',padx=2)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,textvariable=self.FurtherInformation,font=('arial',12,'bold'),width=35)
        txtFurtherinfo.grid(row=0,column=3)
        
        #Blood Pressure
        lblBloodPressure = Label(DataframeLeft,font=('arial',12,'bold'),text='Blood Pressure',padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,textvariable=self.DrivingUsingMachine,font=('arial',12,'bold'),width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        #Storage Advice
        lblStorage=Label(DataframeLeft, font=('arial',12,'bold'),text="Storage Advice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,textvariable=self.StorageAdvice, font=('arial', 12,'bold'), width=35)
        txtStorage.grid(row=2,column=3)
        
        #Medication
        lblMedicine=Label(DataframeLeft,font=('arial',12,'bold'),text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,textvariable=self.HowtoUseMedication,font=('arial',12,'bold'),width=35)
        txtMedicine.grid(row=3,column=3,sticky=W)
        
        #Patient Id
        lblPatientId= Label(DataframeLeft,font=('arial',12,'bold'),text="Patient Id", padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,textvariable=self.PatientId,font=('arial',12,'bold'),width=35)
        txtPatientId.grid(row=4,column=3)
        
        #NHS Number
        lblNhsNumber = Label(DataframeLeft,font=('arial',12,'bold'),text="NHS Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,textvariable=self.nhsNumber,font=('arial',12,'bold'),width=35)
        txtNhsNumber.grid(row=5,column=3)
        
        #Patient Name
        lblPatientname = Label(DataframeLeft, font=('arial',12,'bold'),text="Patient Name",padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname= Entry(DataframeLeft, textvariable=self.PatientName,font=('arial',12,'bold'),width=35)
        txtPatientname.grid(row=6,column=3)
        
        #Date of Birth
        lblDateofBirth = Label(DataframeLeft, font=('arial',12,'bold'), text="Date of Birth", padx=2, pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,textvariable=self.DateOfBirth,font=('arial',12,'bold'),width=35)
        txtDateOfBirth.grid(row=7,column=3)
        
        #Patient Address
        lblPatientAddress = Label(DataframeLeft, font=('arial',12,'bold'),text="Patient Address", padx=2, pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataframeLeft,textvariable=self.PatientAddress, font=('arial', 12, 'bold'), width = 35)
        txtPatientAddress.grid(row=8,column=3)
        
        # --------------------------------------------------Data Frame Right ------------------------------------
        
        self.txtPrescription = Text(DataframeRight, font=('arial',8, 'bold'), width=45, height=20, padx=1, pady=6)
        self.txtPrescription.grid(row=0,column=0)
        #---------------------------------------------------Buttons----------------------------------------------
        btnPrescription = Button(ButtonFrame,command=self.iPrescription,text="Prescription",font=('arial',6,'bold'), fg="white",bg="green",  width=40, padx=2,pady=6)
        btnPrescription.grid(row=0,column=1)
        
        btnPrescriptionData = Button(ButtonFrame, command=self.iPrescriptionData,text="Prescription Data",font=('arial',6,'bold'), fg="white",bg="green",  width=40,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=2)
        
        btnUpdate = Button(ButtonFrame,command=self.update_data,text="Update",font=('arial',6,'bold'), fg="brown",bg="green",  width=40, padx=2,pady=6)
        btnUpdate.grid(row=0,column=3)        

        btnDelete = Button(ButtonFrame,command=self.idelete,text="Delete",font=('arial',6,'bold'), fg="white",bg="green",  width=40,  padx=2,pady=6)
        btnDelete.grid(row=0,column=4)

        btnClear = Button(ButtonFrame,command=self.clear,text="Clear",font=('arial',6,'bold'), fg="white",bg="green",  width=40, padx=2,pady=6)
        btnClear.grid(row=0,column=5)

        btnExit = Button(ButtonFrame,command=self.iExit,text="Exit",font=('arial',6,'bold'), fg="white",bg="green",  width=40, padx=2,pady=6)
        btnExit.grid(row=0,column=6)
        
        #-----------------------------------------Table-----------------------------------------------------------------
        #----------------scrollbar----------------------
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)

        # Create the Treeview widget and link the scrollbars
        self.hospital_table = ttk.Treeview(DetailsFrame, 
                                        columns=('nameoftablets','ref','dose','nooftablets','lot','issuedate',
                                                    'expdate','dailydose','storage','nhsnumber','pname','dob','address'),
                                        xscrollcommand=scroll_x.set,  # Link horizontal scrollbar
                                        yscrollcommand=scroll_y.set)  # Link vertical scrollbar

        # Pack the scrollbars in the correct positions
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        # Configure the scrollbars to work with the Treeview
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        # Configure the column headings
        self.hospital_table.heading('nameoftablets', text="Name of Tablets")
        self.hospital_table.heading('ref', text='Reference No.')
        self.hospital_table.heading('dose', text='Dose')  # Missing in your original setup
        self.hospital_table.heading('nooftablets', text='No. of Tablets')
        self.hospital_table.heading('lot', text="Lot")
        self.hospital_table.heading('issuedate', text="Issue Date")
        self.hospital_table.heading('expdate', text='Expiry Date')
        self.hospital_table.heading('dailydose', text='Daily Dose')
        self.hospital_table.heading('storage', text='Storage')
        self.hospital_table.heading('nhsnumber', text='NHS Number')
        self.hospital_table.heading('pname', text="Patient Name")
        self.hospital_table.heading('dob', text='Date of Birth')
        self.hospital_table.heading('address', text='Address')

        # Make sure only the headings are displayed (no default empty column)
        self.hospital_table['show'] = 'headings'

        # Pack the Treeview to fill the entire area
        self.hospital_table.pack(fill=BOTH, expand=1)

        # Bind the Treeview to the cursor event (assumed to select a row)
        self.hospital_table.bind('<ButtonRelease-1>', self.get_cursor)

        # Call to fetch and display data
        self.fetch_data()
      
    #===============================Functionality Declaration=====================================

    def iPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                # Establish MySQL connection
                conn = mysql.connector.connect(
                    host='localhost',
                    username='root',
                    password='root',
                    database='mydata'
                )
                my_cursor = conn.cursor()

                # Insert query
                my_cursor.execute('''INSERT INTO hospital (Nameoftablets, ReferenceNo, Dose, issuedate, expdate, dailydose, storage, nhsnumber, DOB, patientaddress) 
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (
                    self.Nameoftablets.get(),
                    self.ref.get(),
                    self.Dose.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.StorageAdvice.get(),
                    self.nhsNumber.get(),
                    self.DateOfBirth.get(),
                    self.PatientAddress.get()
                ))

                # Commit to the database
                conn.commit()

                # Refresh the data and close connection
                self.fetch_data()
                conn.close()

                # Success message
                messagebox.showinfo('Success', "Record has been inserted")

            except mysql.connector.Error as err:
                # Handling specific MySQL errors
                messagebox.showerror('Database Error', f"Error: {err}")
            except Exception as e:
                # Handling general errors
                messagebox.showerror('Error', f"An error occurred: {e}")
            finally:
                if conn.is_connected():
                    conn.close()  # Ensure the connection is closed

    
    def fetch_data(self):
            conn = mysql.connector.connect(host='localhost', username='root',password='root',database='mydata')
            my_cursor=conn.cursor()
            my_cursor.execute('select * from hospital')
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert('', END, values = i)
                conn.commit()
            conn.close()
    
    def get_cursor(self, event=None):
        cursor_row = self.hospital_table.focus()  # Get the ID of the selected row
        row = self.hospital_table.item(cursor_row, 'values')  # Get the values of the selected row
        
        if row:  # Check if row has data
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.NumberofTablets.set(row[3])
            self.Lot.set(row[4])
            self.IssueDate.set(row[5])
            self.ExpDate.set(row[6])
            self.DailyDose.set(row[7])
            self.StorageAdvice.set(row[8])
            self.nhsNumber.set(row[9])
            self.PatientName.set(row[10])
            self.DateOfBirth.set(row[11])
            self.PatientAddress.set(row[12])
        else:
            # Handle the case when no row is selected or row is empty
            print("No row selected or row is empty.")

        
    def update_data(self):
        # Establish connection
        conn = mysql.connector.connect(host='localhost', username='root', password='root', database='mydata')
        my_cursor = conn.cursor()

        # Correct the SQL query
        update_query = '''
        UPDATE hospital 
        SET 
            Nameoftablets=%s, 
            dose=%s, 
            Numbersoftablets=%s, 
            Lot=%s, 
            issuedate=%s, 
            expdate=%s, 
            dailydose=%s, 
            storage=%s, 
            nhsnumber=%s, 
            patientname=%s, 
            DOB=%s, 
            patientaddress=%s 
        WHERE 
            ReferenceNo=%s
        '''

        # Execute the query with data values
        my_cursor.execute(update_query, (
            self.Nameoftablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.IssueDate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.StorageAdvice.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get(),
        ))

        # Commit changes
        conn.commit()
        self.fetch_data()
        # Close the connection
        conn.close()

    def iPrescription(self):
        self.txtPrescription.delete("1.0", END)
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t" + self.ref.get() + "\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END,"Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t" + self.sideEffect.get() + "\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END,"StorageAdvice:\t\t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
        self.txtPrescription.insert(END,"PatientId:\t\t\t" + self.PatientId.get() + "\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END,"Date of Birth:\t\t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t" + self.PatientAddress.get() + "\n")

    def idelete(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='root', database='mydata')
        my_cursor = conn.cursor()
        query = 'delete from hospital where ReferenceNo=%s'
        value=(self.ref.get(),)
        my_cursor.execute(query,value)
        
        conn.commit()
        
        conn.close()
        self.fetch_data()
        messagebox.showinfo('Delete','Patient has been deleted successfully')
    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def iExit(self):
        iExit = messagebox.askyesno('Hospital management system', 'Confirm you want to exit')
        if iExit > 0:
                root.destroy()
                return
    
    def __str__(self):
        return f'width is {self.width} and height is {self.height}'

root = Tk()
ob = Hospital(root)
print(ob)
root.mainloop()

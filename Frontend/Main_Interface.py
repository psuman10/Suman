import tkinter
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from Backend import air_query
from Frontend import Airline_Bill

class Airline:
    """ class is used because it is a grouping of object-oiented constructs and it is
            used to keep related things together"""

    def __init__(self, ):
        self.root = Tk()
        self.root.title("Ticket Booking System")
        self.root.geometry('1350x800+100+0')
        self.airline=air_query.Airline()
        self.title = Label(self.root, text="Ticket Booking System", relief=GROOVE, font=('Comic Sans MS', 38, 'bold'),
                      bg='black', fg='white')
        self.title.pack(side=TOP, fill=X)

#############  STRINGVAR  #################################################
        self.passport_No_var = StringVar()
        self.Full_Name_var = StringVar()
        self.Journey_Date_var = StringVar()
        self.Gender_var = StringVar()
        self.Email_var = StringVar()
        self.boarding_var = StringVar()
        self.Pick_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()


###################   FRAME  ##########################################

        self.Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='black')
        self.Manage_Frame.place(x=20, y=100, width=450, height=680)

        self.m_title = Label(self.Manage_Frame, text='SP FLIGHTS', bg='black', fg='white', font=('Comic Sans MS', 25, 'bold'))
        self.m_title.grid(row=0, column=1, columnspan=1, pady=10)

#######################################  LABEL AND ENTRY OF PASSPORT NO

        self.lbl_pass = Label(self.Manage_Frame, text='Passport No.', bg='black', fg='white', font=('Comic Sans MS', 18, 'bold'))
        self.lbl_pass.grid(row=1, column=0, pady=20, padx=10, sticky=W)
        self.txt_pass = Entry(self.Manage_Frame, textvariable=self.passport_No_var, font=('arial', 15, 'bold'), bd=5,
                         relief=RAISED)
        self.txt_pass.grid(row=1, column=1, pady=20, padx=10, sticky=W)

        #######################################  LABEL AND ENTRY OF FULL NAME
        self.lbl_Fname = Label(self.Manage_Frame, text='Full-Name', bg='black', fg='white', font=('Comic Sans MS', 18, 'bold'))
        self.lbl_Fname.grid(row=2, column=0, pady=20, padx=10, sticky=W)
        self.txt_Fname = Entry(self.Manage_Frame, textvariable=self.Full_Name_var, font=('arial', 15, 'bold'), bd=5, relief=RAISED)
        self.txt_Fname.grid(row=2, column=1, pady=20, padx=10, sticky=W)

        #######################################  LABEL AND ENTRY OF GENDER

        self.lbl_Gender = Label(self.Manage_Frame, text='Gender', bg='black', fg='white', font=('Comic Sans MS', 18, 'bold'))
        self.lbl_Gender.grid(row=3, column=0, pady=20, padx=10, sticky=W)
        self.combo_gender = ttk.Combobox(self.Manage_Frame, textvariable=self.Gender_var, font=('times new roman', 14, 'bold'),
                                    state='readonly')
        self.combo_gender['values'] = ('Male', 'Female', 'Other')
        self.combo_gender.grid(row=3, column=1, padx=10, pady=20)

        #######################################  LABEL AND ENTRY OF JOURNEY DATE
        self.lbl_jo = Label(self.Manage_Frame, text='JourneyDate', bg='black', fg='white', font=('Comic Sans MS', 18, 'bold'))
        self.lbl_jo.grid(row=4, column=0, pady=20, padx=10, sticky=W)
        self.txt_jo = Entry(self.Manage_Frame, textvariable=self.Journey_Date_var, font=('arial', 15, 'bold'), bd=5,
                       relief=RAISED)
        self.txt_jo.grid(row=4, column=1, pady=20, padx=10, sticky=W)
        self.txt_jo.insert(0, "DD/MM/YYYY")

        #######################################  LABEL AND ENTRY OF PICKUP POINT
        self.variable = StringVar(self.Manage_Frame)
        self.variable = Label(self.Manage_Frame, text='Pick UP Point', bg='black', fg='white',font=('Comic Sans MS', 18, 'bold'))
        self.variable.grid(row=5, column=0, pady=20, padx=10, sticky=W)
        self.combo_pick = ttk.Combobox(self.Manage_Frame, textvariable=self.Pick_var, font=('times new roman', 14, 'bold'),state='readonly')
        self.combo_pick['values'] = ("New York", "kathmandu-Nepal", "sydney", "brisbane", "Delhi")
        self.combo_pick.grid(row=5, column=1, padx=10, pady=20)

        #######################################  LABEL AND ENTRY OF EMAIL
        self.lbl_email = Label(self.Manage_Frame, text='Email', bg='black', fg='white', font=('Comic Sans MS', 18, 'bold'))
        self.lbl_email.grid(row=6, column=0, pady=20, padx=10, sticky=W)
        self.txt_email = Entry(self.Manage_Frame, textvariable=self.Email_var, font=('arial', 15, 'bold'), bd=5, relief=RAISED)
        self.txt_email.grid(row=6, column=1, pady=20, padx=10, sticky=W)

        #######################################  LABEL AND ENTRY OF BOARDING POINT
        self.variable = StringVar(self.Manage_Frame)
        self.variable = Label(self.Manage_Frame, text='Boarding Point', bg='black', fg='white',font=('Comic Sans MS', 18, 'bold'))
        self.variable.grid(row=7, column=0, pady=5, padx=5, sticky=W)
        self.combo_drop = ttk.Combobox(self.Manage_Frame, textvariable=self.boarding_var, font=('times new roman', 14, 'bold'),state='readonly')
        self.combo_drop['values'] = ("New York", "kathmandu-Nepal", "sydney", "brisbane", "Delhi")
        self.combo_drop.grid(row=7, column=1, padx=10, pady=20)

        ####################################### BUTTON

        self.btn_Frame = Frame(self.Manage_Frame, bd=4, relief=RIDGE, bg='skyblue')
        self.btn_Frame.place(x=10, y=610, width=430)
        self.Add_btn = Button(self.btn_Frame, text='Add', width=8, command=self.add_passenger ).grid(row=0, column=0, padx=10, pady=10)
        self.Update_btn = Button(self.btn_Frame, text='Update', width=8, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        self.Delete_btn = Button(self.btn_Frame, text='Delete', width=8, command=self.delete_datas).grid(row=0, column=2, padx=10, pady=10)
        self.Clear_btn = Button(self.btn_Frame, text='Clear', width=8, command=self.clearing).grid(row=0, column=3, padx=10, pady=10)
        self.Close_btn = Button(self.btn_Frame, text='Close', width=8, command=self.close).grid(row=0, column=4, padx=10, pady=10)

        ###############detail  Frame
        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='skyblue')
        self.Detail_Frame.place(x=500, y=100, width=800, height=680)
        self.lbl_Search = Label(self.Detail_Frame, text='Search By', bg='skyblue', fg='black', font=('arial', 20, 'bold'))
        self.lbl_Search.grid(row=0, column=0, pady=10, padx=20, sticky=W)
        self.combo_search = ttk.Combobox(self.Detail_Frame, width=10, textvariable=self.search_by,
                                    font=('times new roman', 13, 'bold'), state='readonly')
        self.combo_search['values'] = ('Passport', 'name', 'pickup', 'email')
        self.combo_search.grid(row=0, column=1, padx=20, pady=10)
        self.txt_Search = Entry(self.Detail_Frame, width=20, textvariable=self.search_txt, font=('arial', 10, 'bold'), bd=5, relief=GROOVE)
        self.txt_Search.grid(row=0, column=2, pady=20, padx=10, sticky=W)

    ##### BUTTON#############################################3
        self.search_btn = Button(self.Detail_Frame, text='Search', width=10, command=self.search_data,pady=5).grid(row=0, column=3, padx=10, pady=10)
        self.show_all_btn = Button(self.Detail_Frame, text='refresh', width=10, pady=5, command=self.fetch_data ).grid(row=0, column=4, padx=10, pady=10)
        self.bill_btn = Button(self.root, text='TOTAL AMOUNT', font=('arial', 10, 'bold'), command=self._bill_).place(x=945, y=725, width=330)


        ########################TABLE FRAME
        self.Table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg='black')
        self.Table_Frame.place(x=10, y=70, width=760, height=550)
        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.table = ttk.Treeview(self.Table_Frame,
                                  columns=('Passport', 'name', 'gender', 'date', 'pickup', 'email', 'boarding',),
                                  xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.table.xview)
        self.scroll_y.config(command=self.table.yview)
        self.table.heading('Passport', text='Passport No')
        self.table.heading('name', text='Full Name')
        self.table.heading('gender', text='Gender')
        self.table.heading('date', text='Journey Date')
        self.table.heading('pickup', text='Pick UP')
        self.table.heading('email', text='Email')
        self.table.heading('boarding', text='Boarding Point')
        self.table['show'] = 'headings'
        self.table.column('Passport', width=150)
        self.table.column('name', width=120)
        self.table.column('gender', width=150)
        self.table.column('date', width=200)
        self.table.column('pickup', width=150)
        self.table.column('email', width=250)
        self.table.column('boarding', width=150)
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind('<ButtonRelease-1>', self.get_cursor)
        self.root.mainloop()


                        ##############FUNCTION
    def fetch_data(self):

            self.table.delete(*self.table.get_children())
            # data= Sorting.sorting_sp(air_query.Airline().fetch_data())
            data=(air_query.Airline().fetch_data())
            for i in data:
                self.table.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

    ##############FUNCTION
    def clearing(self):
        try:
            if self.passport_No_var.get() != '' and self.Full_Name_var.get() != '' and self.Journey_Date_var.get() != '' and \
                    self.Gender_var.get() != '' and self.Email_var.get() != '' and self.Pick_var.get() != '' and self.boarding_var.get() != '':

                self.passport_No_var.set('')
                self.Full_Name_var.set('')
                self.Gender_var.set('')
                self.Journey_Date_var.set('')
                self.Pick_var.set('')
                self.Email_var.set('')
                self.boarding_var.set('')
            else:
                messagebox.showerror('Empty', 'Fill All ')
                return False
        except Exception as e:
            print(e)
    ##############FUNCTION
    def clear(self):
        try:
            self.passport_No_var.set('')
            self.Full_Name_var.set('')
            self.Gender_var.set('')
            self.Journey_Date_var.set('')
            self.Pick_var.set('')
            self.Email_var.set('')
            self.boarding_var.set('')
            return False
        except Exception as e:
            print(e)

    ##############FUNCTION
    def get_cursor(self,ev):

        cursor_row = self.table.focus()
        content = self.table.item(cursor_row)
        row = content['values']
        self.passport_No_var.set(row[0])
        self.Full_Name_var.set(row[1])
        self.Gender_var.set(row[2])
        self.Journey_Date_var.set(row[3])
        self.Pick_var.set(row[4])
        self.Email_var.set(row[5])
        self.boarding_var.set(row[6])
        return True



    ##############FUNCTION
    def update_data(self):
        try:
            if self.airline.update(

                    self.Full_Name_var.get(),
                    self.Gender_var.get(),
                    self.Journey_Date_var.get(),
                    self.Pick_var.get(),
                    self.Email_var.get(),
                    self.passport_No_var.get(),
                    self.boarding_var.get()):
                messagebox.showinfo('Success', 'Updates Successfully')
                self.fetch_data()
                self.clear()
        except Exception as e:
            print(e)

    ##############FUNCTION
    def delete_datas(self):
        try:
            if self.passport_No_var.get() != '' and self.Full_Name_var.get() != '' and self.Journey_Date_var.get() != '' and \
                    self.Gender_var.get() != '' and self.Email_var.get() != '' and self.Pick_var.get() != '' and self.boarding_var.get() != '':
                air_query.Airline().delete_datas(self.passport_No_var.get())

                messagebox.showinfo('Success', 'Passenger Details deleted')
                self.fetch_data()
                self.clearing()
            else:
                messagebox.showerror('Error', 'Select The Details First')
        except Exception as e:
            print(e)

    ##############FUNCTION
    def search_data(self):
        try:
            if self.search_txt.get() != '':
                rows = air_query.Airline().search_data(self.search_by.get(), self.search_txt.get())

                if len(rows) != 0:
                    self.table.delete(*self.table.get_children())
                    for row in rows:
                        self.table.insert('', END, values=row)
                else:
                    messagebox.showinfo('Not Found', 'Put Details Correctly')
            else:
                tkinter.messagebox.showwarning('please fill the box')

        except Exception as e:
            print(e)

    ##############FUNCTION
    def _bill_(self):

        try:
            ob = messagebox.askyesno("Bill", "want to open billing system?")
            if ob > 0:
                self.root.destroy()
                Airline_Bill.bill()
            else:
                return True
        except Exception as e:
            print(e)

    ##############FUNCTION
    def add_passenger(self):

        if self.passport_No_var.get() != '' and self.Full_Name_var.get() != '' and self.Journey_Date_var.get() != '' and \
                self.Gender_var.get() != '' and self.Email_var.get() != '' and self.Pick_var.get() != '' and self.boarding_var.get() != '':
            if self.airline.add(
                    self.passport_No_var.get(),
                    self.Full_Name_var.get(),
                    self.Gender_var.get(),
                    self.Journey_Date_var.get(),
                    self.Pick_var.get(),
                    self.Email_var.get(),
                    self.boarding_var.get()):
                messagebox.showinfo('Success', 'Passenger Details Added')
                self.fetch_data()
                self.clear()

    ##############FUNCTION

    def close(self):
        try:
            ob = messagebox.askyesno('Close', 'Are you sure you want to close the program? If yes click ok')
            if ob > 0:
                self.root.destroy()
                return True
        except Exception as e:
            print(e)

#
# Airline()

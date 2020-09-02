from tkinter import *
from tkinter import messagebox
import os
import math, random

from Backend import air_query


class bills:
    def __init__(self):
        self.window=Tk()
        self.window.geometry("1000x600+0+0")
        self.window.title("Billing")
        title = Label(self.window, text="Welcome to Airling Billing System", bd=12, bg="Black", fg="white",
                      font=('Comic Sans MS', 30, 'bold'), pady=2).pack(fill=X)
        self.window.resizable(False, False)

        self.semfee = IntVar()
        self.anfee = IntVar()
        self.regfee = IntVar()
        self.ecafee = IntVar()
        self.liabfee = IntVar()
        self.labfee = IntVar()
        self.exmfee = IntVar()
        self.sname = StringVar()
        self.roll = StringVar()
        self.bill_no = StringVar()
        x = random.randint(100, 9999)
        self.bill_no.set(str(x))
        self.Passport_No = StringVar()
        self.search = StringVar()
        self.tot = StringVar()
        self.tax = StringVar()
        self.dis = StringVar()
        self.search=StringVar()
        ###====CUSTOMER DETAILS FRAMES====####
        F1 = LabelFrame(self.window, text="Customer Details", bg="medium blue", fg="black",
                        font=('Comic Sans MS', 15, 'bold'))
        F1.place(x=0, y=80, relwidth=1)
        sname_lbl = Label(F1, text="Passport No:", bg="medium blue", fg="black",
                          font=('Comic Sans MS', 15, 'bold')).grid(row=0, column=0, padx=20, pady=5)
        sname_txt = Entry(F1, width=15, textvariable=self.sname,
                          font=("arial", 15, "bold")).grid(row=0, column=1, pady=5, padx=10)
        sroll_lbl = Label(F1, text="Name:", bg="medium blue", fg="black",
                          font=("arial", 12, "bold")).grid(row=0, column=2, padx=20, pady=5)
        sroll_txt = Entry(F1, width=12, textvariable=self.roll,
                          font=("arial", 15, "bold")).grid(row=0, column=3, pady=5, padx=10)
    #     ssem_lbl = button(F1, text="Bill No:", bg="medium blue", fg="black",
    #                      font=("arial", 12, "bold")).grid(row=0, column=4, padx=20, pady=5)
    #     ssem_txt = Entry(F1, width=12, textvariable=self.Passport_No,
    #
    #                    font=("arial", 15, "bold")).grid(row=0, column=5, pady=5, padx=10)
    #
    #     combo_search = ttk.Combobox(F1, width=10, textvariable=self.search,
    #                                 font=('times new roman', 13, 'bold'), state='readonly')
    #     combo_search['values'] = ('Passport', 'name', 'pickup', 'email')
    #     combo_search.grid(row=0, column=1, padx=20, pady=10)
    #
    # def search_data(self):
    #     try:
    #         if self.Passport_No.get() != '':
    #                 rows = air_query.Airline().search_data(self.Passport_No.get(), self.search.get())
    #
    #                 if len(rows) != 0:
    #                     self.table.delete(*self.table.get_children())
    #                     for row in rows:
    #                         self.table.insert('', END, values=row)
    #                 else:
    #                     messagebox.showinfo('Not Found', 'Put Details Correctly')
    #             else:
    #                 tkinter.messagebox.showwarning('please fill the box')
    #
    #         except Exception as e:
    #             print(e)


        ###===BUTTON===###
        # search_btn = Button(F1, text="Search", command=self.find_bill, width=9, font=("arial", 15, "bold")).grid(row=0,
        #                                                                                                          column=8)

        ###=======BILL AREA=======###
        F3 = LabelFrame(self.window, bg="white", fg="black",
                        font=("arial", 15, "bold"))
        F3.place(x=70, y=170, width=850, height=380)
        bill_title = Label(F3, text="Invoice", font=("arial", 15, "bold")).pack(fill=X)
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea = Text(F3, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        self.welcome()
    def total(self):
        self.sem_fee = self.semfee.get()
        self.an_fee = self.anfee.get()
        self.reg_fee = self.regfee.get()
        self.eca_fee = self.ecafee.get()
        self.exm_fee = self.exmfee.get()
        self.liab_fee = self.liabfee.get()
        self.lab_fee = self.labfee.get()
        self.total_fee = (
                self.sem_fee +
                self.an_fee +
                self.reg_fee +
                self.eca_fee +
                self.exm_fee +
                self.liab_fee +
                self.lab_fee
        )
        self.total_tot = self.total_fee
        self.tot.set("Rs." + str(self.total_tot))
        self.total_tax = self.total_fee * 0.02
        self.tax.set("Rs." + str(self.total_tax))
        self.total_dis = self.total_fee * 0.05
        self.dis.set("Rs." + str(self.total_dis))
        self.Total_bill = self.total_tot + self.total_tax + self.total_dis
    def welcome(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(
            END, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You For Choosing Nepal Airlines")

        self.textarea.insert(END, f"\t\t\t\t\t\t\t\t\tPassport_No:{self.Passport_No.get()}")
        self.textarea.insert(END, f"\n Name:{self.sname.get()}")
        self.textarea.insert(END, f"\t\t\t\t\t\t\t\t\tBill No.:{self.bill_no.get()}")
        self.textarea.insert(END,
                             f"\n---------------------------------------------------------------------------------------------------")
        self.textarea.insert(END, f"\n PARTICULARS\t\t\t\t\t\t\t\t\t\t\tAMOUNT")
        self.textarea.insert(END,
                             f"\n---------------------------------------------------------------------------------------------------")
    # def particulars(self):
    #     if self.sname.get() == ""  or self.Passport_No.get() == "":
    #         messagebox.showerror("ERROR", "Enter Students Details")
    #     else:
    #         self.welcome()
    #         if self.semfee.get() != 0:
    #             self.textarea.insert(END, f"\nSemester Fee\t\t\t\t\t\t\t\t\t\t\t{self.sem_fee}")
    #         if self.anfee.get() != 0:
    #             self.textarea.insert(END, f"\nAnnual Fee\t\t\t\t\t\t\t\t\t\t\t{self.an_fee}")
    #         if self.regfee.get() != 0:
    #             self.textarea.insert(END, f"\nRegistration Fee\t\t\t\t\t\t\t\t\t\t\t{self.reg_fee}")
    #         if self.ecafee.get() != 0:
    #             self.textarea.insert(END, f"\nECA Fee\t\t\t\t\t\t\t\t\t\t\t{self.eca_fee}")
    #         if self.exmfee.get() != 0:
    #             self.textarea.insert(END, f"\nExam Fee\t\t\t\t\t\t\t\t\t\t\t{self.exm_fee}")
    #         if self.liabfee.get() != 0:
    #             self.textarea.insert(END, f"\nLiabrary Fee\t\t\t\t\t\t\t\t\t\t\t{self.lab_fee}")
    #         if self.labfee.get() != 0:
    #             self.textarea.insert(END, f"\nLab Fee\t\t\t\t\t\t\t\t\t\t\t{self.lab_fee}")
    #         ######################
    #         self.textarea.insert(END,
    #                              f"\n---------------------------------------------------------------------------------------------------")
    #         self.textarea.insert(END, f"\nTax\t\t\t\t\t\t\t\t\t\t\t{str(self.tax.get())}")
    #         self.textarea.insert(END, f"\nDiscount\t\t\t\t\t\t\t\t\t\t\t{str(self.dis.get())}")
    #         self.textarea.insert(END,
    #                              f"\n---------------------------------------------------------------------------------------------------")
    #         self.textarea.insert(END, f"\nTotal Amount\t\t\t\t\t\t\t\t\t\t\tRs.{str(self.total_fee)}")
    #         self.textarea.insert(END,
    #                              f"\n-------------------------------------------****THANK YOU****-------------------------------------")
            # self.save_bill()
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do You Want TO Save The Bill?")
        if op > 0:
            self.bill_data = self.textarea.get('1.0', END)
            f = open("BILLS/" + str(self.bill_no.get()) + ".txt", "w")
            f.write(self.bill_data)
            f.close()
            messagebox.showinfo("Success", f"\nYour bill {self.bill_no.get()} has been saved successfully")
        else:
            return
    def find_bill(self):
        present = "no"
        for i in os.listdir("BILLS/"):
            if i.split('.')[0] == self.bill_no.get():
                f = open(f"BILLS/{i}", "r")
                self.textarea.delete("1.0", END)
                for d in f:
                    self.textarea.insert(END, d)
                f.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("ERROR", "Bill not Found!!!")
    def clear_txt(self):
        op = messagebox.askyesno("Clear", "Do you want to clear data?")
        if op > 0:
            self.semfee.set(0)
            self.anfee.set(0)
            self.regfee.set(0)
            self.ecafee.set(0)
            self.liabfee.set(0)
            self.labfee.set(0)
            self.exmfee.set(0)
            self.sname.set("")
            self.bill_no.set("")
            x = random.randint(100, 9999)
            self.bill_no.set(str(x))
            self.Passport_No.set("")
            self.search.set("")
            self.tot.set("")
            self.tax.set("")
            self.dis.set("")
            self.welcome()
    def Exit(self):
        op = messagebox.askyesno("Exit", "Do you want to exit?")
        if op > 0:
            self.window.destroy()



#
window = Tk()
obj = bill()
window.mainloop()
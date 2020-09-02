from tkinter import *
from tkinter import messagebox
import random
import os

class bill:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("1250x600+0+0")
        self.window.title("Billing")
        self.title = Label(self.window, text="Welcome to Airling Billing System", bd=12, bg="Black", fg="white",
                      font=('Comic Sans MS', 30, 'bold'), pady=2).pack(fill=X)
        self.window.resizable(False, False)


        ####################################################
        self.passn = StringVar()
        self.fname = StringVar()
        self.bill_no = StringVar()
        x = random.randint(0,999)
        self.bill_no.set(str(x))
        self.Takeoff = StringVar()
        self.Check=StringVar()
        self.Seat_Class = StringVar()
        self.LWeight = StringVar()
        self.amount=StringVar()
        self.Class_fee = self.Seat_Class.get()
        self.Weight_fee = self.LWeight.get()

           ######   FRAME     LABEL     ####

        self.Air = LabelFrame(self.window, text="Details", bg="white", fg="black",
                         font=("arial", 15, "bold"))
        self.Air.place(x=0, y=85, height=320, width=360)

        self.pass_txt = Label(self.Air, text="Passport No", bg="white", fg="black",
                              font=('Calibri', 15, 'bold')).grid(row=0, column=0, padx=10,pady=10, sticky="w")
        self.pass_entry = Entry(self.Air, font=("arial", 12), textvariable=self.passn,
                                fg="black", bg="whitesmoke", relief=GROOVE).grid(row=0, column=1, padx=10, pady=10)

        self.name = Label(self.Air, text="Full-Name",
                          font=("goudy", 12, "bold"), bg="white", fg="black").grid(row=1, column=0, padx=10, pady=10,sticky="w")
        self.name = Entry(self.Air, font=("arial", 12), textvariable=self.fname,
                          fg="black", bg="whitesmoke", relief=GROOVE).grid(row=1, column=1, padx=10, pady=10)

        self.TO = Label(self.Air, text=" Destination", font=("goudy", 12, "bold")
                        , bg="white", fg="black").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.TO = Entry(self.Air, font=("arial", 12), textvariable=self.Takeoff,
                        fg="black", bg="whitesmoke", relief=GROOVE).grid(row=2, column=1, padx=10, pady=10)

        self.From = Label(self.Air, text=" Check-In", font=("goudy", 12, "bold")
                        , bg="white", fg="black").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.From = Entry(self.Air, font=("arial", 12), textvariable=self.Check,
                        fg="black", bg="whitesmoke", relief=GROOVE).grid(row=3, column=1, padx=10, pady=10)

        self.Seat = Label(self.Air, text=" Class", font=("goudy", 12, "bold")
                          , bg="white", fg="black").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.Seat = Entry(self.Air, font=("arial", 12), textvariable=self.Seat_Class,
                          fg="black", bg="whitesmoke", relief=GROOVE).grid(row=4, column=1, padx=10, pady=10)
        self.Luggage = Label(self.Air, text=" Luggage_Weight", font=("goudy", 12, "bold")
                          , bg="white", fg="black").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.Luggage = Entry(self.Air, font=("arial", 12), textvariable=self.LWeight,
                          fg="black", bg="whitesmoke", relief=GROOVE).grid(row=5, column=1, padx=10, pady=10)


           ################         FRAME           ###################################################

        self.Inv = LabelFrame(self.window, bg="white", fg="black",font=("arial", 15, "bold"))
        self.Inv .place(x=361, y=150, width=820, height=380)
        self.bill_title = Label(self.Inv , text="Invoice", font=("arial", 15, "bold")).pack(fill=X)
        self.scroll_y = Scrollbar(self.Inv , orient=VERTICAL)
        self.textarea = Text(self.Inv , yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)
        self.welcome()
################################# FRAME FOR ENTRY#############################
        self.ent = LabelFrame(self.window, bg="white", fg="black",
                    font=("arial", 15, "bold"))
        self.ent.place(x=0, y=400, width=360, height=140)

        self.Frame_banner = Frame(self.ent, bg="dark red")
        self.Frame_banner.place(x=0, y=0, height=10, width=2000)

        self.Frame_banner = Frame(self.ent, bg="medium blue")
        self.Frame_banner.place(x=0, y=8, height=7, width=2000)

        self.tot = Label(self.ent, text="Total Rs:", bg="white", fg="black",
                font=("arial", 20, "bold")).place(x=0,y=30)
        self.tot = Entry(self.ent, width=18, bg="whitesmoke", fg="black", textvariable=self.amount,
                font=("arial", 15, "bold")).place(x=130,y=35)

        self.bil_btn = Button(self.ent, text="Print Bill", command=self.particulars, width=8, font=("arial", 15, "bold"))
        self.bil_btn.place(x=245,y=80)




#############FRAME###############################################

        self.sb = LabelFrame(self.window, bg="blue", fg="black", font=("arial", 15, "bold"))
        self.sb.place(x=360, y=85, width=820, height=65)

        self.Search_entry = Entry(self.sb, width=14, textvariable=self.bill_no, font=("arial", 15, "bold")).place(x=500,y=5)
        self.bil_btn = Button(self.sb, text="Search Bill", width=8, font=("arial", 15, "bold"),command=self.find_bill)
        self.bil_btn.place(x=700,y=5)

       #############################FUNCTION###############################

    def welcome(self):
        self.textarea.delete('1.0', END)
        self.textarea.insert(
            END, "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank You For Choosing Nepal Airlines")

        self.textarea.insert(END, f"\t\t\t\t\t\t\t\t\tPassportNo:{self.passn.get()}")
        self.textarea.insert(END, f"\n Full-Name:{self.fname.get()}")
        self.textarea.insert(END, f"\t\t\t\t\t\t\t\tDestination.:{self.Takeoff.get()}")
        self.textarea.insert(END, f"\t\t\t\t\t\t\t\t\tBill No.:{self.bill_no.get()}")
        self.textarea.insert(END, f"\t\t\t\t\t\t\t\t\t\tCheck-In.:{self.Check.get()}")
        self.textarea.insert(END,
                             f"\n---------------------------------------------------------------------------------------------------")
        self.textarea.insert(END, f"\nSeat_Class\t\t\t\t\t\t\t\t\t\t\t:{self.Seat_Class.get()}")
        self.textarea.insert(END, f"\nLuggage_Weight\t\t\t\t\t\t\t\t\t\t\t:{self.LWeight.get()}")
        self.textarea.insert(END,
                             f"\n---------------------------------------------------------------------------------------------------")

        self.textarea.insert(END, f"\n PARTICULARS\t\t\t\t\t\t\t\t\t\t\tAMOUNT")
        self.textarea.insert(END, f"\n\nTotal Amount\t\t\t\t\t\t\t\t\t\t\t:{self.amount.get()}")

        self.textarea.insert(END,
                             f"\n---------------------------------------------------------------------------------------------------")





    def particulars(self):
        if self.passn.get() == "" or self.fname.get() == "" or self.Takeoff.get() == "" or self.Check.get() =="" or self.LWeight.get() =="" or \
                self.Seat_Class.get() =="" or self.amount.get() =="":
            messagebox.showerror("ERROR", ("Fill the box First"))
        else:
            self.welcome()
            self.textarea.insert(END,
                                 f"\n-------------------------------------------****THANK YOU****-------------------------------------")
        self.save_bill()

    def save_bill(self):
            op = messagebox.askyesno("Save Bill","Do You Want TO Save The Bill?")
            if op>0:
                self.bill_data = self.textarea.get('1.0', END)
                f = open("BILLS/"+str(self.bill_no.get())+".txt","w")
                f.write(self.bill_data)
                f.close()
                messagebox.showinfo("Success", f"\nYour bill {self.bill_no.get()} has been saved successfully")

    def find_bill(self):
        present = "no"
        for i in os.listdir("BILLS/"):
            if i.split('.')[0] == self.bill_no.get():
                f = open(f"BILLS/{i}","r")
                self.textarea.delete("1.0", END)
                for d in f:
                    self.textarea.insert(END, d)
                f.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("ERROR","Bill not Found!!!")


# obj = bill()


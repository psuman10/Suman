import tkinter
from tkinter import messagebox
from tkinter import *
from Backend import air_query
from Frontend import Login

class registration:
    def __init__(self):
        self.window = Tk()
        self.window.title("Registration Form")
        self.window.configure(background='black')
        self.window.geometry("500x500+500+200")
        self.frame_heading = Frame(self.window)
        self.frame_heading.pack()
        self.label_name = Label(self.frame_heading, bg='black', fg='white', text="Registration Form",
                                font=('Comic Sans MS', 28, 'bold'))

################FRAME###############################
        self.label_name.pack()
        self.frame_login = Frame(self.window, bg='black')
        self.frame_login.pack()

############LABEL AND ENTRY USERNAME#################################################

        self.label_un = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white', text="Username:")
        self.label_un.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.entry_un = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_un.grid(row=0, column=1, padx=10, pady=10)



##########################################LABEL AND ENTRY PASSWORD#############################
        self.label_pw = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white', text="Password:")
        self.label_pw.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_pw = Entry(self.frame_login, show='*', font=('arial', 10, 'bold'))
        self.entry_pw.grid(row=1, column=1, padx=10, pady=10)

 ##############################LABEL AND ENTRY FULL NAME########################################
        self.label_n = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white', text="Full Name:")
        self.label_n.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.entry_n = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_n.grid(row=2, column=1, padx=10, pady=10)

###########################LABEL AND ENTRY ADDRESS################################################
        self.label_a = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white', text="Address:")
        self.label_a.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.entry_a = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_a.grid(row=3, column=1, padx=10, pady=10)

#######################################LABEL AND ENTRY COUNTRY###########################################
        self.label_p = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white', text="Country:")
        self.label_p.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.entry_p = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_p.grid(row=4, column=1, padx=10, pady=10)

############################################ LABEL AND ENTRY EMAIL###########################################
        self.label_e = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white', text="Email:")
        self.label_e.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.entry_e = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_e.grid(row=5, column=1, padx=10, pady=10)

###################################LABEL AND ENTRY PASSPORT NO##############################
        self.label_t = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black', fg='white',
                             text="Passport No:")
        self.label_t.grid(row=6, column=0, padx=10, pady=10, sticky=W)

        self.entry_t = Entry(self.frame_login, font=('arial', 10, 'bold'))
        self.entry_t.grid(row=6, column=1, padx=10, pady=10)

#################BUTTON#################################################################

        self.btn_regis = Button(self.frame_login, bg='black', fg='white', command=self.submit, text="Submit",
                                font=('Calibri', 20, 'bold'))
        self.btn_regis.grid(row=7, column=1)
        self.btn_back = Button(self.frame_login, bg='black', fg='white', text="Back", command=self.back,
                               font=('Calibri', 20, 'bold'))
        self.btn_back.grid(row=7, column=0)
        self.btn_reset = Button(self.frame_login, text='Reset', bg='black', font=('Calibri', 20, 'bold'), fg='white',
                                command=self.reset)
        self.btn_reset.grid(row=7, column=2)
        self.window.mainloop()

#######################################FUNCTION##############################

    def reset(self):
        """ It reset all the values and make the bracket empty """
        try:
            if self.entry_un.get() != '' and self.entry_pw.get() != '' and self.entry_n.get() != '' and \
                    self.entry_a.get() != '' and self.entry_p.get() != '' and self.entry_e.get() != '' and self.entry_t.get() != '':
                self.entry_un.delete(0, END)
                self.entry_pw.delete(0, END)
                self.entry_n.delete(0, END)
                self.entry_a.delete(0, END)
                self.entry_p.delete(0, END)
                self.entry_e.delete(0, END)
                self.entry_t.delete(0, END)
            else:
                tkinter.messagebox.showerror('Error', 'Please Fill The All Boxes.')

        except Exception as e:
            print(e)

    #######################################FUNCTION##############################
    def back(self):
        try:
            messagebox.showinfo('Back', 'Welcome Back To The Login In Page ')
            self.window.destroy()
            import login
        except Exception as e:
            print(e)

    #######################################FUNCTION##############################

    def submit(self):
            if self.entry_un.get() == '' or self.entry_pw.get() == '' or self.entry_n.get() == '' or self.entry_a.get() == '' or self.entry_p.get() == '' or \
                    self.entry_e.get() == '':
                messagebox.showwarning('Error', 'Fill All the Boxes Properly')
            else:
                air_query.Airline().signup(

                        self.entry_un.get(),
                        self.entry_pw.get(),
                        self.entry_n.get(),
                        self.entry_a.get(),
                        self.entry_t.get(),
                        self.entry_p.get(),
                        self.entry_e.get())
                messagebox.showinfo('Success', 'Registered Successfully')
                self.window.destroy()
                Login.Login()

# registration()
# # self.window.destroy()
# # Login.LoginView()

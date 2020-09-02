from tkinter import *
from tkinter import messagebox
from Backend import air_query
from Frontend import Register, Inquiry


class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title("Admin Login")
        self.window.configure(background='black')
        self.show = False
        self.window.geometry("400x300+500+200")
##############FRAME######################################
        self.frame = Frame(self.window)
        self.frame.pack()
        self.username = StringVar()
        self.password = StringVar()
        self.label_name = Label(self.frame, bg='black',fg='white', text="Admin Login",  font=('Comic Sans MS', 28, 'bold'))
        self.label_name.pack()
        self.frame_login = Frame(self.window, bg='black')
        self.frame_login.pack()

        ####### USERNAME############
        self.label_userN = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black',fg='white', text="Username")
        self.label_userN.grid(row=0, column=0, pady=10, padx=10, sticky=W)
        self.entry_userN = Entry(self.frame_login, textvariable=self.username, font=('arial', 10, 'bold'))
        self.entry_userN.grid(row=0, column=1, padx=10, pady=10)



        ############PASSWORD#########################################
        self.label_passW = Label(self.frame_login, font=('Calibri', 15, 'bold'), bg='black',fg='white', text="Password")
        self.label_passW.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.entry_passW = Entry(self.frame_login, show='*', textvariable=self.password, font=('arial', 10, 'bold'))
        self.entry_passW.grid(row=1, column=1, padx=10, pady=10)

        ###########BUTTON############################
        self.btn_login = Button(self.frame_login, bg='black',fg='white', text="Log In", font=('Calibri', 20, 'bold'),
                                command=self.on_login_click)
        self.btn_login.grid(row=2, column=0)
        self.btn_regis = Button(self.frame_login, bg='black',fg='white', text="Sign Up", font=('Calibri', 20, 'bold'),
                                command=self.signup)
        self.btn_regis.grid(row=2, column=1)

#################SHOWPASS BUTTON###############################################################
        self.showpass = Button(self.frame_login, text='show', bg='orange', fg='black', font=('Comic Sans MS', 8, 'bold'),
                               command=self.showpasswo, bd=5, activebackground='white', )
        self.showpass.place(x=240,y=60)
        self.window.mainloop()

#########################FUNCTION#################################################################

    def showpasswo(self):
        """  It shows and hide the password clicking show button"""
        if self.show == True:
            self.entry_passW.configure(show="*")
            self.show = False
        else:
            self.entry_passW.configure(show="")
            self.show = True

#####################FUNCTION##########################################################################

    def on_login_click(self):
        """It handle the sign in"""
        if self.entry_userN.get() == '' or self.entry_passW.get() == '':
            messagebox.showwarning('Error', 'All Fields Are Required')
        else:
                user = air_query.Airline().login(self.entry_userN.get(), self.entry_passW.get())
                if user:
                    messagebox.showinfo('Success', 'Welcome')
                    self.window.destroy()
                    Inquiry.Inquiry_Page()
                else:
                    messagebox.showerror('Error', 'Invalid Id Or Password')

#####################FUNCTION#######################################################################

    def signup(self):
        try:
            op = messagebox.askyesno("Registration Form", "Are you sure, you want to open Registration Form?")
            if op > 0:
                self.window.destroy()
                Register.registration()
            else:
                return False
        except Exception as e:
            print(e)
Login()






































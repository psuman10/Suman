from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
from Frontend import Main_Interface


class Inquiry_Page():
    def __init__(self):
        self.window=Tk()
        self.window.geometry("800x280")
        self.user_name = StringVar()
        self.ent_email_value = StringVar()
        self.ent_pass_value = StringVar()
        self.ent_pass2_value = StringVar()
        self.ent_name1_value = StringVar()
        self.ent_name2_value = StringVar()
        self.ent_add_value = StringVar()
        self.ent_con_value = StringVar()

        self.Label = Label(self.window, text="Welcome to Flight Inquiry System", font=("algerian", 20), fg="Red", width=46,
                       bg="White").grid(row=0, column=0, columnspan=4)


        #############PICKUP POINT#######################
        self.sos = Label(self.window, text="Select Pick Up Point", font=("algerian", 15,), fg="Red", bg="Black").grid(row=2,
                                                                                                               column=1)
        self.variable = StringVar(self.window)
        self.variable.set("Select Source")
        self.w = OptionMenu(self.window, self.variable, "New York",   "kathmandu-Nepal","sydney", "brisbane","Delhi" )
        self.w.grid(row=2, column=2)

        ##################BOARDING POINT###########################
        self.sos=Label(self.window, text="Select Boarding Point", font=("algerian", 15,), fg="Red", bg="Black").grid(row=3, column=1)
        self.variable1 = StringVar(self.window)
        self.variable1.set("Select Destination")
        self.w = OptionMenu(self.window, self.variable1, "New York",   "kathmandu-Nepal","sydney", "brisbane",  "Delhi")
        self.w.grid(row=3, column=2)

##################CLASS##############################

        self.cl = Label(self.window, text="Seat/ Class:", font=("algerian", 15,), fg="Red", bg="Black").grid(
            row=4, column=1)
        self.variable2 = StringVar(self.window)
        self.variable2.set("Select Class")  # default value
        self.w = OptionMenu(self.window, self.variable2, "1st-class", "Economy-class", "Business-class")
        self.w.grid(row=4, column=2)

        ###############SHOW FLIGHTS BUTTON#####################################

        self.Button = Button(self.window, text="Signup to Book", fg="white", bg="blue", font=("algerian", 14), bd=8,command=self.siggn
                             ).grid(row=7,columnspan=5)
        self.Button = Button(self.window, text="Show Flights", font=("algerian", 14), fg="white", bg="Black", bd="8",compound="center",command=self.flights
                             ).grid(row=6, columnspan=1)

#####################################FLIGHT INFORMATION#########################################

    def flights(self):
                                #####NOT----KATHMANDU---TO Newyork
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "New York"and self.variable2.get() == "1st-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "New York" and self.variable2.get() == "Business-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "New York" and self.variable2.get() == "Economy-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

                             #########    NOT   DELHI TO Sydney
        if self.variable.get() == "Delhi" and self.variable1.get() == "sydney"and self.variable2.get() == "1st-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

        if self.variable.get() == "Delhi" and self.variable1.get() == "sydney" and self.variable2.get() == "Business-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "Delhi" and self.variable1.get() == "sydney" and self.variable2.get() == "Economy-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

                    ###### NOT SYDNEY TO-------- Delhi
        if self.variable.get() == "sydney" and self.variable1.get() == "Delhi"and self.variable2.get() == "1st-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "sydney" and self.variable1.get() == "Delhi" and self.variable2.get() == "Business-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "sydney" and self.variable1.get() == "Delhi" and self.variable2.get() == "Economy-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

            ###### NOT SYDNEY TO-------- Newyork
        if self.variable.get() == "sydney" and self.variable1.get() == "New York" and self.variable2.get() == "1st-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "sydney" and self.variable1.get() == "New York" and self.variable2.get() == "Business-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "sydney" and self.variable1.get() == "New York" and self.variable2.get() == "Economy-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

            ######### NOT BRISBANE TO ------------- DElhi
        if self.variable.get() == "brisbane" and self.variable1.get() == "Delhi" and self.variable2.get() == "1st-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "brisbane" and self.variable1.get() == "Delhi" and self.variable2.get() == "Business-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "brisbane" and self.variable1.get() == "Delhi" and self.variable2.get() == "Economy-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

            ######### NOT BRISBANE TO ------------- Newyork
        if self.variable.get() == "brisbane" and self.variable1.get() == "New York" and self.variable2.get() == "1st-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "brisbane" and self.variable1.get() == "New York" and self.variable2.get() == "Business-class":
            showerror('Oops!', "Sorry No direct flights available for this root")
        if self.variable.get() == "brisbane" and self.variable1.get() == "New York" and self.variable2.get() == "Economy-class":
            showerror('Oops!', "Sorry No direct flights available for this root")

                ###### KATHMANDU TO---------------------- brisbane
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "brisbane" and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="3", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                            ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to brisbane is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4,column=3)
         ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "brisbane" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="85", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
            ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to brisbane is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4,column=3)
                        #####################        BUSINESS CLASS################################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "brisbane" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="5", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to brisbane is:", font=("algerian", 13,), fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)


                    ###### KATHMANDU TO---------------------- Sydney
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "sydney" and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Sydney is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,  column=3)
            ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "sydney" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Sydney is:", font=("algerian", 13,), fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)

            ####################        BUSINESS CLASS################################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "sydney" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Sydney is:", font=("algerian", 13,), fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)






            ###### KATHMANDU TO---------------------- delhi
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "Delhi" and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Delhi is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,  column=3)
            ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "Delhi" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Delhi is:", font=("algerian", 13,), fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
            ####################        BUSINESS CLASS################################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "Delhi" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Delhi is:", font=("algerian", 13,), fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)



##############################   NEW YORK TO----------------------- ktm nepal

        if self.variable.get() == "New York" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="150000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "New York" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="35", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "New York" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",  bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="12", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="105000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)






##############################   NEW YORK TO----------------------- sydney

        if self.variable.get() == "New York" and self.variable1.get() == "sydney"and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to sydney is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="40", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to kathmandu-Nepal is:", font=("algerian", 13,),fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="45000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,  columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="11", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of kathmandu-Nepal to Delhi is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)


##############################   NEW YORK TO----------------------- brisbane

        if self.variable.get() == "New York" and self.variable1.get() == "brisbane"  and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to brisbane is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "New York" and self.variable1.get() == "brisbane" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to brisbane is:", font=("algerian", 13,),fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "New York" and self.variable1.get() == "brisbane" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")

            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of New York to brisbane is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)





##############################   DELHI TO----------------------- ktm nepal
        if self.variable.get() == "Delhi" and self.variable1.get() == "kathmandu-Nepal"and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "Delhi" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
            ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to kathmandu-Nepal is:", font=("algerian", 13,),fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "Delhi" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)


##############################   DELHI TO-----------------------  Newyork
        if self.variable.get() == "Delhi" and self.variable1.get() == "New York" and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to New York is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "Delhi" and self.variable1.get() == "New York" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
               ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to New York is:", font=("algerian", 13,),fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4, column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "Delhi" and self.variable1.get() == "New York" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to New York is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4,column=3)



            ##############################   DELHI TO----------------------- brisbane
        if self.variable.get() == "Delhi" and self.variable1.get() == "brisbane"and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to brisbane is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)

            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "Delhi" and self.variable1.get() == "brisbane" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to brisbane is:", font=("algerian", 13,), fg="black",  bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "Delhi" and self.variable1.get() == "brisbane" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)

            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of Delhi to brisbane is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4,column=3)












##############################   SYDNEY TO----------------------- kathmandu nepal
        if self.variable.get() == "sydney" and self.variable1.get() == "kathmandu-Nepal"and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of sydney to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "sydney" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of sydney to kathmandu-Nepal is:", font=("algerian", 13,),fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "sydney" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)

            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of sydney to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)


##############################   SYDNEY TO----------------------- brisbane
        if self.variable.get() == "sydney" and self.variable1.get() == "brisbane"and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,  column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of sydney to brisbane is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "sydney" and self.variable1.get() == "brisbane" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of sydney to brisbane is:", font=("algerian", 13,),fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "sydney" and self.variable1.get() == "brisbane" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of sydney to brisbane is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)


##############################   BRISBANE TO----------------------- ktm nepal
        if self.variable.get() == "brisbane" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of brisbane to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "brisbane" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of brisbane to kathmandu-Nepal is:", font=("algerian", 13,), fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4, column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "brisbane" and self.variable1.get() == "kathmandu-Nepal" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")

            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)

            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of brisbane to kathmandu-Nepal is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)


##############################   BRISBANE TO sydney
        if self.variable.get() == "brisbane" and self.variable1.get() == "sydney"and self.variable2.get() == "1st-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of brisbane to sydney is:", font=("algerian", 13,), fg="black",
                      bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="110000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)
                ###############          ECONOMY CLASS              #####################
        if self.variable.get() == "brisbane" and self.variable1.get() == "sydney" and self.variable2.get() == "Economy-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="25", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4, column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of brisbane to sydney is:", font=("algerian", 13,),fg="black", bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="65000", font=("algerian", 14,), fg="black", bg="white").grid(row=6, columnspan=4,column=3)
                ####################        BUSINESS CLASS################################
        if self.variable.get() == "brisbane" and self.variable1.get() == "sydney" and self.variable2.get() == "Business-class":
            messagebox.showinfo("flight found")
            Label(self.window, text="Number of Seats Available are:", font=("algerian", 15,), fg="black",
                      bg="white").grid(row=5, columnspan=4, column=0)
            Label(self.window, text="2", font=("algerian", 15,), fg="black", bg="white").grid(row=5, columnspan=4,column=2)
                ######################AMOUNT############################
            Label(self.window, text="Amount of brisbane to sydney is:", font=("algerian", 13,), fg="black",bg="white").grid(row=6, columnspan=5)
            Label(self.window, text="95000", font=("algerian", 14,), fg="black", bg="white").grid(row=6,columnspan=4,column=3)





################### SAME DESTIANTION----------------------


        if self.variable.get() == "New York" and self.variable1.get() == "New York":
            showerror('Oops!', "Sorry can't choose same destination")

        if self.variable.get() == "kathmandu-Nepal" and self.variable1.get() == "kathmandu-Nepal":
            showerror('Oops!', "Sorry can't choose same destination")
        if self.variable.get() == "Delhi" and self.variable1.get() == "Delhi":
            showerror('Oops!', "Sorry can't choose same destination")

        if self.variable.get() == "sydney" and self.variable1.get() == "sydney":
            showerror('Oops!', "Sorry can't choose same destination")
        if self.variable.get() == "brisbane" and self.variable1.get() == "brisbane":
            showerror('Oops!', "Sorry can't choose same destination")


    def siggn(self):
        messagebox.showinfo('Success', 'Welcome To The Registration Form')
        self.window.destroy()
        self.iv=Main_Interface.Airline()



# def main():
#     a= Tk()
#     Inquiry(y)
#     y.mainloop()
#
# if __name__ == '__main__':
#     main()
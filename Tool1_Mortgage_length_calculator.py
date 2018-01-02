
# coding: utf-8

# # Calculates repayment time given some inputs

# In[5]:


## Author: Andrew M. Telford
## Version: 1.0
## Date: 02/01/2018

## Simple application to calculate the length of a mortgage based on a fixed
## interest rate and fixed monthly repayments

from tkinter import *
from math import log

class App:

    def __init__(self, master): 
        ## Sets up a master frame with 2 columns and 4 rows. The left columns 
        ## contains labels of each field; the right column contains the
        ## fillable boxes.

        ## Frame setup: creates a second frame to hold the interactive buttons 
        ## CALCULATE and QUIT
        self.frame = Frame(master, bd=3, relief=SUNKEN) 
        self.frame.pack()
        
        ## Setup of first row: amount borrowed (input)
        Label(self.frame, text="Amount borrowed: ").grid(row=0, column=0)
        self.borrowed = Entry(self.frame)
        self.borrowed.grid(row=0, column=1)
        
        ## Setup of second row: annual interest (input)
        Label(self.frame, text="Annual interest (fixed): ").grid(row=1, column=0)
        self.annual_interest = Entry(self.frame)
        self.annual_interest.grid(row=1, column=1)
        
        ## Setup of third row: monthly repayments (input)
        Label(self.frame, text="Monthly repayment: ").grid(row=2, column=0)
        self.monthly_repay = Entry(self.frame)
        self.monthly_repay.grid(row=2, column=1)
        
        ## Setup of forth row: years to full repayment (output)
        self.result = StringVar()
        Label(self.frame, text="Years to full repayment: ").grid(row=3, column=0)
        Entry(self.frame, textvariable=self.result, bg="light grey").grid(row=3, column=1)
        
        ## Setup of CALCULATE button action
        self.calculate = Button(
            self.frame, text="CALCULATE", fg="black",
            font=("Times", 10, "bold"),
            command=self.Calculate
            ) 
        self.calculate.grid(row=0, column=2)        
        
        ## Setup of QUIT button action
        self.exit = Button(
            self.frame, text="QUIT", fg="red",
            font=("Times", 10, "bold"),
            command=self.frame.quit
            )
        self.exit.grid(row=1, column=2)
                

    def Calculate(self):
        monthly_interest = float(self.annual_interest.get())/1200 ## Divide by 100 and by 12
        output = 1/12 * -log(1 - monthly_interest * float(self.borrowed.get()) / float(self.monthly_repay.get())) / log(1 + monthly_interest)
        self.result.set(str("%.2f" %output)) 

root = Tk()
app = App(root)
root.mainloop()
root.destroy() # Required in Windows! Otherwise the app cannot be exited.


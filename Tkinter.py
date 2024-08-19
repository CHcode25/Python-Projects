

import tkinter as tk
from tkinter import ttk


# frame of Tip Calculator GUI
class TipCalcFrame(ttk.Frame):
    def __init__(self, parent): #main constructor for the class

        ttk.Frame.__init__(self, parent, padding="20 20 20 20")
        self.pack()

        self.mealCost = tk.StringVar() 
        self.tipPercent = tk.IntVar()
        self.tiptotal = tk.StringVar()
        self.billtotal = tk.StringVar()


        ttk.Label(self, text="***TIP CALCULATOR***").grid(column=1, row=0, sticky=tk.E) #sets the name on the border

        ttk.Label(self, text="Cost of Meal").grid(column=0, row=1, sticky=tk.E) #label for box 1
        ttk.Entry(self, width=30, textvariable=self.mealCost).grid(column=1, row=1)
        # tk.Entry(self, width=30, textvariable=self.mealCost).grid(column=1, row=1, command=lambda:Do_Something.testing)


        ttk.Label(self, text="Tip Percent").grid(column=0, row=2, sticky=tk.E) #label for box 2
        #ttk.Entry(self, width=30, textvariable=self.tipPercent).grid(column=1, row=2)
        ttk.Entry(self, width=30, textvariable=self.tipPercent, state="readonly").grid(column=1, row=2)

        ttk.Label(self, text="Totol Tip").grid(column=0, row=3, sticky=tk.E) #label for box 3
        #ttk.Entry(self, width=30, textvariable=self.tiptotal).grid(column=1, row=2)
        ttk.Entry(self, width=30, textvariable=self.tiptotal, state="readonly").grid(column=1, row=3)

        ttk.Label(self, text="Total Bill").grid(column=0, row=4, sticky=tk.E) #label for box 4
        #ttk.Entry(self, width=30, textvariable=self.billtotal, state="readonly").grid(column=1, row=2)
        ttk.Entry(self, width=30, textvariable=self.billtotal, state="readonly").grid(column=1, row=4)

        ttk.Button(self, text="Calculate",command=self.calculate).grid(column=1, row=5, sticky=tk.E) #box 5 when press calculates executes box 1-4

        ttk.Label(self, text="Tip Percent:").grid(column=2, row=1, sticky=tk.E)
        ttk.Radiobutton(self, text="10%", variable = self.tipPercent,value = 15).grid(column=2, row=2, sticky=tk.E)
        ttk.Radiobutton(self, text="15%", variable = self.tipPercent,value = 18).grid(column=2, row=3, sticky=tk.E)
        ttk.Radiobutton(self, text="18%", variable = self.tipPercent,value = 20).grid(column=2, row=4, sticky=tk.E)


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def calculate(self):

        tip = self.tipPercent.get() #sets the tip percent for box 2
        tiptotal = round(float(self.mealCost.get()) * (tip/100),2) #takes the cost of box 1 mutiples it against tip variable and divide by 100
        total = round(float(self.mealCost.get()) + tiptotal,2) #takes the cost of box 1 and adds tiptotal variable

        self.tiptotal.set("$ " + str(tiptotal)) #converts tiptotal to string 
        self.billtotal.set("$ " + str(total)) #converts billtotal to string

  #Main program that will call the class TipCalcFrame  
def main():
    tipcalculator = tk.Tk() #calls the Tkinter gui

    tipcalculator.title("Tip Calculator")

    TipCalcFrame(tipcalculator) #calls the class and passes through tipcalculator object
    tipcalculator.mainloop()

if __name__ == "__main__":
    main()


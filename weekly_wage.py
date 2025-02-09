"""
Lab Activity: Final Assignment
Author: Aakrosh Rai 
Programme discription: Provides a GUI-based program of weekly pay. It takes hourly wage, regular hours and
overtime as input.
"""
from tkinter import *
from tkinter.messagebox import *
class WeeklyWage(Frame):

    def __init__(self):
        """Sets up the window and widgets."""
        Frame.__init__(self)
        self.master.title("Hourly Wage")
        self.grid()

        # Label and field for the hourly wage
        self._hourlyWageLable = Label(self,text = "Hourly wage")
        self._hourlyWageLable.grid(row = 0, column = 0)
        self._hourlyWageVar = DoubleVar()
        self._hourlyWageEntry = Entry(self,
                                  textvariable = self._hourlyWageVar)
        self._hourlyWageEntry.grid(row = 0, column = 1)

        # Label and field for the regular hours
        self._regularHourLabel = Label(self, text = "Regular hours")
        self._regularHourLabel.grid(row = 1, column = 0)
        self._regularHourVar = DoubleVar()
        self._regularHourEntry = Entry(self,
                                textvariable = self._regularHourVar)
        self._regularHourEntry.grid(row = 1, column = 1)
        #Lable and Field for the overtime
        self._overtimeLabel = Label(self, text = "Overtime hours")
        self._overtimeLabel.grid(row = 2, column = 0)
        self._overtimeVar = DoubleVar()
        self._overtimeEntry = Entry(self,
                                textvariable = self._overtimeVar)
        self._overtimeEntry.grid(row = 2, column = 1)

        #Lable and Field for the weekly pay
        self._weeklyLabel = Label(self, text = "Weekly pay")
        self._weeklyLabel.grid(row = 3, column = 0)
        self._weeklyVar = DoubleVar()
        self._weeklyEntry = Entry(self,
                                textvariable = self._weeklyVar)
        self._weeklyEntry.grid(row = 3, column = 1)
        
        # The command buton
        self._button = Button(self,
                              text = "Compute",
                              command = self._weeklyPay)
        self._button.grid(row = 4, column = 0, columnspan = 4)

    def _weeklyPay(self):
        """Event handler for the button."""
        #Calculate and displays the weekly pay.
        try:
            hourlyWage = self._hourlyWageVar.get()
            regularHour = self._regularHourVar.get()
            overtime = self._overtimeVar.get()
            weeklyPay = (hourlyWage * regularHour) + (overtime * (1.5 * hourlyWage))
            self._weeklyVar.set(weeklyPay)
        except:
            showerror(message = "Error: Bad format",
                                 parent = self)

def main():
    """Instantiate and pop up the window."""
    WeeklyWage().mainloop()

main()

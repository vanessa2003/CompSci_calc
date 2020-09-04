#program name Mathscalc.py
#allows user to solve a few simple and complex maths problems



from tkinter import *
name = input("what is your name? ")

#function to do simple addition
def addition():
    label.config (text = "Hello!")

#function to do simple subtraction
def subtraction():
    label.config (text = "Goodbye!")
#function to add two matrices together
def add_matrices():
    label.config (text = "go away")
#function to subtract two matrice
def subtract_matrices():
    label.config (text = "stay")





#creates a fixed size menu option for calculator
calc = Tk()
#gives the menu a title
calc.title("Maths calculator")
#sets the fixed size of the menu
calc.geometry("530x200")
#doesnt allow for the size of the menu to be changed during use
calc.resizable (False, False)
#sets the colour of the menu background to pink
calc.configure(background = "pink")
#adds a label that greets the user and initialises where the label should be and how it looks
label = Label(calc, text = ("Hello",name))
label.grid(row = 0, column = 21, padx = 20, pady = 20)
#creates buttons that show users the different operations available and sets where they are on the menu and the size of each button
button1 = Button(calc, text = "Addition", width = 9, command = addition)
button1.grid(row = 1, column = 20, padx = 20)
button2 = Button(calc, text = "Subtraction", width = 9, command = subtraction)
button2.grid(row = 1, column = 22, padx = 20)
button3 = Button(calc, text = "Add matrices", width = 15, command = add_matrices)
button3.grid(row = 3, column = 20, padx = 20)
button4 = Button(calc, text = "Subtract matrices", width = 15, command = subtract_matrices)
button4.grid(row = 3, column = 22, padx = 20)
instruction = Label(calc, text = "Choose an operation to carry out")
instruction.grid(row = 4, column = 21, padx = 20, pady = 20)


#program runs continuously until user closes it 
calc.mainloop()





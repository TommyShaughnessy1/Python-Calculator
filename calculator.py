from tkinter import *
# this is from the clone
 
 # Holds value for text box.
expression = ""
 
 #Metohd for when (num) is pressed (num) is concatenated to expression
def press(num):
    
    global expression
 
 #num is concatenated to expression
    expression = expression + str(num)

# expression value is set to equation 
    equation.set(expression)

 # function for when '=' is pressed
def equalpress():
    
    try:
 
        global expression

        #takes string as expression and determines its value
        total = str(eval(expression))
 
        equation.set(total)
 
    except:
 
        equation.set(" error ")
        expression = ""
 
def clear():
    global expression
    expression = ""
    equation.set("")
 
 
if __name__ == "__main__":
    # reference to parent window.
    gui = Tk()
 
   
    gui.configure(background="light green")
 
   
    gui.title("Calculator")
 
    
    gui.geometry("270x150")
 
    
    # instance of the StringVar class 
    # StringVar manages value of widget
    equation = StringVar()
 
    # Entry(parent window = "gui", text variable(which needs to be set to
    #  Instance of String Var class to retrieve text from entry widget) = equation)
    expression_field = Entry(gui, textvariable=equation) 
 
    # columnspan how many columns Widget occupies
    # ipadx how many pixels to pad widget
    expression_field.grid(columnspan=4, ipadx=70)
 
    # Button(parent window = gui , command = function carried out when button is clicked)
    # command lambda 
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
 
    gui.mainloop()




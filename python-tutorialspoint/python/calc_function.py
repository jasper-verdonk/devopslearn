from tkinter import *

def calculator(frame):

    text_Input = StringVar()
    operator = ""

    def btnClick(numbers):
        nonlocal operator
        operator += str(numbers)
        text_Input.set(operator)

    def btnClearDisplay():
        nonlocal operator
        operator = ""
        text_Input.set(operator)

    def btnEquals():
        nonlocal operator
        total = str(eval(operator))
        text_Input.set(total)



    txtDisplay = Entry(frame, 
                    bd = 30, 
                    font = ('arial', 20, 'bold'),
                    insertwidth = 4, 
                    bg = 'light blue', 
                    justify = 'right',
                    textvariable = text_Input).grid(columnspan = 4)

    btnClear = Button(frame,
                    padx = 59,
                    pady = 15,
                    bd = 8,
                    font = ('arial', 20, 'bold'),
                    text = 'C', 
                    bg = 'light blue',
                    command = btnClearDisplay).grid(row = 1, columnspan = 2)

    btnbracket1 = Button(frame, 
                        padx = 19,
                        pady = 15, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "(", 
                        bg = 'light blue', 
                        command = lambda: btnClick("(")).grid(row = 1, column = 2)

    btnbracket2 = Button(frame, 
                        padx = 19,
                        pady = 15, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = ")", 
                        bg = 'light blue', 
                        command = lambda: btnClick(")")).grid(row = 1, column = 3)

    btn7 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "7", 
                        bg = 'light blue', 
                        command = lambda: btnClick(7)).grid(row = 2, column = 0)

    btn8 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "8", 
                        bg = 'light blue', 
                        command = lambda: btnClick(8)).grid(row = 2, column = 1)

    btn9 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "9", 
                        bg = 'light blue', 
                        command = lambda: btnClick(9)).grid(row = 2, column = 2)

    division = Button(frame, 
                        padx = 19,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "/", 
                        bg = 'light blue', 
                        command = lambda: btnClick("/")).grid(row = 2, column = 3)

    btn4 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "4", 
                        bg = 'light blue', 
                        command = lambda: btnClick(4)).grid(row = 3, column = 0)

    btn5 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "5", 
                        bg = 'light blue', 
                        command = lambda: btnClick(5)).grid(row = 3, column = 1)

    btn6 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "6", 
                        bg = 'light blue', 
                        command = lambda: btnClick(6)).grid(row = 3, column = 2)

    substraction = Button(frame, 
                        padx = 19,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "-", 
                        bg = 'light blue', 
                        command = lambda: btnClick("-")).grid(row = 3, column = 3)

    btn1 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "2", 
                        bg = 'light blue',
                        command = lambda: btnClick(2)).grid(row = 4, column = 0)

    btn2 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "5", 
                        bg = 'light blue', 
                        command = lambda: btnClick(5)).grid(row = 4, column = 1)

    btn3 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "6", 
                        bg = 'light blue', 
                        command = lambda: btnClick(6)).grid(row = 4, column = 2)

    multiplication = Button(frame, 
                        padx = 19,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "*", 
                        bg = 'light blue', 
                        command = lambda: btnClick("*")).grid(row = 4, column = 3)

    btn0 = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "0", 
                        bg = 'light blue', 
                        command = lambda: btnClick(0)).grid(row = 5, column = 0)

    dot = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = ".", 
                        bg = 'light blue',
                        command = lambda: btnClick(".")).grid(row = 5, column = 1)

    equal = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "=", 
                        bg = 'light blue',
                        command = btnEquals).grid(row = 5, column = 2)

    addition = Button(frame, 
                        padx = 16,
                        pady = 16, 
                        bd = 8, 
                        font = ('arial', 20, 'bold'),
                        text = "+", 
                        bg = 'light blue', 
                        command = lambda: btnClick("+")).grid(row = 5, column = 3)

    return frame





   

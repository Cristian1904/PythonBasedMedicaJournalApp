from tkinter import *

root = Tk()
root.title("Simple calculator app")
entryNumbers = Entry(root, width=60, borderwidth=13)

def number_add(number):
    entryNumbers.insert(END, number)

def clear():
    entryNumbers.delete(0, END)

def addition():
    string = entryNumbers.get()
    number_list = entryNumbers.get().split('+')
    output = 0
    for i in range(len(number_list)):
        output += int(number_list[i])
    entryNumbers.delete(0, END)
    entryNumbers.insert(END, output)
    return
def backspace():
    entryNumbers.delete(len(entryNumbers.get())-1, END)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = (screen_width - root.winfo_reqwidth()) // 2
center_y = (screen_height - root.winfo_reqheight()) // 2

# Set the initial size and position of the window
root.geometry(f"600x400+{center_x}+{center_y}")    
#creating buttons

button1 = Button(root, text = "1", padx = 50, pady = 20, command=lambda: number_add(1))
button2 = Button(root, text = "2", padx = 50, pady = 20, command=lambda: number_add(2))
button3 = Button(root, text = "3", padx = 50, pady = 20, command=lambda: number_add(3))
button4 = Button(root, text = "4", padx = 50, pady = 20, command=lambda: number_add(4))
button5 = Button(root, text = "5", padx = 50, pady = 20, command=lambda: number_add(5))
button6 = Button(root, text = "6", padx = 50, pady = 20, command=lambda: number_add(6))
button7 = Button(root, text = "7", padx = 50, pady = 20, command=lambda: number_add(7))
button8 = Button(root, text = "8", padx = 50, pady = 20, command=lambda: number_add(8))
button9 = Button(root, text = "9", padx = 50, pady = 20, command=lambda: number_add(9))
button0 = Button(root, text = "0", padx = 50, pady = 20, command=lambda: number_add(0))

button_add = Button(root, text = "+", padx = 49, pady = 20, command= lambda: number_add("+"))
button_equal = Button(root, text = "=", padx = 49, pady = 20, command=lambda: addition())
button_clear = Button(root, text = "Clear", padx = 186, pady = 20, command=clear)
button_backspace = Button(root, text = "B\nA\nC\nK",padx = 16, pady = 99, command = backspace)

#putting the buttons on the screen
button1.grid(row=1 , column=0, padx = 1, pady= 2)
button2.grid(row=1 , column=1, padx = 1, pady= 2)
button3.grid(row=1 , column=2, padx = 1, pady= 2)
button4.grid(row=2 , column=0, padx = 1, pady= 2)
button5.grid(row=2 , column=1, padx = 1, pady= 2)
button6.grid(row=2, column=2, padx = 1, pady= 2)
button7.grid(row=3 , column=0, padx = 1, pady= 2)
button8.grid(row=3 , column=1, padx = 1, pady= 2)
button9.grid(row=3 , column=2, padx = 1, pady= 2)
button0.grid(row =4 , column=0, padx = 1, pady= 2)

button_add.grid(row=4, column=1, padx = 1, pady= 2)
button_clear.grid(row=5,column=0,padx = 1, pady= 2,columnspan=4)
button_equal.grid(row=4,column=2,padx = 1, pady= 2)
button_backspace.grid(row = 1 , column =3, rowspan=4, padx =1, pady = 2 )

entryNumbers.grid(row=0,column=0, columnspan=4, padx=10, pady=10)
#creating main loop, this is how the app sees the mouse updates, keyboard presses, etc

root.mainloop()

from tkinter import *

root = Tk()

entryNumbers = Entry(root, width=35, borderwidth=13)

def number_add(number):
    entryNumbers.insert(END, number)

def clear():
    entryNumbers.delete(0, END)


#creating buttons
button1 = Button(root, text = "1", padx = 40, pady = 20, command=lambda: number_add(1))
button2 = Button(root, text = "2", padx = 40, pady = 20, command=lambda: number_add(2))
button3 = Button(root, text = "3", padx = 40, pady = 20, command=lambda: number_add(3))
button4 = Button(root, text = "4", padx = 40, pady = 20, command=lambda: number_add(4))
button5 = Button(root, text = "5", padx = 40, pady = 20, command=lambda: number_add(5))
button6 = Button(root, text = "6", padx = 40, pady = 20, command=lambda: number_add(6))
button7 = Button(root, text = "7", padx = 40, pady = 20, command=lambda: number_add(7))
button8 = Button(root, text = "8", padx = 40, pady = 20, command=lambda: number_add(8))
button9 = Button(root, text = "9", padx = 40, pady = 20, command=lambda: number_add(9))
button0 = Button(root, text = "0", padx = 40, pady = 20, command=lambda: number_add(0))

button_add = Button(root, text = "+", padx = 39, pady = 20, command= lambda: number_add)
button_equal = Button(root, text = "=", padx = 39, pady = 20, command=lambda: number_add)
button_clear = Button(root, text = "Clear", padx = 130, pady = 20, command=clear)

#putting the buttons on the screen
button1.grid(row=1 , column=0, padx = 3, pady= 2)
button2.grid(row=1 , column=1, padx = 3, pady= 2)
button3.grid(row=1 , column=2, padx = 3, pady= 2)
button4.grid(row=2 , column=0, padx = 3, pady= 2)
button5.grid(row=2 , column=1, padx = 3, pady= 2)
button6.grid(row=2, column=2, padx = 3, pady= 2)
button7.grid(row=3 , column=0, padx = 3, pady= 2)
button8.grid(row=3 , column=1, padx = 3, pady= 2)
button9.grid(row=3 , column=2, padx = 3, pady= 2)
button0.grid(row =4 , column=0, padx = 3, pady= 2)

button_add.grid(row=4, column=1, padx = 3, pady= 2)
button_clear.grid(row=5,column=0,padx = 3, pady= 2,columnspan=3)
button_equal.grid(row=4,column=2,padx = 3, pady= 2)


entryNumbers.grid(row=0,column=0, columnspan=3, padx=10, pady=10)
#creating main loop, this is how the app sees the mouse updates, keyboard presses, etc

root.mainloop()

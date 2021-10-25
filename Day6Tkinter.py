# from tkinter import *

# root = Tk()
# label1 = Label(root, text="Hello World")
# label1.pack()
# root.mainloop()


# from tkinter import *

# root = Tk()

# frame1 = Frame(root)
# frame1.pack()

# frame2 = Frame(root)
# frame2.pack(side=BOTTOM)

# button1 = Button(frame1, text="Click Here", fg="Blue")
# button2 = Button(frame2, text="Click Here", fg="Black")

# button1.pack()
# button2.pack()

# root.mainloop()


# from tkinter import *

# root = Tk()

# label1 = Label(root, text="First Name")
# label2 = Label(root, text="Last Name")

# entry1 = Entry(root)
# entry2 = Entry(root)

# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)

# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# root.mainloop()


# from tkinter import *

# root = Tk()

# label1 = Label(root, text="First", bg="Black", fg="White")
# label1.pack(fill=X)

# label2 = Label(root, text="Second", bg="Red", fg="Green")
# label2.pack(side=LEFT, fill=Y)

# root.mainloop()

# from tkinter import *

# root = Tk()


# def dosomething():
#     print("Ahhh Yeee")


# button1 = Button(root, text="Click Me", command=dosomething)
# button1.pack()

# root.mainloop()


from tkinter import *


class MyButton:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(rootone, text="Click Me", command=self.printmsg)
        self.printbutton.pack()

        self.exitbutton = Button(rootone, text="Exit", command=frame.quit)
        self.exitbutton.pack()

    def printmsg(Self):
        print("Helo")


root = Tk()
b = MyButton(root)
root.mainloop()

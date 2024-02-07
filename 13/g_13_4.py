import tkinter


class MyGUI:
    def __init__(self):
        # Create main window widget
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text='Hello, World')
        self.label1 = tkinter.Label(self.main_window, text='It is my first GUI-programm')

        self.label.pack(side='left', ipadx=20, ipady=20)
        self.label1.pack(side='right', ipadx=20, ipady=20)

        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()

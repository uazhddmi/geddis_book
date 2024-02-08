import tkinter


class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.label = tkinter.Label(self.main_window, text='Programming is cool')
        self.label.pack(side='bottom')

        self.button_frame = tkinter.Frame(self.main_window)
        self.button_frame.pack()

        self.button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.button.pack()


        self.canvas = tkinter.Canvas(self.main_window, width=200, height=200)

        self.canvas.create_line(0, 0, 199, 199, fill='green', smooth=True)
        self.canvas.create_line(199, 0, 0, 199, dash=(5, 2))

        self.canvas.create_line(10, 10, 189, 10, 100, 189, 10, 10, arrow=tkinter.FIRST)

        self.canvas.create_rectangle(20, 20, 180, 180, outline='green', dash=(5, 3))

        self.canvas.create_oval(50, 50, 150, 150)
        self.canvas.create_arc(20, 20, 180, 180, start=0, extent=90)
        self.canvas.pack()

        tkinter.StringVar

        tkinter.mainloop()


if __name__ == '__main__':
    my_gui = MyGUI()

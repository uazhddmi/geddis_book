import tkinter
import tkinter.messagebox


class FIO:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.t_frame = tkinter.Frame(self.main_window, padx=100, pady=20)
        self.b_frame = tkinter.Frame(self.main_window, padx=100, pady=10)

        self.value = tkinter.StringVar()
        self.address_label = tkinter.Label(self.t_frame, textvariable=self.value)

        self.button1 = tkinter.Button(self.b_frame, text='Show info', command=self.__show_info)
        self.button2 = tkinter.Button(self.b_frame, text='Quit', command=self.main_window.destroy)

        self.address_label.pack()

        self.button1.pack(side='left')
        self.button2.pack(side='right')

        self.t_frame.pack()
        self.b_frame.pack()

        tkinter.mainloop()

    def __show_info(self):
        self.value.set('Here is should be personal data')


if __name__ == '__main__':
    fio = FIO()

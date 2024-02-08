import tkinter


class Tranlator:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.t_frame = tkinter.Frame(self.main_window)
        self.b_frame = tkinter.Frame(self.main_window)

        # Create empty field in top frame
        self.value = tkinter.StringVar()
        self.word_label = tkinter.Label(self.t_frame, textvariable=self.value)

        # Create buttons in bottom frame
        self.sinister_button = tkinter.Button(self.b_frame, text='sinister', command=self.show_word1)
        self.dexter_button = tkinter.Button(self.b_frame, text='dexter', command=self.show_word2)
        self.medium_button = tkinter.Button(self.b_frame, text='medium', command=self.show_word3)

        self.word_label.pack()

        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')

        self.t_frame.pack()
        self.b_frame.pack()

        tkinter.mainloop()

    def show_word1(self):
        self.value.set('left')

    def show_word2(self):
        self.value.set('right')

    def show_word3(self):
        self.value.set('middle')


if __name__ == '__main__':
    translate = Tranlator()

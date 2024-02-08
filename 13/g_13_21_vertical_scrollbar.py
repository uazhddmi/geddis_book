import tkinter

class VerticalScrollbar:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        self.listbox = tkinter.Listbox(self.listbox_frame, height=6, width=0)
        self.listbox.pack(side='left')

        # Create vertical Scrollbar widget inside of listbox_frame
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

        # Setting widgets Scrollbar and Listbox for work
        self.scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        months = ['Januanry', 'February', 'March', 'April', 'May',
                  'June', 'July', 'August', 'September', 'October', 'November',
                  'Desember']

        for month in months:
            self.listbox.insert(tkinter.END, month)

        tkinter.mainloop()

if __name__ == '__main__':
    scrollbar_example = VerticalScrollbar()

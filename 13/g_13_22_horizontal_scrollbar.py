import tkinter

class HorizontalScrollbar:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox_frame = tkinter.Frame(self.main_window)
        self.listbox_frame.pack(padx=20, pady=20)

        self.listbox = tkinter.Listbox(self.listbox_frame, height=0, width=30)
        self.listbox.pack(side='top')

        # Create vertical Scrollbar widget inside of listbox_frame
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame, orient=tkinter.HORIZONTAL)
        self.scrollbar.pack(side='bottom', fill=tkinter.X)

        # Setting widgets Scrollbar and Listbox for work
        self.scrollbar.config(command=self.listbox.xview)
        self.listbox.config(xscrollcommand=self.scrollbar.set)

        data = [
                ' Dummy long text blalbladldsf sfa1',
                ' Dummy long text blalbladldsf sfa2',
                ' Dummy long text blalbladldsf sfa3',
                ' Dummy long text blalbladldsf sfa4',
                ' Dummy long text blalbladldsf sfa5',
                ' Dummy long text blalbladldsf sfa6 sdfsdfsfs d',
        ]

        for element in data:
            self.listbox.insert(tkinter.END, element)

        tkinter.mainloop()

if __name__ == '__main__':
    scrollbar_example = HorizontalScrollbar()

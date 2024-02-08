import tkinter


class Scrollbar:
    def __init__(self):
        self.main_window = tkinter.Tk()

        # Create external frame will contain inner frame & horizontal scroll
        self.outer_frame = tkinter.Frame(self.main_window)
        self.outer_frame.pack(padx=20, pady=20)

        # Create inner frame with Listbox and vertical scroll
        self.inner_frame = tkinter.Frame(self.outer_frame)
        self.inner_frame.pack()

        # Create widget Listbox
        self.listbox = tkinter.Listbox(self.inner_frame, height=5, width=30)
        self.listbox.pack(side='left')

        # Create vertical widget scrollbar inside inner_frame
        self.v_scrollbar = tkinter.Scrollbar(self.inner_frame, orient=tkinter.VERTICAL)
        self.v_scrollbar.pack(side='right', fill=tkinter.Y)

        # Create horizontal widget scrollbar inside outer_frame
        self.h_scrollbar = tkinter.Scrollbar(self.outer_frame, orient=tkinter.HORIZONTAL)
        self.h_scrollbar.pack(side='bottom', fill=tkinter.X)

        # Configure widgets Scrollbar & Listbox for group work
        self.v_scrollbar.config(command=self.listbox.yview)
        self.h_scrollbar.config(command=self.listbox.xview)
        self.listbox.config(yscrollcommand=self.v_scrollbar.set,
                            xscrollcommand=self.h_scrollbar.set)

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
    scrollbar_example = Scrollbar()


import tkinter


class ListboxExample:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.listbox = tkinter.Listbox(self.main_window)
        self.listbox.pack(padx=10, pady=10)

        # Fill in data
        self.listbox.insert(0, 'Monday')
        self.listbox.insert(1, 'Tuesday')
        self.listbox.insert(2, 'Wednesday')
        self.listbox.insert(3, 'Thuesday')
        self.listbox.insert(4, 'Friday')
        self.listbox.insert(5, 'Saturday')
        self.listbox.insert(6, 'Sunday')

        tkinter.mainloop()


if __name__ == '__main__':
    listbox_example = ListboxExample()
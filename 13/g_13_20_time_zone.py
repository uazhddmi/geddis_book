import tkinter


class TimeZone:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Time zones')

        self.__build_prompt_label()
        self.__build_listbox()
        self.__build_output_frame()
        self.__build_quit_button()

        tkinter.mainloop()

    # Create widget prompt_label with signature
    def __build_prompt_label(self):
        self.prompt_label = tkinter.Label(
            self.main_window, text='Choose city'
        )
        self.prompt_label.pack(padx=5, pady=5)

    def __build_listbox(self):
        self.__cities = ['Denver', 'Gonolulu', 'Mineapolis', 'New York', 'SanFrancisco']
        self.city_listbox = tkinter.Listbox(self.main_window, height=0, width=0)
        self.city_listbox.pack(padx=5, pady=5)

        # Link callback function to Listbox
        self.city_listbox.bind('<<ListboxSelect>>', self.__display_time_zone)

        for city in self.__cities:
            self.city_listbox.insert(tkinter.END, city)

    # Method create output_frame and fill it in
    def __build_output_frame(self):
        self.output_frame = tkinter.Frame(self.main_window)
        self.output_frame.pack(padx=5)

        self.output_description_label = tkinter.Label(
            self.output_frame, text='Time zone:')
        self.output_description_label.pack(side='left', padx=(5,1), pady=5)

        self.__timezone = tkinter.StringVar()

        self.output_label = tkinter.Label(
            self.output_frame, borderwidth=1, relief='solid',
            width=15, textvariable=self.__timezone)
        self.output_label.pack(side='right', padx=(1, 5), pady=5)

    def __build_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window, text='Quit', command=self.main_window.destroy
        )
        self.quit_button.pack(padx=5, pady=5)

    def __display_time_zone(self, event):
        index = self.city_listbox.curselection()
        city = self.city_listbox.get(index[0])

        if city == 'Denver':
            self.__timezone.set('Mountain')
        elif city == 'Gonolulu':
            self.__timezone.set('Haway-aleut')
        elif city == 'Mineapolis':
            self.__timezone.set('Central')
        elif city == 'New York':
            self.__timezone.set('East')
        elif city == 'SanFrancisco':
            self.__timezone.set('Pasific')


if __name__ == '__main__':
    time_zone = TimeZone()
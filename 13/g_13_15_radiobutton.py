import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create 2 frames, 1 for Radiobutton widgets, 1 for the rest
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Create IntVar object for usage with Radiobutton widgets
        self.radio_var = tkinter.IntVar()

        self.radio_var.set(1)

        # Create Radiobutton widgets in top_frame
        self.rb1 = tkinter.Radiobutton(self.top_frame,
                                       text='Version 1',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,
                                       text='Version 2',
                                       variable=self.radio_var,
                                       value=2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,
                                       text='Version 3',
                                       variable=self.radio_var,
                                       value=3)

        # Pack radiobutton widgets
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        # Create button Ok and Quit
        self.ok_button = tkinter.Button(self.bottom_frame,
                                        text='Ok',
                                        command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        # Pack button widgets
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Packing frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Launch main cycle
        tkinter.mainloop()

    # method show_choide callback function for button Ok
    def show_choice(self):
        tkinter.messagebox.showinfo('Choice',
                                    f'You\'ve choosen {str(self.radio_var.get())} version')


if __name__ == '__main__':
    my_gui = MyGUI()

import tkinter


class TestAvg:
    def __init__(self):
        # Create main window
        self.main_window = tkinter.Tk()

        # Create 5 frames
        self.test1_frame = tkinter.Frame(self.main_window)
        self.test2_frame = tkinter.Frame(self.main_window)
        self.test3_frame = tkinter.Frame(self.main_window)
        self.avg_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create & pack widget for score 1
        self.test1_label = tkinter.Label(self.test1_frame, text='Enter mark 1: ')
        self.test1_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test1_label.pack(side='left')
        self.test1_entry.pack(side='left')

        # Create & pack widget for score 2
        self.test2_label = tkinter.Label(self.test1_frame, text='Enter mark 2: ')
        self.test2_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test2_label.pack(side='left')
        self.test2_entry.pack(side='left')

        # Create & pack widget for score 3
        self.test3_label = tkinter.Label(self.test1_frame, text='Enter mark 3: ')
        self.test3_entry = tkinter.Entry(self.test1_frame, width=10)
        self.test3_label.pack(side='left')
        self.test3_entry.pack(side='left')

        # Create & pack widgets for average
        self.result_label = tkinter.Label(self.avg_frame, text='Average score: ')
        self.avg = tkinter.StringVar()  # For update of avg_label
        self.avg_label = tkinter.Label(self.avg_frame, textvariable=self.avg)
        self.result_label.pack(side='left')
        self.avg_label.pack(side='left')

        # Create and pack Button widgets
        self.calc_button = tkinter.Button(self.button_frame, text='Calculate average', command=self.calc_avg)
        self.quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack frames
        self.test1_frame.pack()
        self.test2_frame.pack()
        self.test3_frame.pack()
        self.avg_frame.pack()
        self.button_frame.pack()

        # Launch main cycle
        tkinter.mainloop()

    # Method calc_avg is call-back function for calc_button widget
    def calc_avg(self):
        # Get 3 marks and put them to variables
        self.test1 = float(self.test1_entry.get())
        self.test2 = float(self.test2_entry.get())
        self.test3 = float(self.test3_entry.get())

        # Calculate average
        self.average = (self.test1 + self.test2 + self.test3) / 3.0

        # Update avg_label widget, save value of self.average to object StringVar -> avg
        self.avg.set(self.average)


# Create of class TestAvg
if __name__ == '__main__':
    test_avg = TestAvg()

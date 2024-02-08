import tkinter as tk


class Fuel:
    def __init__(self):
        self.main_window = tk.Tk()

        # Create frames for label_gas, label_milage, lagel_MGP, enty_gas, entry_milage, buttons
        self.gas_frame = tk.Frame(self.main_window)
        self.milage_frame = tk.Frame(self.main_window)
        self.MGP_frame = tk.Frame(self.main_window)
        self.button_frame = tk.Frame(self.main_window)

        # Create Label field for gas, milage, MGP + empty field for result
        self.gas_label = tk.Label(self.gas_frame, text='Gas you\'ve waisted')
        self.milage_label = tk.Label(self.milage_frame, text='Mileage you can go')

        self.MGP_label = tk.Label(self.MGP_frame, text='Calculated MGP')

        # Create buttons
        self.calculate_button = tk.Button(self.button_frame, text='Calcualate MGP')
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.gas_label.pack(side='left')
        self.milage_label.pack(side='left')
        self.MGP_label.pack(side='left')

        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.gas_frame.pack()
        self.milage_frame.pack()
        self.MGP_frame.pack()
        self.button_frame.pack()

        tk.mainloop()


if __name__ == '__main__':
    fuel = Fuel()
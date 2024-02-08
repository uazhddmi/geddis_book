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
        self.gas_entry = tk.Entry(self.gas_frame, width=10)
        self.milage_label = tk.Label(self.milage_frame, text='Mileage you can go')
        self.milage_entry = tk.Entry(self.milage_frame, width=10)

        self.value = tk.StringVar()
        self.MGP_label = tk.Label(self.MGP_frame, text='Calculated MGP')
        self.MGP_result = tk.Label(self.MGP_frame, textvariable=self.value)

        # Create buttons calculation and quit
        self.calculate_button = tk.Button(self.button_frame, text='Calcualate MGP', command=self.__calc_MGP)
        self.quit_button = tk.Button(self.button_frame, text='Quit', command=self.main_window.destroy)

        self.gas_label.pack(side='left')
        self.gas_entry.pack(side='left')
        self.milage_label.pack(side='left')
        self.milage_entry.pack(side='left')
        self.MGP_label.pack(side='left')

        self.calculate_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.gas_frame.pack()
        self.milage_frame.pack()
        self.MGP_frame.pack()
        self.MGP_result.pack()
        self.button_frame.pack()

        tk.mainloop()

    def __calc_MGP(self):
        self.gas_val = float(self.gas_entry.get())
        self.milage_val = float(self.milage_entry.get())

        self.value.set(f'{self.milage_val / self.gas_val:.02f}')


if __name__ == '__main__':
    fuel = Fuel()

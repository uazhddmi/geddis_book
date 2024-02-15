import tkinter
import tkinter.messagebox
import sqlite3


class EmployeeDetails:
    def __init__(self):
        #  Create main window
        self.main_window = tkinter.Tk()

        #  Compose main window filling
        self.__build_main_window()

        #  Launch main cycle
        tkinter.mainloop()

    #  Compose main window
    def __build_main_window(self):
        self.__create_prompt_label()
        self.__build_listbox_frame()
        self.__create_quit_button()

    #  Create main note with help for user
    def __create_prompt_label(self):
        self.employee_prompt_label = tkinter.Label(
            self.main_window, text='Choose employee'
        )
        self.employee_prompt_label.pack(side='top', padx=5, pady=5)

    #  Compose frame with Listbox & Scrollbar widgets
    def __build_listbox_frame(self):
        #  Create frame for Listbox & Scrollbar widges
        self.listbox_frame = tkinter.Frame(self.main_window)
        self.__setup_listbox()
        self.__create_scrollbar()
        self.__populate_listbox()  # fill-in Listbox widget with employees' names
        self.listbox_frame.pack()

    #  Create widget Listbox  for output employees names on the screen
    def __setup_listbox(self):
        self.employee_listbox = tkinter.Listbox(
            self.listbox_frame, selectmode=tkinter.SINGLE, height=6
        )
        #  link Listbox widget to callback function
        self.employee_listbox.bind('<<ListboxSelect>>', self.__get_details)

        self.employee_listbox.pack(side='left', padx=5, pady=5)

    #  Create vertical widget Scrollbar for usage with Listbox
    def __create_scrollbar(self):
        self.scrollbar = tkinter.Scrollbar(self.listbox_frame,
                                           orient=tkinter.VERTICAL)
        self.scrollbar.config(command=self.employee_listbox.yview)
        self.employee_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill=tkinter.Y)

    #  Output of employees' names in Listbox windget
    def __populate_listbox(self):
        for employee in self.__get_employees():
            self.employee_listbox.insert(tkinter.END, employee)

    #  Create quit button
    def __create_quit_button(self):
        self.quit_button = tkinter.Button(
            self.main_window,
            text='Quit',
            command=self.main_window.destroy)
        self.quit_button.pack(side='top', padx=10, pady=5)

    #  Get list of employees from db
    def __get_employees(self):
        employee_list = []
        conn = None
        try:
            conn = sqlite3.connect('employee.db')
            cur = conn.cursor()

            cur.execute('SELECT Name FROM Employees')

            employee_list = [n[0] for n in cur.fetchall()]
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Db mistake', err)
        finally:
            if conn is not None:
                conn.close()

            return employee_list

    #  Receive detailed information about employee
    def __get_details(self, event):
        listbox_index = self.employee_listbox.curselection()[0]
        selected_emp = self.employee_listbox.get(listbox_index)

        #  Query db info for chosen employee
        conn = None
        try:
            conn = sqlite3.connect('employee.db')
            cur = conn.cursor()

            cur.execute('''
                    SELECT
                    Employees.Name,
                    Employees.Position,
                    Departments.DepartmentName,
                    Locations.City
                    FROM 
                    Employees, Departments, Locations
                    WHERE
                    Employees.Name == ? AND
                    Employees.DepartmentID == Departments.DepartmentID AND
                    Employees.LocationID == Locations.LocationID''',
                        (selected_emp,))

            results = cur.fetchone()

            self.__display_details(name=results[0], position=results[1],
                                   department=results[2], location=results[3])
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Db Error', err)
        finally:
            if conn is not None:
                conn.close()

    #  Output employee's information at widget
    def __display_details(self, name, position, department, location):
        tkinter.messagebox.showinfo('Employee information',
                                    'Name: ' + name +
                                    '\nPosition: ' + position +
                                    '\nDepartment ' + department +
                                    '\nLocation: ' + location)


if __name__ == '__main__':
    employee_details = EmployeeDetails()

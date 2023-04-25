# OrganizationConsoleView.py
# By Mohamed Sed
# Presentation layer, that handles everything the user sees and interacts with. It sends and retrieves
# data from business layer.

# import tkinter so we can build a GUI
from tkinter import ttk
import tkinter as tk
# import OrganizationService class from OrganizationService file in Business package
from Business.OrganizationService import OrganizationService
# import OrganizationRecordModel class from OrganizationRecord file in Model package
from Model.OrganizationRecord import OrganizationRecordModel


# View class that control user interactions.
class OrganizationRecordView:
    # constructor instantiates an instance of our business layer and model layer
    def __init__(self):
        self.textbox = None
        self.new_window = None
        self.window = tk.Tk()
        self.service = OrganizationService()
        self.model = OrganizationRecordModel

    # method to build GUI using tkinter library
    # select option from drop down menu, and passed that option to
    # select_option method once button is clicked
    def appGUI(self):
        self.window.title("Company Records")
        self.window.geometry("300x200")

        header = tk.Label(self.window, text="Company Record Database\n(Select option)")
        header.pack()
        menu = tk.StringVar()
        menu.set("Select any option")
        combo = tk.ttk.Combobox(self.window, state="readonly",
                                values=["View record", "Insert record",
                                        "Update record", "Delete record",
                                        "View all records", "Display chart",
                                        "Reload records(csv)", "Quit"])
        combo.pack(pady=10)
        button = tk.Button(self.window, text="Submit", command=lambda: self.select_option(combo))
        button.pack(pady=10)

        self.window.mainloop()

    # method to perform option selected from drop down
    def select_option(self, combo):
        selected = combo.get()
        if selected == "Reload records(csv)":
            self.reloadDataSet()
        elif selected == "view record":
            self.viewRecord()
        elif selected == "View all records":
            self.viewAllRecords()
        elif selected == "Insert record":
            self.insertRecord()
        elif selected == "Update record":
            self.updateRecord()
        elif selected == "Delete record":
            self.deleteRecord()
        elif selected == "Display chart":
            self.chartData()
        elif selected == "Quit":
            exit()
        else:
            textbox = tk.Text(self.window, height=50, width=50)
            textbox.pack(pady=10)
            # Clear the textbox
            textbox.delete("1.0", tk.END)

            # Insert the result into the textbox
            textbox.insert(tk.END, "Invalid menu option, try again.")
        combo.set("")

    # method to display all records from our dataset, reloads the database on every call
    def reloadDataSet(self):
        reload_window = tk.Toplevel(self.window)
        reload_window.title("Original Records")
        reload_window.geometry("1400x800")

        header = tk.Label(reload_window, text="Original list of Organizations")
        header.pack()
        self.textbox = tk.Text(reload_window, height=105, width=250)
        self.textbox.pack(pady=10)
        # Clear the textbox
        self.textbox.delete("1.0", tk.END)
        organization = self.service.getAllDataSetRecords()

        header = ["ID", "Name", "Country", "Founded", "Industry", "Number of Employees"]

        max_lengths = [0, 0, 0, 8, 0, 0]
        for line in organization:
            for i in range(len(line)):
                max_lengths[i] = max(max_lengths[i], len(str(line[i])))

        header_str = "  "
        for i, column_name in enumerate(header):
            header_str += column_name.ljust(max_lengths[i] + 4)

        text = header_str + "\n"
        for line in organization:
            line_str = "  "
            for i, item in enumerate(line):
                line_str += str(item).ljust(max_lengths[i] + 4)
            text += line_str + "\n"

        self.textbox.insert("1.0", text)
        # Wait for user action
        reload_window.wait_window()

        # Close the insert window
        reload_window.destroy()

    # method which takes in an int input and display record at user input
    def viewRecord(self):
        self.new_window = tk.Toplevel(self.window)
        self.new_window.title("View Organization")
        self.new_window.geometry("250x250")

        label = tk.Label(self.new_window, text="Select line number to view an organization: ")
        label.pack()

        result_entry = tk.Entry(self.new_window)
        result_entry.pack()

        view = input(result_entry)
        # access last element of string and assign it to variable last_num
        last_num = view[-1]
        if last_num == 1 and view != 11:
            suffix = "st"
        elif last_num == 2 and view != 12:
            suffix = "nd"
        elif last_num == 3 and view != 13:
            suffix = "rd"
        else:
            suffix = "th"
        print("Viewing " + view + suffix + " employee: ")

        submit_button = tk.Button(self.new_window, text="Submit",
                                  command=lambda: self.service.getRecord(view))
        submit_button.pack()

    # method to display all records from database
    def viewAllRecords(self):
        viewAll_window = tk.Toplevel(self.window)
        viewAll_window.title("Updated Records")
        viewAll_window.geometry("1200x800")

        header = tk.Label(viewAll_window, text="Updated list of Organizations")
        header.pack()

        self.textbox = tk.Text(viewAll_window, height=105, width=250)
        self.textbox.pack(pady=10)
        # Clear the textbox
        self.textbox.delete("1.0", tk.END)

        # Insert the result into the textbox
        organization = self.service.getAllRecords()
        max_lengths = [0, 0, 0, 8, 0, 0]
        for line in organization:
            for i in range(len(line)):
                max_lengths[i] = max(max_lengths[i], len(str(line[i])))
        # Insert the result into the textbox

        for line in organization:
            self.textbox.insert(tk.END,
                                str(line[0]).ljust(max_lengths[0]) + "\t" + str(line[1]).ljust(max_lengths[1]) + "\t\t"
                                + str(line[2]).ljust(max_lengths[2]) + "\t" + str(line[3]).ljust(max_lengths[3]) + "\t"
                                + str(line[4]).ljust(max_lengths[4]) + "\t\t\t" + str(line[5]).ljust(max_lengths[5])
                                + "\n")

        # Wait for user action
        viewAll_window.wait_window()

        # Close the insert window
        viewAll_window.destroy()

    # method that takes in user inputs and inserts it into the database.
    def insertRecord(self):
        insert_window = tk.Toplevel(self.window)
        insert_window.title("Insert Record")
        insert_window.geometry("500x500")

        # Add any widgets that you want to display in the insert window
        # ...

        # Wait for user action
        insert_window.wait_window()

        # Close the insert window
        insert_window.destroy()
        print("Insert record")
        founded = input("Enter year founded: ")
        while len(founded) != 4 and not isinstance(founded, int):
            print("Incorrect year length, try again! ")
            founded = input("Enter year founded: ")
        industry = input("Enter industry: ")
        numberEmployees = input("Enter number of employees: ")
        name = input("Enter name: ")
        country = input("Enter country: ")
        print("Inserted record: ")
        print(self.service.insertRecord(name, country, founded, industry,
                                        numberEmployees))

    # method that takes in a user input and updates that record in the database
    def updateRecord(self):
        index = input("Select record index to update a record: ")
        current_record = self.service.getRecord(index)
        founded = input("Update year founded (current value: {}): ".format(current_record[3]))
        while len(founded) != 4 and not isinstance(founded, int):
            print("Incorrect year format, try again! ")
            founded = input("Update year founded (current value: {}): ".format(current_record[3]))
        industry = input("Update industry (current value: {}): ".format(current_record[4]))
        numberEmployees = input("Enter number of employees (current value: {}): ".format(current_record[5]))
        name = input("Enter name (current value: {}): ".format(current_record[1]))
        country = input("Enter country (current value: {}): ".format(current_record[2]))
        print("Previous record: ")
        print(current_record)
        updated_record = self.service.updateRecord(index, name, country, founded, industry, numberEmployees)
        print("Updated record: ")
        print(updated_record)

    # method that takes in a user input and deletes that record in the database.
    def deleteRecord(self):
        index = input("Select record index to delete record: ")
        print("Deleted record: ")
        print(self.service.getRecord(index))
        self.service.deleteRecord(index)

    # method that takes in 2 columns to select for our vertical bar chart and sends those columns to the service layer.
    def chartData(self):
        print("Select two columns to create vertical bar chart")
        print("(name, country, founded, industry, number_employees)")
        x_column = input("Column x: ")
        y_column = input("Column y: ")
        self.service.createBarChart(x_column, y_column)

    def submit_result(prev_window, result_text):
        prev_window.result_text.set(result_text)

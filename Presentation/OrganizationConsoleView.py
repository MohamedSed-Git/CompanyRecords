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

        header = tk.Label(self.window, text="Company Record Database")
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
        self.textbox.delete("1.0", tk.END)
        combo.set("")

    # method to display all records from our dataset, reloads the database on every call
    def reloadDataSet(self):
        reload_window = tk.Toplevel(self.window)
        reload_window.title("Original Records")
        reload_window.geometry("1000x700")

        header = tk.Label(reload_window, text="Original list of Organizations")
        header.pack()

        self.textbox = tk.Text(reload_window, height=105, width=250)
        self.textbox.pack(pady=10)
        # Clear the textbox
        self.textbox.delete("1.0", tk.END)

        # Insert the result into the textbox
        organization = self.service.getAllDataSetRecords()
        for line in organization:
            self.textbox.insert(tk.END, str(line) + "\n")

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
        viewAll_window.geometry("1000x700")

        header = tk.Label(viewAll_window, text="Updated list of Organizations")
        header.pack()

        self.textbox = tk.Text(viewAll_window, height=105, width=250)
        self.textbox.pack(pady=10)
        # Clear the textbox
        self.textbox.delete("1.0", tk.END)

        # Insert the result into the textbox
        organization = self.service.getAllRecords()
        for line in organization:
            self.textbox.insert(tk.END, str(line) + "\n")

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
        organizationID = input("Enter organizationID (15 character alphanumeric): ")
        while len(organizationID) > 15:
            print("ID is lengthy, try again! ")
            organizationID = input("Enter organizationID (15 character alphanumeric): ")
        founded = input("Enter year founded: ")
        while len(founded) != 4:
            print("Incorrect year length, try again! ")
            founded = input("Enter year founded: ")
        industry = input("Enter industry: ")
        numberEmployees = input("Enter number of employees: ")
        name = input("Enter name: ")
        country = input("Enter country: ")
        print("Inserted record: ")
        print(self.service.insertRecord(organizationID, name, country, founded, industry,
                                        numberEmployees))

    # method that takes in a user input and updates that record in the database
    def updateRecord(self):
        index = input("Select record index to update a record: ")
        organizationID = input("Update organizationID (15 character alphanumeric ): ")
        while len(organizationID) > 15:
            print("ID is lengthy, try again! ")
            organizationID = input("Enter organizationID (15 character alphanumeric): ")
        founded = input("Update year founded: ")
        while len(founded) != 4:
            print("Incorrect year length, try again! ")
            founded = input("Update year founded: ")
        industry = input("Update industry: ")
        numberEmployees = input("Enter number of employees: ")
        name = input("Enter name: ")
        country = input("Enter country: ")
        print("Previous record: ")
        print(self.service.getRecord(index))
        print("Updated record: ")
        print(self.service.updateRecord(index, organizationID, name, country, founded, industry, numberEmployees,
                                        numberEmployees))

    # method that takes in a user input and deletes that record in the database.
    def deleteRecord(self):
        index = input("Select record index to delete record: ")
        print("Deleted record: ")
        print(self.service.getRecord(index))
        self.service.deleteRecord(index)

    # method that takes in 2 columns to select for our vertical bar chart and sends those columns to the service layer.
    def chartData(self):
        print("Select two columns to create vertical bar chart")
        print("(organizationID, name, country, founded, industry, number_employees)")
        x_column = input("Column x: ")
        y_column = input("Column y: ")
        self.service.createBarChart(x_column, y_column)

    def submit_result(prev_window, result_text):
        prev_window.result_text.set(result_text)

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
        self.service = OrganizationService()
        self.model = OrganizationRecordModel

    # method to build GUI using tkinter library
    def appGUI(self):
        window = tk.Tk()
        window.title("Company Records")
        window.geometry("300x250")
        menu = tk.StringVar()
        menu.set("Select any option")
        combo = ttk.Combobox(state="readonly", values=["View record", "Insert record",
                                                       "Update record", "Delete record",
                                                       "View all records", "Display chart",
                                                       "Reload records from csv"])
        combo.place(x=75, y=75)
        window.mainloop()

    # method that displays and loops through an interactive menu.
    def options(self):
        loop = True
        while loop:
            self.menu()
            option = input()
            option = int(option)
            if option == 1:
                self.reloadDataSet()
            elif option == 2:
                self.viewRecord()
            elif option == 3:
                self.viewAllRecords()
            elif option == 4:
                self.insertRecord()
            elif option == 5:
                self.updateRecord()
            elif option == 6:
                self.deleteRecord()
            elif option == 7:
                self.chartData()
            elif option == 0:
                print("Exiting program.")
                loop = False
            else:
                print("Invalid menu option, try again.")

    # method to display all records from our dataset, reloads the database on every call
    def reloadDataSet(self):
        print("Organization Dataset")
        organization = self.service.getAllDataSetRecords()
        for line in organization:
            print(line)  # print each line in dataset

    # method which takes in an int input and display record at user input
    def viewRecord(self):
        view = input("Select line number to view a record: ")
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
        print(self.service.getRecord(view))

    # method to display all records from database
    def viewAllRecords(self):
        print("List of organization")
        organization = self.service.getAllRecords()
        for line in organization:
            print(line)

    # method that takes in user inputs and inserts it into the database.
    def insertRecord(self):
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

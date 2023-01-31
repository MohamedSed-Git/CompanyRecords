# DataStore.py
# By Mohamed Sed
# Student 040922070
# CST8333_350 Practical Project Part 4
# Persistence Layer that uses csv library to open and record from the csv dataset.
# Layer also connects to our Database and performs our CRUD all our operations.

# import the csv module so we can implement its classes
import csv
import tkinter.ttk

# import mysql connector so we can connect to mysql database
import mysql.connector
from mysql.connector import Error
# import matplotlib pyplot so we can plot bar charts
import matplotlib.pyplot as plt
# import OrganizationRecord class from Model package
from Model.OrganizationRecord import OrganizationRecordModel


# DataStore class which holds all our methods to manipulate the data
class DataStore:
    def __init__(self):
        self.model = OrganizationRecordModel
        self.db = self.createConnection()  # global variable so we can use our connection instance throughout the class
        self.createDatabase()  # create database when datastore is called
        self.createTable()  # create table when database is called

    # method that opens a readable csv file, reads the first line and assigns it to reader variable.
    def openFile(self, fileName):
        # try block to open our file and our program
        try:
            # Open the file as read only, set the general encoding and assigned the open file to the file variable
            fileName = open(fileName, 'r', encoding='utf-8')
        # except block which will handle any file not found error
        except FileNotFoundError:
            print('File not found: ' + "'" + fileName + "'" + '.')
        return fileName

    # method that will call to openFile() to open the file and use a csv module to read and record the dataset
    # to a list, and return that list.
    def loadFromFile(self):
        myList = []  # Create empty list
        try:
            # String variable which we assigned our csv file name, "r"" is used to indicate raw string
            path = r"C:\Users\moham\PycharmProjects\PracticalProjectPart04"
            fileName = path + r"\organizations.csv"
            file = self.openFile(fileName)
            # Reader function of the csv module takes in our open file and returns a
            # reader object which is assigned to the reader variable
            reader = csv.reader(file)

            # The next functions gives us the first line of our file which we'll assign
            # to the header variable to display as a header for our program
            header = next(file)

            # for loop will start from the second row and loop through our reader object
            for line in reader:

                # Instantiate OrganizationRecord object and assign to the record variable
                OrganizationRecordModel(line[0], line[1], line[2], line[3], line[4], line[5])

                # Append each line to myList and print each line
                myList.append(line)

                # break once length of list exceeds 100 records
                if len(myList) >= 100:
                    break
        # except block which will handle any input-output error
        except IOError:
            print('Problem opening file: ' + "'" + file + "'" + '.')
            file.close()
        return myList

    # method that gets all the records from the company table in worldwide database
    def getAllRecords(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM worldwide.company")
        rows = cursor.fetchall()
        self.db.commit()
        return rows

    # method that takes in a recordID and returns the corresponding record from our database table.
    def getRecord(self, recordID):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM worldwide.company WHERE id = " + recordID)
        row = cursor.fetchone()
        self.db.commit()
        return row

    # method that takes in record parameters and insert that record at the end of our database table
    def insertRecord(self, organizationID, name, country, founded, industry, numberEmployees):
        cursor = self.db.cursor()
        sql = "INSERT INTO worldwide.company" \
              "(organizationID, name, country, founded, industry, number_employees ) " \
              "VALUES (%s, %s, %s, %s, %s, %s) "
        record = (organizationID, name, country, founded, industry, numberEmployees)
        cursor.execute(sql, record)
        self.db.commit()
        return self.getRecord("(SELECT MAX(id) FROM worldwide.company)")

    # method that takes in record parameters and updates the corresponding record from our database table
    def updateRecord(self, recordID, organizationID, name, country, founded, industry, numberEmployees):
        cursor = self.db.cursor()
        sql = "UPDATE worldwide.company SET organizationID=%s, name=%s, country=%s, " \
              "founded=%s, industry=%s, number_employees=%s WHERE id=%s"
        record = (organizationID, name, country, founded, industry, numberEmployees, recordID)
        cursor.execute(sql, record)
        self.db.commit()
        return self.getRecord(recordID)

    # method that takes in recordID parameter and deletes the corresponding record from our database table
    def deleteRecord(self, recordID):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM worldwide.company WHERE id=" + recordID)
        self.db.commit()
        return self.getRecord(recordID)

    # method that will create and return a connection to the database or error if failure to connect
    def createConnection(self):
        try:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='sed00002'
            )
        except Error:
            print("Failed to connect. ")
        mydb.commit()
        return mydb

    # method that takes in a connection and a string database name, uses the connection to create a cursor and executes
    # a query to create a database with our name
    def createDatabase(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("CREATE DATABASE worldwide")
        except Error:
            print("Cannot create database, it already exist. ")
        self.db.commit()

    # method to create a table with defined columns and populate that table with dataset list from csv file
    def createTable(self):
        cursor = self.db.cursor()
        mylist = self.loadFromFile()
        try:
            cursor.execute("USE worldwide")
            cursor.execute("CREATE TABLE company(id INT AUTO_INCREMENT PRIMARY KEY, organizationID VARCHAR(25), "
                           "name VARCHAR(50), country VARCHAR(50), founded INT(4), "
                           "industry VARCHAR(50), number_employees INT(6))")
            cursor.executemany(
                "INSERT INTO company (organizationID, name, country, founded, industry, number_employees) "
                "VALUES (%s, %s, %s, %s, %s, %s) ", mylist)
        except Error:
            print("Cannot create table, it already exist. ")
        self.db.commit()

    # method to delete our database
    def deleteDB(self):
        cursor = self.db.cursor()
        try:
            cursor.execute("DROP DATABASE worldwide")
        except Error:
            print("Cannot delete database, it doesn't exist.")
        self.db.commit()

    # method to create vertical bar chart, takes in two columns from the user, fetches the data from those columns
    # creates and assigns those columns to x and y-axis.
    def verticalBarChart(self, column1, column2):
        x_column = []
        y_column = []
        cursor = self.db.cursor()
        if column2 == "number_employees":
            cursor.execute("SELECT " + column1 + ", sum(" + column2 + ") FROM worldwide.company group by " + column1)
            columns = cursor.fetchall()
            for line in columns:
                x_column.append(line[0])
                y_column.append(line[1])
            self.db.commit()
            plt.bar(x_column, y_column)
            plt.xlabel(column1)
            plt.ylabel(column2 + " (sum)")
            plt.title("Vertical Bar Chart")
            plt.show()
        else:
            cursor.execute("SELECT " + column1 + ", count(" + column2 + ") FROM worldwide.company group by "
                           + column1)
            columns = cursor.fetchall()
            for line in columns:
                x_column.append(line[0])
                y_column.append(line[1])
            self.db.commit()
            plt.bar(x_column, y_column)
            plt.xlabel(column1)
            plt.ylabel(column2 + " (count)")
            plt.title("Vertical Bar Chart")
            plt.show()

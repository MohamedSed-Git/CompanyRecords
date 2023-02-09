# OrganizationService.py
# By Mohamed Sed
# Business Layer, responsible to process data between persistence and view layers.

# import DataStore class from DataStore python file in Persistence package
from Persistence.DataStore import DataStore
# import OrganizationRecordModel class from OrganizationRecord file in Model package
from Model.OrganizationRecord import OrganizationRecordModel


# Class which requests the Persistence layer to perform insert, update, delete and saving of records.
class OrganizationService:
    def __init__(self):
        self.dataStore = DataStore()
        self.model = OrganizationRecordModel('', '', '', int(), '', int())

    # methods reloads recreates the database and populates the table with the dataset records.
    def getAllDataSetRecords(self):
        self.dataStore.deleteDB()
        self.dataStore.createDatabase()
        self.dataStore.createTable()
        return self.dataStore.getAllRecords()

    # Get all database records
    def getAllRecords(self):
        return self.dataStore.getAllRecords()

    # Take in record id and returns that record from the database
    def getRecord(self, recordID):
        return self.dataStore.getRecord(recordID)

    # Take in record id, new record and insert new record in database at id
    def insertRecord(self, organizationID, name, country, founded, industry, numberEmployees):
        return self.dataStore.insertRecord(organizationID, name, country, founded, industry, numberEmployees)

    # Update record in database at provided id
    def updateRecord(self, recordID, organizationID, name, country, founded, industry, numberEmployees):
        return self.dataStore.updateRecord(recordID, organizationID, name, country, founded, industry,
                                           numberEmployees)

    # Delete record in database at provided id
    def deleteRecord(self, recordID):
        self.dataStore.deleteRecord(recordID)

    # Create bar chart, sends columns selected in view to datastore
    def createBarChart(self, x_column, y_column):
        return self.dataStore.verticalBarChart(x_column, y_column)

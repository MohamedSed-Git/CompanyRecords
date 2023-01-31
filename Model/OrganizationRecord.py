# OrganizationRecord.py
# By Mohamed Sed
# Student 040922070
# CST8333_350 Practical Project Part 4
# Model layer which holds our Organization record object


# OrganizationRecord class to hold our object variables and accessors/mutators
class OrganizationRecordModel:

    # the initializing constructor
    def __init__(self, organizationID, name, country, founded, industry, numberEmployees):
        # Private variables which are initialized
        self.__organizationID = organizationID
        self.__name = name
        self.__country = country
        self.__founded = int(founded)
        self.__industry = industry
        self.__numberEmployees = int(numberEmployees)

    # Mutator for organization variable
    def set_organizationID(self, organizationID):
        self.__organizationID = organizationID

    # Accessor for organization variable
    def get_organizationID(self):
        return self.__organizationID

    # Mutator for name variable
    def set_name(self, name):
        self.__name = name

    # Accessor for name variable
    def get_name(self):
        return self.__name

    # Mutator for country variable
    def set_country(self, country):
        self.__country = country

    # Accessor for country variable
    def get_country(self):
        return self.__country

    # Mutator for founded variable
    def set_founded(self, founded):
        self.__founded = int(founded)

    # Accessor for founded variable
    def get_founded(self):
        return self.__founded

    # Mutator for industry variable
    def set_industry(self, industry):
        self.__industry = (industry)

    # Accessor for industry variable
    def get_industry(self):
        return self.__industry

    # Mutator for numberEmployees variable
    def set_numberEmployees(self, numberEmployees):
        self.__numberEmployees = int(numberEmployees)

    # Accessor for numberEmployees
    def get_numberEmployees(self):
        return self.__numberEmployees

    # String representation of Organization record
    def __str__(self):
        return str(self.__organizationID) + "', '" + str(self.__name) + "', '" \
               + str(self.__country) + "', '" + str(self.__founded) + "', '" + str(self.__industry) + "', '" \
               + str(self.__numberEmployees)

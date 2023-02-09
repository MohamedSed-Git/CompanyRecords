# OrganizationProgramStartUp.py
# By Mohamed Sed

# import View class from View file in Presentation package
from Presentation.OrganizationConsoleView import OrganizationRecordView


# class used to start our program
class OrganizationProgramStartUp:
    # instantiate an instance of OrganizationRecordView class and call options to display menu options.
    start = OrganizationRecordView()
    start.appGUI()

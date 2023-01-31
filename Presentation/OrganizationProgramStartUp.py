# OrganizationProgramStartUp.py
# By Mohamed Sed
# Student 040922070
# CST8333_350 Practical Project Part 4

# import View class from View file in Presentation package
from Presentation.OrganizationConsoleView import OrganizationRecordView


# class used to start our program
class OrganizationProgramStartUp:
    # instantiate an instance of OrganizationRecordView class and call options to display menu options.
    start = OrganizationRecordView()
    start.appGUI()

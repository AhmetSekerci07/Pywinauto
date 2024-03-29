# Importing necessary libraries from pywinauto
from pywinauto import Application

# Define the name of the executable of the application you want to automate.
# Replace 'Your_App_Name.exe' with the actual executable name of your application.
yourExeName = "Your_App_Name.exe"

# Connect to an already running application using its executable name.
# This command searches for the process by the module (executable name) and connects to it.
# Note: The application must be running; otherwise, this will raise an error.
app = Application(backend='uia').connect(path=yourExeName)

# Once connected to the application, you can interact with its windows (dialogs).
# Here, we focus on the main dialog of the application.
# The 'print_control_identifiers()' method prints the hierarchy of control identifiers for the main dialog window,
# which is useful for identifying the controls (buttons, text fields, etc.) you can automate.
app.Dialog.print_control_identifiers()

# Note: If your application has multiple dialogs or the main window is not recognized as 'Dialog',
# you might need to adjust 'app.Dialog' to correctly reference the window you wish to interact with.
# Use tools like 'Inspect.exe' (part of the Windows SDK) to explore the UI elements and their identifiers.

'''
# Simple Code 

from pywinauto import application
import pywinauto.application

yourExeName = "Canfield Capture"
pid = application.process_from_module(module=yourExeName)
app = pywinauto.Application(backend='uia').connect(process=pid)
app.Dialog.print_control_identifiers()

'''

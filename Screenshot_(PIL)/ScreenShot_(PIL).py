# I get error many times while setuping PIL library try with PIL only first not with 'Image Grab'
# pip install Pillow
from datetime import datetime

from PIL import ImageGrab


import os

screenshots_directory = "screenshots"
if not os.path.exists(screenshots_directory):
    os.makedirs(screenshots_directory)

class Screenshot:
    """
    This class provides a simple way to capture and save screenshots.
    It allows specifying a custom directory for saving screenshots;
    if none is provided, it defaults to a 'screenshots' folder in the script's directory.

    Methods:
    - __init__(directory=None): Initializes the screenshot utility, optionally with a custom directory.
    - take_screenshot(filename): Captures and saves a screenshot with the given filename.
    """

    def __init__(self, directory=None):
        # Set the directory where screenshots will be saved.
        # Defaults to a 'screenshots' subdirectory in the script's current directory.
        if directory is None:
            self.screenshots_directory = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                      "screenshots")
        else:
            self.screenshots_directory = directory

        # Create the directory if it does not already exist.
        if not os.path.exists(self.screenshots_directory):
            os.makedirs(self.screenshots_directory)

    def take_screenshot(self, filename):
        # Construct the full path where the screenshot will be saved.
        screenshot_path = os.path.join(self.screenshots_directory, filename)
        # Capture the current screen.
        screen = ImageGrab.grab()
        # Save the screenshot to the specified path.
        screen.save(screenshot_path)
        # Print a confirmation message.
        print(f"Screenshot saved as {screenshot_path}")

    def save_screenshot_with_timestamp(self, prefix: object) -> object:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{prefix}_{timestamp}.png"
        self.take_screenshot(filename)

#How I run in main

def test_a():
    screenshot_obj = Screenshot()

    screenshot_obj.save_screenshot_with_timestamp("(a)1004")



'''
ignore
 C:\Program Files\JetBrains\PyCharm Community Edition 2022.3\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py:8: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import iter_entry_points message 
  
  
  import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)




'''
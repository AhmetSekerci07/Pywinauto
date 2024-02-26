# I get error many times while setuping PIL library try with PIL only first not with 'Image Grab'
# pip install Pillow


from PIL import ImageGrab
import os

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

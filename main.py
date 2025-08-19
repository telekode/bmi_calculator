#import python GUI libraries
from PyQt6.QtWidgets import QApplication, QWidget
import os
#import UI module
from ui import build_window

# Import logic module
from logic import calculate_bmi,clear_inputs

def main():
    # Initialize the application (entry point for any PyQt app)
    app = QApplication([]) 

    # Build the main window and all required widgets from the UI module
    bmi_window,bmi_widgets = build_window()

    # Display the main application window
    bmi_window.show()

    # Apply external stylesheet (QSS)
    # The file path is built relative to the current script location to ensure
    # the stylesheet is found regardless of the working directory
    qss_file = os.path.join(os.path.dirname(__file__), "style.qss") 
    with open(qss_file, "r") as f:
        app.setStyleSheet(f.read())

    # Connect the button click to the BMI calculation function
    bmi_widgets["cal_bmi"].clicked.connect(lambda: calculate_bmi(bmi_widgets))  

    # Connect the button click to the BMI clear function
    bmi_widgets["clear_bmi"].clicked.connect(lambda:clear_inputs(bmi_widgets)) 

    # Start the application event loop (keeps the app running and responsive)
    app.exec()

# Run the app only if this file is executed directly (not imported as a module)
if __name__ == "__main__":  
    main()  

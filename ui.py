# UI module
from PyQt6.QtWidgets import QFormLayout,QPushButton,QWidget,QLineEdit,QHBoxLayout,QRadioButton,QLabel

def build_window():
    bmi_window = QWidget()  # Create a new QWidget instance for the main window
    bmi_window.setWindowTitle("BMI Calculator")  # Set the title of the window
    
    form_layout = QFormLayout(bmi_window)  # Create a QFormLayout and set it as the layout for the window
    #form_layout.setSizeConstraint(QFormLayout.SizeConstraint.SetFixedSize)  # Set the layout to a fixed size
    bmi_window.setFixedSize(500, 300) # Lock the main window size

    def create_input_box(placeholder_text,box_text): 
        line = QLineEdit()  # Create a QLineEdit widget
        line.setFixedSize(250,50) # # Create a QLineEdit with a fixed size
        line.setPlaceholderText(placeholder_text) # Set a placeholder text for the widget
        form_layout.addRow(box_text,line) # Add a row to the form layout with a label and the widget
        return line  # Return the widget for further use

    def create_push_button(button_text):
        button = QPushButton(button_text)  # Create a QPushButton widget
        button.setFixedSize(210,50)  # Create a QPushButton with a fixed size
        return button

    # Age Section
    age = create_input_box("Must Be a Number","Enter Your Age")  # Create an input box for age

    # Gender Selection Section
    gender = QLineEdit( ) # Create a QLineEdit for gender input
    gender_layout = QHBoxLayout() # Create a horizontal layout for choose gender
    
    radio_male = QRadioButton("Male")   # Create a radio button for choose male
    radio_female = QRadioButton ("Female")  # Create a radio button for choose female
    
    gender_layout.addWidget(radio_male)  # Add the male radio button
    gender_layout.addWidget(radio_female)  # Add the female radio button
    form_layout.addRow("Select Gender",gender_layout) # Add a row to the form layout for Gender Selection

    # Weight section
    weight_kg = create_input_box("Must Be a Number","Enter your Weight in kg")    # Create an input box for weight

    # Height section
    height_m = create_input_box("Must Be a Number","Enter your Height in m")  # Create an input box for height  
    
    # BMI Calculation Button
    cal_bmi = create_push_button("Calculate BMI")  # Create a button for calculating BMI
    cal_bmi.setObjectName("cal_bmi") #set an object name to use in QSS
    
    cal_text = create_input_box("","")# Create a QLineEdit for displaying the calculated BMI

    bmi_cal_layout = QHBoxLayout()  # Create a horizontal layout for the BMI calculation button and Text
    bmi_cal_layout.addWidget(cal_bmi)   # Add the BMI calculation button to the layout
    bmi_cal_layout.addWidget(cal_text)  # Add the BMI display field to the layout
    form_layout.addRow(bmi_cal_layout)  # Add a row to the form layout for the BMI calculation button and display fields

    # Clear Button
    clear_bmi = create_push_button("Clear")  # Create a button for clearing all input fields
    clear_bmi.setObjectName("clear_bmi") #set an object name to use in QSS
    
    # Notice Section
    notice = QLabel("")

    # Clear and Notice Layout
    clear_notice_layout = QHBoxLayout()
    clear_notice_layout.addWidget(clear_bmi)
    clear_notice_layout.addWidget(notice)
    form_layout.addRow(clear_notice_layout)

    # Message to the user
    message = QLabel("Press ‘Clear’ to reset") # Create the label
    message.setVisible(False) # Make it hide by default
    message.setStyleSheet("color:red;") # Set the lable color 
    form_layout.addRow(message) # Add a row to the form layout for the message 

    bmi_widgets = {
    "age": age,
    "radio_male":radio_male,
    "radio_female":radio_female,
    "weight_kg": weight_kg, 
    "height_m": height_m,
    "cal_bmi": cal_bmi,
    "cal_text": cal_text,
    "clear_bmi":clear_bmi,
    "notice":notice,
    "message":message
    }  # Create a dictionary to hold references to the widgets for later use
    
    return bmi_window, bmi_widgets  # Return the window and the dictionary of widgets
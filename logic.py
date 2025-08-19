# -------------------------------
# Logic Module for BMI Calculator
# -------------------------------
def calculate_bmi(bmi_widgets:dict):
    # --- Get user input ---
    age = bmi_widgets["age"].text().strip()  # Get the age input from the widget and strip any whitespace
    weight = bmi_widgets["weight_kg"].text().strip()  # Get the weight input from the widget and strip any whitespace
    height = bmi_widgets["height_m"].text().strip()  # Get the height input from the widget and strip any whitespace

    # Define minimum and maximum valid age values
    min_age,max_age = 5,120  

    # -------------------------------
    # Functions for Validation styling
    # -------------------------------
    def input_invalid_style(widget,message):
        bmi_widgets[widget].setText(message) # If conversion fails, set the text to the provided message
        bmi_widgets[widget].setStyleSheet("color:red; font-weight:50")  # Set the text color to red and font weight to bold

    def input_valid_style(widget):
        bmi_widgets[widget].setStyleSheet("color:white; font-weight:normal") # If conversion succeeds, set the text color to black and font weight to normal
    
    valid = True # Initialize a flag to check if the input is valid - Starting assumption

    # ----------------------------
    #validate age input
    # ----------------------------
    try:
        if int(age):
            if int(age)<min_age or int(age)>max_age:
                input_invalid_style("age",f" Must Be Between {min_age} - {max_age}") # If age is not within the valid range, set an error message
                valid = False  # Set valid to False if age is invalid
            else:
                input_valid_style("age")    # If age is valid, set the style to normal
    except ValueError:
        input_invalid_style("age"," Invalid Age") # If conversion fails, set an error message
        valid = False

    # ----------------------------
    #validate gender input
    # ----------------------------
    if not bmi_widgets["radio_male"].isChecked() and not bmi_widgets["radio_female"].isChecked():
        input_invalid_style("cal_text"," Select Your Gender") # If user has not choose gender show this error message
        valid = False  # Set valid to False if Gender is not selected
    else:
       bmi_widgets["cal_text"].setText("")  # Clear the BMI display

    # ----------------------------
    #validate weight input
    # ----------------------------
    try:
        if float (weight):
            if not float (weight)>0:
                input_invalid_style("weight_kg"," Weight Must Be Positive") # If weight is not positive, set an error message
                valid = False  # Set valid to False if weight is invalid
            else:
                input_valid_style("weight_kg")  # If weight is valid, set the style to normal
    except ValueError:
        input_invalid_style("weight_kg"," Invalid Weight") # If conversion fails, set an error message
        valid = False

    # ----------------------------
    #validate height input
    # ----------------------------
    try:
        if not float(height)>0:
            input_invalid_style("height_m"," Weight Must Be Positive") # If height is not positive, set an error message
            valid = False # Set valid to False if height is invalid
        else:
            input_valid_style("height_m") # If height is valid, set the style to normal
    except ValueError:
        input_invalid_style("height_m"," Invalid Height") # If conversion fails, set an error message
        valid = False
    
    if valid:  # If all inputs are valid
        bmi = float(weight)/float(height)**2 
        bmi_widgets["cal_text"].setText(f"{bmi:.2f} kgm\u207B\u00B2")  # Calculate BMI and set the text of the BMI display field
        bmi_widgets["cal_text"].setStyleSheet("color:#d4af37; font-weight:bold;")

    # ----------------------------
    #BMI Evaluation & Status Display
    # ----------------------------
        # Freeze input & output text fields after the result
        for feeze_text in ["age","weight_kg","height_m","cal_text"]:
            bmi_widgets[feeze_text].setReadOnly(True)

        # Freeze radio buttons after the result
        for freeze_radio in ["radio_male","radio_female"]:
            bmi_widgets[freeze_radio].setEnabled(False)

        # Make visible message for the user
        bmi_widgets["message"].setVisible(True)
    
        # Function to update the notice label with a message and style
        def notice_style(message,tone):
            bmi_widgets["notice"].setText(message) # Display the message
            bmi_widgets["notice"].setStyleSheet(f"color:{tone}; font-weight:bold;") # Apply color & bold style

        # Evaluate BMI and display corresponding health category & risk
        if bmi < 18.5:
            notice_style("Underweight - High Risk","red")

        elif 18.5 <= bmi <= 24.9:
            notice_style("Normal - Healthy","green")

        elif 25.0 <= bmi <= 29.9:
            notice_style("Overweight - Increased Risk","pink")
        
        elif 30.0 <= bmi <=34.9:
            notice_style("Obesity I - High Risk","darkred")
        
        elif 35.0 <= bmi <=39.9:
            notice_style("Obesity II- High Risk","crimson")
        
        elif 40.0 <= bmi:
            notice_style("Obesity III - High Risk","red")

# ----------------------------
# Clear Input Fields & Selections
# ---------------------------- 
def clear_inputs(bmi_widgets:dict):
    # Clear text input, output fields
    for cls_inputs in ["age","weight_kg","height_m","cal_text","notice","message"]:
        bmi_widgets[cls_inputs].clear()
    
    #clearing radio button -  because of their exclusivity
    for radio_cls in ["radio_male","radio_female"]:
        r = bmi_widgets[radio_cls]
        r.setAutoExclusive(False) # Turn off the exclusivity
        r.setChecked(False)    # Uncheck the button - clearing
        r.setAutoExclusive(True) # Turn on the exclusivity after clearing
    # If not set - setAutoExclusive(True) both of them can be selected at the same time

    
    # Unfreeze input & output text fields after the result
    for ready_inputs in ["age","weight_kg","height_m","cal_text"]:
        bmi_widgets[ready_inputs].setReadOnly(False)

    # Unfreeze radio buttons after the result
    for freeze_radio in ["radio_male","radio_female"]:
        bmi_widgets[freeze_radio].setEnabled(True)
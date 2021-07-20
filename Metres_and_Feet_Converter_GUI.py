from tkinter import *
from functools import partial 
import random

class Welcome_Screen:
    def __init__(self, partner):
        
        # Formatting variables
        background_color = "light blue"
        
        # Welcome Screen GUI
        self.welcome_screen_frame = Frame(width=600, height=600, bg=background_color, pady=10)
        self.welcome_screen_frame.grid()

        # Main Heading (row 0)
        self.measurement_welcome_screen_label = Label(self.welcome_screen_frame, text="Measurement Converter", font=("Arial", "16", "bold"), bg=background_color, padx=10, pady=10)
        self.measurement_welcome_screen_label.grid(row=0)

        # Metres and Feet Button (row 1)
        self.m_and_ft_welcome_screen_button = Button(self.welcome_screen_frame, text="Metres and Feet", font=("Arial", "14"), command=self.Metres_and_Feet_Converter, padx=10, pady=10)
        self.m_and_ft_welcome_screen_button.grid(row=1)

    def Metres_and_Feet_Converter(self):
        get_Metres_and_Feet_Converter = Metres_and_Feet_Converter(self)

class Metres_and_Feet_Converter:
    def __init__(self, partner):
        
        # Formatting variables
        background = "orange"
        to_m_button_background = "dark orchid"
        to_ft_button_background = "green"

        # disable Metres and Feet button while window is open
        partner.m_and_ft_welcome_screen_button.config(state=DISABLED)

        # Metres and Feet Converter child window
        self.m_and_ft_box = Toplevel()
        
        # If users press cross at top, closes window and re-enables Metres and Feet button
        self.m_and_ft_box.protocol('WM_DELETE_WINDOW', partial(self.close_Metres_and_Feet_Converter, partner))

        # GUI Frame
        self.m_and_ft_frame = Frame(self.m_and_ft_box, bg=background)
        self.m_and_ft_frame.grid()

        # Metres and Feet Converter heading (row 0)
        self.m_and_ft_heading = Label(self.m_and_ft_frame, text="Metres and Feet Converter",
                                 font="arial 18 bold", bg=background, padx=10, pady=10)
        self.m_and_ft_heading.grid(row=0)

        # User instructions (row 1)
        self.m_and_ft_instructions_label = Label(self.m_and_ft_frame, text="Type in a measurement below and push the button you wish to convert the measurement to.",
                                        font="Arial 10 italic", wrap=300,
                                         justify=CENTER, bg=background,
                                        padx=10, pady=10)
        self.m_and_ft_instructions_label.grid(row=1)

        # Measurement input box (row 2)
        self.to_convert_input = Entry(self.m_and_ft_frame, width=20, font="Arial 20 bold")
        self.to_convert_input.grid(row=2)

        # "To Convert" buttons frame
        self.to_m_and_ft_buttons_frame = Frame(self.m_and_ft_frame)
        self.to_m_and_ft_buttons_frame.grid(row=3, pady=10)

        # To Metres button (row 3)
        self.to_m_button = Button(self.to_m_and_ft_buttons_frame, text="To Metres", font="Arial 10 bold", bg=to_m_button_background, padx=10, pady=10)
        self.to_m_button.grid(row=3, column=0)

        # To Feet button (row 3)
        self.to_ft_button = Button(self.to_m_and_ft_buttons_frame, text="To Feet", font="Arial 10 bold", bg=to_ft_button_background, padx=10, pady=10)
        self.to_ft_button.grid(row=3,column=1)

        # Conversion Result subheading (row 4)
        self.m_and_ft_result_subheading_label = Label(self.m_and_ft_frame, font="Arial 14", bg=background, pady=10, text="Conversion Result:")
        self.m_and_ft_result_subheading_label.grid(row=4)

        # Conversion Result (row 5)
        self.m_and_ft_result_label = Label(self.m_and_ft_frame, font = "Arial 11 bold", bg=background, fg="blue", pady=10, text="placeholder result")
        self.m_and_ft_result_label.grid(row=5)

        # Conversion History, Help and Dismiss buttons frame (row 6)
        self.m_and_ft_history_help_dismiss_buttons_frame = Frame(self.m_and_ft_frame)
        self.m_and_ft_history_help_dismiss_buttons_frame.grid(row=6, pady=10)

        # Conversion History button (row 6)
        self.m_and_ft_history_button = Button(self.m_and_ft_history_help_dismiss_buttons_frame, text="Conversion History", font="Arial 10 bold", bg="grey", padx=10, pady=10)
        self.m_and_ft_history_button.grid(row=6,column=0)

        # Help button (row 6)
        self.m_and_ft_help_button = Button(self.m_and_ft_history_help_dismiss_buttons_frame, text="Help", font="Arial 10 bold", bg="grey", padx=10, pady=10)
        self.m_and_ft_help_button.grid(row=6,column=1)

        # Dismiss button (row 6)
        self.m_and_ft_dismiss_button = Button(self.m_and_ft_history_help_dismiss_buttons_frame,
                                                                                                 text="Dismiss", font="Arial 10 bold", 
                                                                                                 bg="grey", 
                                                                                                 command=partial(self.close_Metres_and_Feet_Converter, partner),
                                                                                                 padx=10, pady=10)
        self.m_and_ft_dismiss_button.grid(row=6,column=2)

    def close_Metres_and_Feet_Converter(self, partner):
        # Put "Metres and Feet" button in welcome screen back to normal... 
        partner.m_and_ft_welcome_screen_button.config(state=NORMAL)
        self.m_and_ft_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Measurement Converter Tool")
    something = Welcome_Screen(root)
    root.mainloop()
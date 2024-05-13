
# Import Module
import tkinter as tk

# create root window
dasFenster = tk.Tk()
 
# root window title and dimension
dasFenster.title("Welcome to Tkinter after; sudo apt install python3-tk")
# Create a StringVar to associate with the label
text_var = tk.StringVar()
text_var.set("Starte in Terminal not vscode")

# Create the label widget with all options
label = tk.Label(dasFenster, 
                 textvariable=text_var, 
                 anchor=tk.CENTER,       
                 bg="lightblue",      
                 height=3,              
                 width=30,              
                 bd=3,                  
                 font=("Arial", 16, "bold"), 
                 cursor="hand2",   
                 fg="red",             
                 padx=15,               
                 pady=15,                
                 justify=tk.CENTER,    
                 relief=tk.RAISED,     
                 underline=0,           
                 wraplength=250         
                )

# Pack the label into the window
label.pack(pady=20)  # Add some padding to the top

# Set geometry (widthxheight)
dasFenster.geometry('444x200')
 
# all widgets will be here
# Execute Tkinter
dasFenster.mainloop()

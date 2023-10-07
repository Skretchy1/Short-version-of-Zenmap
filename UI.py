import tkinter as tk
from tkinter import filedialog

import CORS
import HTTPCookies
import geoLookup
import serviceDiscovery
import serviceScanTest


def scan_function():
    # Code to run when the Scan button is clicked
    if selected_option.get() == "Locate":
        result = geoLookup.geolocation(e1.get())
        text_widget.config(state="normal")
        text_widget.insert(tk.END, result)
        text_widget.config(state="disabled")

    if selected_option.get() == "Service Scan":
        text_widget.config(state="normal")
        text_widget.insert(tk.END, "(Running service scan)\n")
        text_widget.config(state="disabled")
        result = serviceDiscovery.serviceScan(host=e1.get())
        text_widget.config(state="normal")
        text_widget.insert(tk.END, result)
        text_widget.config(state="disabled")

    if selected_option.get() == "Check CORS":
        result = CORS.scan(e1.get())
        text_widget.config(state="normal")
        text_widget.insert(tk.END, result)
        text_widget.config(state="disabled")

    if selected_option.get() == "Cookies scan":
        result = HTTPCookies.scan(e1.get())
        text_widget.config(state="normal")
        text_widget.insert(tk.END, result)
        text_widget.config(state="disabled")



def select_directory():
    file_path = filedialog.askopenfilename()
    print(file_path)


window = tk.Tk()
window.title("Zenmap GUI")
window.geometry("1400x900")


label = tk.Label(window, text="Target:",).grid(row = 0, column = 0)
# label.pack(side="left",fill="x", pady=100)

# Text box for IP input
# ip_input = tk.Entry(window, width=30)
# ip_input.pack(side="left")

# e1 = tk.Entry(window).place(x = 80, y = 50)
e1 = tk.Entry(window, width=40)
e1.grid(row = 0, column = 1)


#FOR THE PROFILE:

label_profile = tk.Label(window, text="Profile:",).grid(row = 0, column = 3, padx=(20, 0))
# label.pack(side="left",fill="x", pady=100)

# Text box for IP input
# ip_input = tk.Entry(window, width=30)
# ip_input.pack(side="left")

# e1 = tk.Entry(window).place(x = 80, y = 50)
# e2 = tk.Entry(window, width=40).grid(row = 0, column = 4)

# Define a list of options for the dropdown menu
options = ["Locate", "Service Scan", "Cookies scan", "Check CORS"]

# Set a default value for the dropdown menu
selected_option = tk.StringVar(window)
selected_option.set(options[0])

# Create the dropdown menu using the OptionMenu widget
option_menu = tk.OptionMenu(window, selected_option, *options).grid(row = 0, column = 4)



# Button to start the scan
scan_button = tk.Button(window, text="Scan", command=scan_function).grid(row = 0, column = 5, padx=(20, 0))
# scan_button.pack()

# Button to pick a file
scan_button = button = tk.Button(window, text="Browse", command=select_directory).grid(row = 1, column = 0, padx=(10, 0), pady=(5, 0))


# frame = tk.Frame(window, bg='gray', bd=5).grid(row = 2, column = 0, padx=(5, 0), pady=(5, 0))
# Buttons for picking either hosts or Services
host_button = button = tk.Button(window, text="Hosts").grid(row = 2, column = 0, padx=(150, 0), pady=(15, 0))
services_button = button = tk.Button(window, text="Services").grid(row = 2, column = 0, padx=(50, 0),pady=(15, 0))

# LISTBOX
listbox = tk.Listbox(window, width=40, height=50).grid(row = 3, column = 0, columnspan=2, rowspan=1)


# THE SHOWING SECTION
# text_widget = tk.Text(window, height=150, width=50).grid(row = 3, column = 2, columnspan=2, rowspan=1) # IT LOOKS PERFECT
# text_widget.insert( 'SHOWING STUFF\n HERE \n')

nmap_output = button = tk.Button(window, text="Nmap Output").grid(row = 2, column = 2, pady=(13, 0))
hosts_ports = button = tk.Button(window, text="Host/Ports").grid(row = 2, column = 3, pady=(13, 0))



text_widget = tk.Text(window, height=50, width=100)
text_widget.grid(row = 3, column = 2, columnspan=20, rowspan=1)# IT LOOKS MORE PERFECT
text_widget.config(state= "disabled")


scrollbar = tk.Scrollbar(window, command=text_widget.yview)
scrollbar.grid(row=3, column=22, sticky="NS")


text_widget.config(yscrollcommand=scrollbar.set, state="disabled")


# STARTING OF THE MENU
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# SCAN MENU
scan_menu = tk.Menu(menu_bar, tearoff=0)
scan_menu.add_command(label="New")
scan_menu.add_command(label="Open")
scan_menu.add_separator()
scan_menu.add_command(label="Quit", command=quit)
menu_bar.add_cascade(label="Scan", menu=scan_menu)

# TOOLS MENU
tools_menu = tk.Menu(menu_bar, tearoff=0)
tools_menu.add_command(label="Cut")
menu_bar.add_cascade(label="Tools", menu=tools_menu)

# PROFILE MENU
profile_menu = tk.Menu(menu_bar, tearoff=0)
profile_menu.add_command(label="About", command=scan_function)
menu_bar.add_cascade(label="Profile", menu=profile_menu)

# HELP MENU
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=scan_function)
menu_bar.add_cascade(label="Help", menu=help_menu)



target_label = tk.Label(window, text="Target:")
# target_label.pack()

w = tk.Spinbox(window, from_ = 0, to = 9999)
# w.pack()



if __name__ == "__main__":
    window.mainloop()




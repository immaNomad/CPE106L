import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    # Create the root window (optional)
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog and get the selected file
    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )

    # Check if a file was selected
    if file_path:
        print("Selected file:", file_path)
        return file_path
    else:
        return None

# Call the function to open the file dialog and get the selected file path
selected_file = open_file_dialog()
if selected_file:
    # You can now use the selected_file variable to access the selected file
    with open(selected_file, 'r') as file:
        content = file.read()
        print("File content:", content)
else:
    print("No file selected.")

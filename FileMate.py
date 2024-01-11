import os
import shutil
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import filedialog

def organize_folder(target_folder):
    # Organize files based on type and modified date (similar to the previous script)
    # ...
     # Get all files in the target folder
    files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]

    for file in files:
        file_path = os.path.join(target_folder, file)
        modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))

        # Create a folder based on the modified date
        folder_name = modified_date.strftime("%Y-%m-%d")
        folder_path = os.path.join(target_folder, folder_name)

        # Move images to the 'Photos' folder
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            folder_path = os.path.join(target_folder, 'Photos', folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f'Moved {file} to Photos folder ({folder_name}).')

        # Move documents to the 'Documents' folder
        elif file.lower().endswith(('.doc', '.docx', '.txt', '.pdf')):
            folder_path = os.path.join(target_folder, 'Documents', folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f'Moved {file} to Documents folder ({folder_name}).')

        # Move videos to the 'Videos' folder
        elif file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
            folder_path = os.path.join(target_folder, 'Videos', folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f'Moved {file} to Videos folder ({folder_name}).')

        # Move PDFs to the 'PDFs' folder
        elif file.lower().endswith('.pdf'):
            folder_path = os.path.join(target_folder, 'PDFs', folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f'Moved {file} to PDFs folder ({folder_name}).')

        # Move ZIP files to the 'Zip' folder
        elif file.lower().endswith('.zip'):
            folder_path = os.path.join(target_folder, 'Zip', folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f'Moved {file} to Zip folder ({folder_name}).')

        # Move executable files and others to the 'Others' folder
        else:
            folder_path = os.path.join(target_folder, 'Others', folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f'Moved {file} to Others folder ({folder_name}).')

def delete_old_files(target_folder, threshold_days):
    # Create a folder for deleted files
    delete_folder = os.path.join(target_folder, 'Delete')
    if not os.path.exists(delete_folder):
        os.makedirs(delete_folder)

    # Get all files in the target folder
    files = [f for f in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, f))]

    current_date = datetime.now()

    for file in files:
        file_path = os.path.join(target_folder, file)
        modified_date = datetime.fromtimestamp(os.path.getmtime(file_path))

        # Calculate the days difference
        days_difference = (current_date - modified_date).days

        if days_difference >= threshold_days:
            # Move the file to the 'Delete' folder
            shutil.move(file_path, os.path.join(delete_folder, file))
            print(f'Moved {file} to Delete folder (old file).')

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry_var.set(folder_path)

def run_operation():
    target_folder = entry_var.get()

    # Check the selected operation
    if operation_var.get() == "Organize":
        organize_folder(target_folder)
        result_label.config(text="Organizing completed successfully.")
    elif operation_var.get() == "Delete":
        delete_old_files(target_folder, threshold_days_var.get())
        result_label.config(text="Deleting completed successfully.")

# Create the main window
root = tk.Tk()
root.title("File Organizer and Deleter")

# Create and set up GUI components
label = tk.Label(root, text="Enter the path to the target folder:")
label.pack(pady=10)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=40)
entry.pack(pady=10)

browse_button = tk.Button(root, text="Browse", command=select_folder)
browse_button.pack(pady=10)

operation_var = tk.StringVar()
operation_var.set("Organize")

operation_label = tk.Label(root, text="Select operation:")
operation_label.pack(pady=10)

operation_radiobutton1 = tk.Radiobutton(root, text="Organize", variable=operation_var, value="Organize")
operation_radiobutton1.pack(pady=5)

operation_radiobutton2 = tk.Radiobutton(root, text="Delete", variable=operation_var, value="Delete")
operation_radiobutton2.pack(pady=5)

threshold_days_var = tk.IntVar()
threshold_days_var.set(5)

threshold_days_label = tk.Label(root, text="Enter threshold days for deleting old files:")
threshold_days_label.pack(pady=5)

threshold_days_entry = tk.Entry(root, textvariable=threshold_days_var, width=5)
threshold_days_entry.pack(pady=5)

run_button = tk.Button(root, text="Run Operation", command=run_operation)
run_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()

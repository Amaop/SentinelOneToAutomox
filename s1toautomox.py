import csv
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

def transform_columns(input_file, output_file):
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip the first row (header row)
        rows = list(reader)

    extracted_first_column = [row[0] for row in rows]  # Extracting the first column
    extracted_sixth_column = [row[5] for row in rows]  # Extracting the sixth column

    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Writing the header row
        writer.writerow(['Hostname', 'CVE-ID', 'Severity'])

        for i in range(len(rows)):
            writer.writerow([extracted_first_column[i], rows[i][1], extracted_sixth_column[i].lower()])

    print(f"Transformation completed. Result written to '{output_file}'.")

# Create Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select the input file
input_file = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
if not input_file:
    print("No input file selected. Exiting the script.")
    exit()

now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")
dynamic_output_file = f"output_{timestamp}.csv"

# Perform the transformation
transform_columns(input_file, dynamic_output_file)

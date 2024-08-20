import os
import csv
from datetime import date

def generate_report(folder_path: str, report_file: str) -> None:
    # Check if the specified folder path is a valid directory
    if os.path.isdir(folder_path):
        # Generate report data: list of [folder name, number of files]
        report_data = [[folder, len(os.listdir(os.path.join(folder_path, folder)))]
                       for folder in os.listdir(folder_path) 
                       if os.path.isdir(os.path.join(folder_path, folder))]
        
        # Write the report data to the CSV file
        with open(report_file, 'w', newline='') as csvfile:
            # Write header and report data
            csv.writer(csvfile).writerows([['Folder Name', 'Number of Files']] + report_data)
        
        # Print success message
        print(f"Report generated successfully: {report_file}")
    else:
        # Print error message if the path is not a valid directory
        print(f"Error: '{folder_path}' is not a valid directory.")

# Define the folder path and the name of the report file
folder_path = 'C:\\Users\\praga\\Desktop\\cognifyz tasks\\Level 3'
report_file = f'C:\\Users\\praga\\Desktop\\cognifyz tasks\\Level 3\\employees_{date.today().strftime("%y-%m-%d")}.csv'

# Generate the report by calling the function
generate_report(folder_path, report_file)


# #OUTPUT:-
# Report generated successfully: C:\Users\praga\Desktop\cognifyz tasks\Level 3\employees_24-08-08.csv

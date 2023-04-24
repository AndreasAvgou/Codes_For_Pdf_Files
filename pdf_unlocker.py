import os
import fitz

# Get the directory path of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input folder path containing the PDF files
input_folder_path = os.path.join(script_dir)

# Define the output folder path to save the decrypted PDF files
output_folder_path = os.path.join(script_dir, 'FolderName')

# Loop through each file in the input folder
for filename in os.listdir(input_folder_path):
    # Check if the file is a PDF
    if filename.endswith('.pdf'):
        # Open the PDF file
        pdf_file = fitz.open(os.path.join(input_folder_path, filename))

        # Create a PDF document object
        pdf_doc = fitz.open()

        # Loop through each page of the PDF file
        for page_num in range(pdf_file.page_count):
            # Get the current page of the PDF file
            page = pdf_file[page_num]
            pdf_doc.insert_pdf(pdf_file, from_page=page_num, to_page=page_num)

        # Save the modified PDF file to the output folder
        output_file_path = os.path.join(output_folder_path, filename)
        pdf_doc.save(output_file_path)

        # Close the input and output files
        pdf_file.close()

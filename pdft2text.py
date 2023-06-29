import os
import PyPDF2

def pdf_to_text(pdf_path, output_dir):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Extract file name without extension
    file_name = os.path.splitext(os.path.basename(pdf_path))[0]

    output_path = os.path.join(output_dir, file_name + '.txt')

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(text)

    print(f"Text extracted successfully. Output file: {output_path}")


# Create the "textfiles" directory if it doesn't exist
output_dir = os.path.join(os.getcwd(), 'textfiles')
os.makedirs(output_dir, exist_ok=True)

while True:
    # Specify the path to the PDF file
    pdf_path = input("Enter the path to the PDF file (or 'exit' to quit): ")

    if pdf_path.lower() == 'exit':
        break

    # Convert PDF to text
    pdf_to_text(pdf_path, output_dir)

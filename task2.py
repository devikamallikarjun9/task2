import csv
from fpdf import FPDF

# Function to read data from a CSV file
def read_data_from_file(filename):
    data = []
    with open(filename, mode='r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)  # Skip the header
        for row in csvreader:
            data.append(row)
    return data

# Function to analyze the data (basic analysis example)
def analyze_data(data):
    total_value = 0
    row_count = len(data)
    for row in data:
        try:
            total_value += float(row[1])  # Assuming the second column has numerical data
        except ValueError:
            continue
    return row_count, total_value

# Function to generate a PDF report
def generate_pdf_report(row_count, total_value, filename="report.pdf"):
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Data Analysis Report', ln=True, align='C')

    # Add summary section
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, f'Total Rows in Data: {row_count}', ln=True)
    pdf.cell(200, 10, f'Total Value in Column 2: {total_value}', ln=True)

    # Save the PDF
    pdf.output(filename)
    print(f"Report generated successfully and saved as {filename}")

# Main function to tie everything together
def main():
    # Read and analyze data
    filename = 'sample_data.csv'
    data = read_data_from_file(filename)
    row_count, total_value = analyze_data(data)

    # Generate PDF report
    generate_pdf_report(row_count, total_value)

# Run the script
if _name_ == "_main_":
    main()
eatures
Reads data from a CSV file

Performs basic analysis:

Counts total rows

Sums up values in the second column

Generates a clean PDF report

📦 Requirements
Install dependencies using pip:

bash
Copy code
pip install fpdf
📁 Project Structure
graphql
Copy code
├── sample_data.csv          # Input CSV file
├── report.pdf               # Output PDF report (auto-generated)
├── data_report.py           # Python script
└── README.md                # Documentation (you’re reading it)
🧪 How to Use
Make sure your CSV file (e.g., sample_data.csv) has at least two columns. Example:

c
Copy code
Name,Amount
Product A,100
Product B,200
Product C,150
Update the filename variable in the script if needed:

python
Copy code
filename = 'sample_data.csv'
Run the script:

bash
Copy code
python data_report.py

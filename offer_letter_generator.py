from fpdf import FPDF

# Step 1: Get user input
name = input("Enter your full name: ")
domain = input("Enter your internship domain (e.g., Python): ")
start_date = input("Enter your internship start date: ")

# Step 2: Create a PDF document
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=14)
pdf.cell(200, 10, txt="MITS Internship Offer Letter", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt=f"""
To,
{name}

Congratulations! You have been selected for the MITS Virtual Internship Program in the domain of {domain}.

Start Date: {start_date}
Duration: 4 Weeks

We look forward to your contribution and learning.

Best wishes,
Micro Information Technology Services (MITS)
""")

# Step 3: Save PDF
file_name = f"Offer_Letter_{name.replace(' ', '_')}.pdf"
pdf.output(file_name)
print(f"\n✅ PDF saved successfully as: {file_name}")

# Step 1: Install the fpdf2 and markdown libraries
# You can install them using pip if you haven't already:
# pip install fpdf2 markdown

from fpdf import FPDF, HTMLMixin
import markdown


class MyFPDF(FPDF, HTMLMixin):
    pass


# Step 2: Read the content of the Markdown file
input_file_path = '../docs/sample_data.md'
with open(input_file_path, 'r', encoding='utf-8') as file:
    md_content = file.read()

# Step 3: Convert the Markdown content to HTML
html_content = markdown.markdown(md_content)

# Step 4: Create a PDF object
pdf = MyFPDF()

# Step 5: Add a page to the PDF
pdf.add_page()

# Step 6: Set the font and size for the text
pdf.set_font("Arial", size=12)

# Step 7: Write the HTML content to the PDF
pdf.write_html(html_content)

# Step 8: Save the PDF to a file
output_file_path = '../docs/sample_data.pdf'
pdf.output(output_file_path)

print(f"PDF created successfully and saved as {output_file_path}")

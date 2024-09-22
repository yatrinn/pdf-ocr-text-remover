import fitz  # Import PyMuPDF
import re

def remove_text_from_content_stream(content):
    """
    Removes text between BT (Begin Text) and ET (End Text) operators in the PDF content stream.
    """
    pattern = re.compile(rb'BT.*?ET', re.DOTALL)
    content = re.sub(pattern, b'', content)
    return content

def process_pdf(input_pdf, output_pdf):
    """
    Processes the PDF file to remove all text content.

    Args:
        input_pdf (str): Path to the input PDF file.
        output_pdf (str): Path to save the output PDF file without text.
    """
    doc = fitz.open(input_pdf)
    for page_num in range(len(doc)):
        page = doc[page_num]
        xrefs = page.get_contents()
        if xrefs is None:
            continue
        for xref in xrefs:
            stream = doc.xref_stream(xref)
            # Remove text between BT and ET operators
            new_stream = remove_text_from_content_stream(stream)
            # Update the content stream
            doc.update_stream(xref, new_stream)
    doc.save(output_pdf)

if __name__ == "__main__":
    input_pdf = "/path/to/your/input.pdf"  # Replace with the path to your input PDF
    output_pdf = "/path/to/your/output.pdf"  # Replace with the desired path for the output PDF
    process_pdf(input_pdf, output_pdf)

<<<<<<< HEAD
# PDF OCR Text Remover

A Python script that removes the OCR scan from PDF files using PyMuPDF (https://pymupdf.readthedocs.io/) (fitz). This script processes the PDF to remove the recognized text generated from OCR (Optical Character Recognition). It's especially useful for PDFs created by physically scanning paper documents and applying OCR afterward, as it only removes the OCR layer, not the actual content of the scanned image.
Important! If the PDF contains computer-generated text, this will also be fully removed from the resulting file. Therefore, this script is best suited for PDFs created from scanned paper documents where no original text needs to be preserved.

## **Features**

- **OCR Text Removal**: Removes all text content from a PDF file.
- **Preserves Images**: Keeps images intact while removing text. 
- **Easy to Use**: Simple script that can be customized as needed.

## **Prerequisites**

- Python 3.x
- [PyMuPDF (fitz)](https://pypi.org/project/PyMuPDF/)

## **Installation**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YourUsername/pdf-ocr-text-remover.git
=======
# pdf-ocr-text-remover
A Python script using PyMuPDF (fitz) that removes OCR scans from PDF files. It processes the PDF to eliminate recognized text from OCR processing, especially useful for scanned paper documents. Note: Any computer-generated text in the PDF will also be removed, so it's ideal for scanned paper pages.
>>>>>>> e95a8295fde0c2bb3080f311cc28176121f816ea

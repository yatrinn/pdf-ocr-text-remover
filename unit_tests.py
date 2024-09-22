import unittest
from unittest.mock import MagicMock, patch
from remove_ocr_text import process_pdf, remove_text_from_content_stream

class TestRemoveOCRText(unittest.TestCase):
    @patch('fitz.open')
    def test_process_pdf(self, mock_fitz_open):
        # Mock the document
        mock_doc = MagicMock()
        mock_fitz_open.return_value = mock_doc

        # Mock the number of pages
        mock_doc.__len__.return_value = 2

        # Mock pages
        mock_page = MagicMock()
        mock_doc.__getitem__.return_value = mock_page

        # Mock get_contents to return xrefs
        mock_page.get_contents.return_value = [1, 2]

        # Mock xref_stream and update_stream
        mock_doc.xref_stream.return_value = b"BT some text ET"
        mock_doc.update_stream.return_value = None

        # Run the function
        input_pdf = "/path/to/your/input.pdf"
        output_pdf = "/path/to/your/output.pdf"
        process_pdf(input_pdf, output_pdf)

        # Assertions
        mock_fitz_open.assert_called_with(input_pdf)
        self.assertEqual(mock_doc.save.call_count, 1)
        mock_doc.save.assert_called_with(output_pdf)

    def test_remove_text_from_content_stream(self):
        # Test the remove_text_from_content_stream function directly
        content = b"Some content BT This is text ET More content"
        expected_result = b"Some content  More content"

        result = remove_text_from_content_stream(content)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

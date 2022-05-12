from typing import List, Tuple
from pdf_file_iterator import PdfFileIterator
import fitz


class PdfMerger:

    def find_and_merge(self, dir_to_scan: str, output_file_path: str):
        merged_pdf_doc = fitz.open()
        files = []
        for filepath in PdfFileIterator().iterate(dir_to_scan):
            files.append(filepath)

        for filepath in sorted(files):
            pages_index = 0
            doc = fitz.open(filepath)
            print(f'Appending {filepath}')
            for _ in doc:
                merged_pdf_doc.insert_pdf(doc, from_page=pages_index, to_page=pages_index)
                pages_index += 1
            pass

        merged_pdf_doc.save(output_file_path)
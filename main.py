import os.path

from pdf_merger import PdfMerger
from pdf_file_iterator import PdfFileIterator

if __name__ == "__main__":
    extractor = PdfMerger()
    extractor.find_and_merge(
        '/path/to/folder',
        '/path/to/output/pdf'
    )
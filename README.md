# MyToolKit

This repository contains a collection of scripts for various utilities.

## Files Overview

- **fisher.pl**  
  A Perl script. Specific usage details should be added as needed.

- **str_length.py**  
  A Python script intended for string length operations. Additional documentation can be added for further clarification.

- **pdf_process/remove_all_annotation_in_pdf.py**  
  A Python script that removes all annotations (highlight, comment, underline, etc.) from PDF files using [PyMuPDF](https://pymupdf.readthedocs.io/). It can process a single PDF file or an entire directory of PDFs.

## PDF Annotation Removal Tool

### Description
The `remove_all_annotation_in_pdf.py` script removes all annotations from PDF files and saves the cleaned document with a modified filename. The cleaned file is saved with the `_ann_cleaned.pdf` suffix.

### Requirements
- Python 3.x
- [PyMuPDF](https://pymupdf.readthedocs.io/) (Install with: `pip install PyMuPDF`)

### Usage

#### Processing a Single PDF File
Run the script with a PDF file as the argument:
```bash
python pdf_process/remove_all_annotation_in_pdf.py input.pdf
```
This will create a new PDF file named `input_ann_cleaned.pdf` in the same directory.

#### Processing a Directory of PDFs
Pass a directory path as the argument:
```bash
python pdf_process/remove_all_annotation_in_pdf.py /path/to/directory
```
The script will process all PDF files in the directory (excluding files that already end with `_ann_cleaned.pdf`) and save each cleaned file with the `_ann_cleaned.pdf` suffix.

## Additional Notes
- Ensure that the required Python modules are installed before running the scripts.
- Contributions and updates are welcome.
- For any issues, please refer to the script comments and documentation or raise an issue in the repository.

## Support & Contributions

If you find the plugin useful, please consider [buying me a coffee](https://buymeacoffee.com/niehu2015o) to support ongoing development.

## License

[MIT](LICENSE)

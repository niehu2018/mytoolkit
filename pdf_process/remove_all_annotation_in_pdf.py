try:
    import fitz  # PyMuPDF
except ModuleNotFoundError:
    print("Module 'fitz' not found. Please install PyMuPDF with: pip install PyMuPDF")
    exit(1)

def remove_pdf_annotations(input_pdf: str, output_pdf: str):
    """
    Remove all annotations (highlight, comment, underline, etc.) from a PDF file and save it.
    
    Parameters:
    input_pdf (str): Input PDF file path.
    output_pdf (str): Output PDF file path.
    """
    try:
        doc = fitz.open(input_pdf)
        for page in doc:
            annots = page.annots()
            if annots:
                for annot in annots:
                    page.delete_annot(annot)
        doc.save(output_pdf)
        doc.close()
        print(f"Annotations removed successfully, saved as: {output_pdf}")
    except Exception as e:
        print(f"Error: {e}")

import os
import sys
# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_all_annotation_in_pdf.py input.pdf or directory")
        sys.exit(1)
    input_path = sys.argv[1]
    if os.path.isdir(input_path):
        # Process all PDF files in the directory, skipping files ending with "_ann_cleaned.pdf"
        for file in os.listdir(input_path):
            if file.endswith("_ann_cleaned.pdf"):
                continue
            if file.endswith(".pdf"):
                pdf_file = os.path.join(input_path, file)
                prefix = pdf_file[:-4]
                output_pdf = f"{prefix}_ann_cleaned.pdf"
                print(f"Processing: {pdf_file}")
                remove_pdf_annotations(pdf_file, output_pdf)
    elif input_path.endswith(".pdf"):
        prefix = input_path[:-4]
        output_pdf = f"{prefix}_ann_cleaned.pdf"
        remove_pdf_annotations(input_path, output_pdf)
    else:
        print("Input path must be a PDF file or a directory containing PDF files")
        sys.exit(1)

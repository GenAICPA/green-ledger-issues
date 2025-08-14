import docx
import sys

def extract_text_from_docx(filename):
    """Extracts text from a .docx file and prints it to standard output."""
    try:
        doc = docx.Document(filename)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return '\n'.join(full_text)
    except Exception as e:
        return f"Error reading docx file: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        text = extract_text_from_docx(sys.argv[1])
        print(text)
    else:
        print("Please provide the path to the .docx file as an argument.")

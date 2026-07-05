import pandas as pd #csv file reader
from pathlib import Path #to handle file paths
from docx import Document #to read docx files
from pypdf import PdfReader #to read pdf files

#its first file
#################################################


KNOWLEDGE_BASE_DIR = Path("knowledge_base") #to store the knowledge base files(to be read in this case)


def read_txt_or_md(file_path: Path) -> str: #to read text or markdown files
    return file_path.read_text(encoding="utf-8") #to read the content of the file and return it as a string(utf-8 encoding is used to handle special characters))
#utf-8 to read arabic characters and other special characters in the text files


def read_pdf(file_path: Path) -> str: #to read pdf files
    reader = PdfReader(file_path) #to read the pdf file and extract the text from it
    text = "" #to store the extracted text from the pdf file


    for page in reader.pages: #to iterate through each page of the pdf file and extract the text from it
        page_text = page.extract_text() #to extract the text from the current page of the pdf file
        if page_text: 
            text += page_text + "\n" #to add the extracted text from the current page to the overall text variable, along with a newline character for formatting
#to add the string to text file
    return text


def read_docx(file_path: Path) -> str:
    document = Document(file_path)
    text = ""

    for paragraph in document.paragraphs: #to iterate through each paragraph in the docx file and extract the text from it
        text += paragraph.text + "\n"

    return text #to return the extracted text from the docx file as a string, with each paragraph separated by a newline character for formatting




def read_csv(file_path: Path) -> str:
    df = pd.read_csv(file_path)
    return df.to_string(index=False)


def load_documents(): #to load the documents from the knowledge base directory and return them as a list of dictionaries, where each dictionary contains the file name and its content
    documents = []  #this class is used to store the documents that are read from the knowledge base directory

    for file_path in KNOWLEDGE_BASE_DIR.iterdir():
        if file_path.is_file(): #to see the files only in the knowledge base directory and ignore any subdirectories or other non-file items
            suffix = file_path.suffix.lower() #to get the file extension of the current file and convert it to lowercase for consistency

            try:
                if suffix in [".txt", ".md"]:
                    content = read_txt_or_md(file_path)

                elif suffix == ".pdf":
                    content = read_pdf(file_path)

                elif suffix == ".docx":
                    content = read_docx(file_path)

                elif suffix == ".csv":
                    content = read_csv(file_path)

                else:
                    print(f"Unsupported file type: {file_path.name}")
                    continue

                documents.append({
                    "file_name": file_path.name,
                    "content": content
                })

            except Exception as e:
                print(f"Error reading {file_path.name}: {e}")

    return documents
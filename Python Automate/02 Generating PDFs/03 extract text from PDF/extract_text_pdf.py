import fitz

with fitz.open(r"02 Generating PDFs\03 extract text from PDF\students.pdf") as pdf:
    text = ''
    for page in pdf:
        text = text + page.get_text()
    print(text)    
    
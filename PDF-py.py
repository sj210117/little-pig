from PyPDF2 import PdfReader
 
with open('/Users/shaojie/Desktop/1.pdf', 'rb') as pdf_file:
    pdf_reader = PdfReader(pdf_file)
    
 
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        print(text)

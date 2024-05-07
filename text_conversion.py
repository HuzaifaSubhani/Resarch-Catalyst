import PyPDF2

def pdf_to_string(pdf_file):

    pdf_reader = PyPDF2.PdfReader(pdf_file)
    extracted_text = ""
    for page_num in range(len(pdf_reader.pages)):  
      page = pdf_reader.pages[page_num]
      try:
        extracted_text += page.extract_text()  
      except: 
        pass
    return extracted_text.strip()  

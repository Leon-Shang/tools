import PyPDF2






class FindInPaper:

    def extract_text_pypdf2(self, file_path):
        
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""

            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
        return text
    

    def find(self, text, keyword):
        if keyword in text:
            return True
        return False
    
    


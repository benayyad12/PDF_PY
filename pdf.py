from base64 import encode
from fpdf import FPDF 

pdf = FPDF(orientation='P', unit='mm', format='A4')

pdf.add_page()

pdf.compress = False 

def titles(self):
        self.set_xy(0.0,0.0)
        self.set_font('Arial', 'B', 16)
        self.set_text_color(220, 50, 50)
        self.cell(w=210.0, h=40.0, align='C', txt="Scholarship application motivation letter example", border=0)
        
titles(pdf)



def texts(self,name):
        with open(name,'rb') as xy:
            txt=xy.read().decode('latin-1')
        self.set_xy(10.0,80.0)    
        self.set_text_color(76.0, 32.0, 250.0)
        self.set_font('Arial', '', 12)
        self.multi_cell(0,10,txt)
        
texts(pdf,'/Users/abdessalambenayyad/Desktop/pdf_py/text.txt')
        
pdf.output('cover_letter.pdf', 'F')

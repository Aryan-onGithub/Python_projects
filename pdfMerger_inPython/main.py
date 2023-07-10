import PyPDF2   #used to do operation in pdf

files = ["PDF1.pdf", "PDF2.pdf"]
merger = PyPDF2.PdfMerger()

for file in files:
    PDFfile = open(file, "rb")                 #read each pdf in binary mode
    PDF_reader = PyPDF2.PdfReader(PDFfile)     #reads pdf in PDF_reader dsing Pdfreader
    merger.append(PDF_reader)                  #adds pdf to merger
    PDFfile.close()
merger.write("merged.pdf")                     #makes a file merged.pdf and write merger in it
import PyPDF2
import os

# list all the PDFs to be merged
pdfFiles = [file for file in os.listdir() if file.endswith('.pdf')]

# Create a PdfFileMerger object
pdfMerger = PyPDF2.PdfMerger()

for file in pdfFiles:
    with open(file, 'rb') as pdf:
        pdfMerger.append(pdf)

# Save the merged PDF to a file
pdfMerger.write(open('merged.pdf', 'wb'))

# Close the PDF files
pdfMerger.close()

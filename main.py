from PyPDF2 import PdfFileWriter, PdfFileReader

inputpdf = PdfFileReader(open("Diploma Thesis.pdf","rb"))

output = PdfFileWriter()
for i in range(13):
    output.addPage(inputpdf.getPage(i))

with open("part1.pdf", "wb") as outputStream:
    output.write(outputStream)
# PyPDF2 can read, arrange, and add pages
# PyPDF2 can't extract images or charts
# you cant change the individual text, font, or layout because pdf's are binary files
# no PDF library can do these things
import PyPDF2

# rb means read binary
my_pdf = open('meetingminutes1.pdf', 'rb')
reader = PyPDF2.PdfFileReader(my_pdf)

# get number of pages
number_of_pages = reader.numPages

# get a specific page
page = reader.getPage(0)

# extract text
text = page.extractText()

# get all the text
# for pageNum in range(reader.numPages):
#     print(reader.getPage(pageNum).extractText())

# combine PDFs___________________________________________________________________________________________

my_pdf2 = open('meetingminutes2.pdf', 'rb')
reader2 = PyPDF2.PdfFileReader(my_pdf2)

# create a new pdf
new_pdf = PyPDF2.PdfFileWriter()

# add pages to the new_pdf
for pageNum in range(reader.numPages):
    page = reader.getPage(pageNum)
    new_pdf.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    new_pdf.addPage(page)

# open in write binary
combined_pdf = open('combined.pdf', 'wb')
new_pdf.write(combined_pdf)
combined_pdf.close()
my_pdf.close()
my_pdf2.close()
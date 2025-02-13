import tabula
 
table = tabula.read_pdf(r"02 Generating PDFs\05 extract table from PDF to excel\Table and Text.pdf", pages=1)
table[0].to_excel(r"02 Generating PDFs\05 extract table from PDF to excel\output.xlsx", index=None)
import tabula

table = tabula.read_pdf(r"02 Generating PDFs\04 extracting tables from PDF\weather.pdf", pages=1)

print(type(table[0]))

table[0].to_csv(r'02 Generating PDFs\04 extracting tables from PDF\output.csv', index=None)
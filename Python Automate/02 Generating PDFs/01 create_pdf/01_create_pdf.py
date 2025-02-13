from fpdf import FPDF

# Cria o objeto PDF
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

# Adiciona a imagem com o caminho relativo
pdf.image(r"02 Generating PDFs\01 create_pdf\tiger.jpeg", w=80, h=50)

pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=15, txt="Malayan Tiger", align='C', ln=1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=0, h=15, txt= 'Description', ln= 1)

pdf.set_font(family='Times', size=12)
txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts of the Malay Peninsula, and has been classified as critically endangered. As of April 2014, the population was estimated at 80 - 120 mature individuals, with a continuing downward trend."""
pdf.multi_cell(w=0, h=15, txt=txt1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=15, txt= 'Kingdom: ')

pdf.set_font(family='Times',  size=14)
pdf.cell(w=100, h=15, txt= 'Animalia', ln= 1)

pdf.set_font(family='Times', style='B', size=14)
pdf.cell(w=100, h=15, txt= 'Phylum: ')

pdf.set_font(family='Times',  size=14)
pdf.cell(w=100, h=15, txt= 'Chordata', ln= 1)

pdf.output(r"02 Generating PDFs\01 create_pdf\output.pdf")
print("PDF criado com sucesso!")

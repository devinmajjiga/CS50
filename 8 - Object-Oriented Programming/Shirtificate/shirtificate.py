import fpdf


class PDF(fpdf.FPDF):
    def header(self):
        self.set_text_color((255, 255, 255))
        self.set_draw_color((255, 255, 255))
        self.set_font("courier", style="B", size=50)
        self.cell(5)
        self.cell(180,20,"CS50 Shirtificate", border=1, align="C")\


name = input("What's your name? ")


pdf = PDF()
pdf.set_line_width(1)
pdf.set_page_background((0, 0, 0))
pdf.add_page()
pdf.image("shirtificate.png", w=190,h=190.962837838, x=10, y=70)
pdf.set_draw_color((255, 255, 255))
pdf.set_font("courier",style="B", size=24)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(65, 120)
pdf.multi_cell(80, 20, f"{name} took CS50", border=1, align="C")
pdf.output("shirtificate_test.pdf")
from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        #header line
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("helvetica", "B", 50)
        self._pdf.cell(0,60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

        #setting the shirt image
        self._pdf.image("shirtificate.png", w=self._pdf.epw)   #setting the width of image to the width of pdf

        #setting text on shirt
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=52,y=145, txt=f"{name} took CS50")

    def output(self, name):
        self._pdf.output(name)   #name of pdf output


def main():
    name = input("What's your name? ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
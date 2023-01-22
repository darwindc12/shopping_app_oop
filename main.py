import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})

class Article:

    def __init__(self, article_number):
        self.book_id = article_number
        self.name = df.loc[df['id'] == self.book_id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.book_id, 'price'].squeeze()

    def availability(self):
        check_stock =


class Receipt:

    def __init__(self, article):
        self.article = article

    def generate_pdf(self):

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Invoice nr. {self.article.book_id}", align='L', ln=1)

        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", align='L', ln=1)

        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", align='L', ln=1)

        pdf.output("receipt.pdf")


if __name__ == "__main__":
    print(df)
    article_id = input("Choose an article to buy: ")
    article = Article(article_id)
    if article.availability():
        pdf_receipt = Receipt(article_id)
        pdf_receipt.generate_pdf()
    else:
        print("No such article in the stock")




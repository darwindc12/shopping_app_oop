# Online Shop - Article Receipt Generator
This code reads a CSV file containing articles available in an online shop, creates an Article class that stores information about each article, such as the name and price. Then it creates a Receipt class that generates a PDF receipt for a given Article object.

## Libraries used
* pandas
* fpdf

## CSV file format
The CSV file should contain the following columns:

* id: article ID, unique identifier
* name: article name
* price: article price
* in stock: whether the article is available in the stock or not

## Classes
### Article
This class represents an article available in the online shop. It has the following methods:

* __init__(self, article_number): constructor that initializes an Article object with the given article number.
* availability(self): checks whether the article is available in the stock or not.

### Receipt
This class generates a PDF receipt for a given Article object. It has the following methods:

* __init__(self, article_object): constructor that initializes a Receipt object with the given Article object.
* generate_pdf(self): generates a PDF receipt for the given Article object.
## Running the code
When running the code, the user is prompted to choose an article by entering its ID. If the article is available in the stock, a PDF receipt is generated for it. If not, a message is printed informing the user that the article is not available.

import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("h3")
price = soup.find_all("p", class_="price_color")
for book in books:
    print(book.a["title"])

import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.append(["Book Title", "Price"])

for i in range(len(books)):
    sheet.append([books[i].a["title"], price[i].text])

workbook.save("books_data.xlsx")
print("Excel file saved!")
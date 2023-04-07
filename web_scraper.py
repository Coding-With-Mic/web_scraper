from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("http://quotes.toscrape.com")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# This is to grab all of the quotes
quotes = soup.findAll("span", attrs={"class": "text"})

# This is to grab all of the authors
authors = soup.findAll("small", attrs={"class": "author"})

# This opens a csv file, and then writes the data to the file
file = open("scraped_quotes.csv", "w")
writer = csv.writer(file)

writer.writerow(["QUOTES", "AUTHORS"])

# This prints out the quote and then the author neatly
for quote, author in zip(quotes, authors):
    print(quote.text + " - " + author.text)
    writer.writerow([quote.text, author.text])
file.close()

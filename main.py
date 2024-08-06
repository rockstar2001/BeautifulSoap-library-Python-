import requests
from bs4 import BeautifulSoup

# Fetch the web page content
url = "https://translate.google.com"#use your on url
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the desired data
title = soup.find("h1").text
paragraphs = [p.text for p in soup.find_all("p")]

# Store the extracted data
print("Title:", title)
print("Paragraphs:")
for paragraph in paragraphs:
    print("- ", paragraph)
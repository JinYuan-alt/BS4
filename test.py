import requests
from bs4 import BeautifulSoup
import csv

file_extensions = [".txt", ".pdf", ".csv", ".docx", ".xlsx", ".zip"]

page = requests.get("https://www.w3schools.com/python/module_requests.asp")

file_scrapping = requests.get("https://scholar.google.com/scholar?start=0&q=social+media&hl=en&as_sdt=0,5")
soup = BeautifulSoup(page.text,features="html.parser")

soup_files = BeautifulSoup(file_scrapping.text,features="html.parser")

print(file_scrapping) #response 200 = good to go

for files in soup_files.find_all('a'):
    if file_extensions[1] in files.get("href"):
        print(files.get("href"))

# for link in soup.find_all('a'):
#     print(link.get("href"))

# for file in soup.find_all('pdf'):
#     print(file.get("href"))

# Define the header and data
# header = ["links","text","metadata"]
# data = []
#
# # Open the CSV file for writing (w mode)
# with open('Storage/CSV_test.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(header)
#     writer.writerow(data)

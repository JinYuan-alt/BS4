import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.w3schools.com/python/module_requests.asp")

soup = BeautifulSoup(page.text,features="html.parser")

print(page) #response 200 = good to go

print(soup)
import requests 
from bs4 import BeautifulSoup


def create_link(type, code):

    link = f"http://next-door.com.ua/uk/{type}/view/{code}"
    return link

print(create_link("flats","SF-2-699-320"))

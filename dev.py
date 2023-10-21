import requests 
from bs4 import BeautifulSoup


def create_link(property_type, property_code):

    link = f"http://next-door.com.ua/uk/{property_type}/view/{property_code}"
    return link

print(create_link("flats","SF-2-699-320"))

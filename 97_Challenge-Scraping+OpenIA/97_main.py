import requests
import openai
import os
from bs4 import BeautifulSoup

url = input("Paste wiki URL > ")

html = requests.get(url)
soup = BeautifulSoup(html, "html.parser")

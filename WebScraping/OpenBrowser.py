# This module comes with python and it opens a webbrowser to a specific page
import webbrowser
import requests
from bs4 import BeautifulSoup

def OpenChrome():
    
    print("Opening Google!")

    # This should open a browser and go to google.com
    webbrowser.open('http://www.google.com')

def main():
    page = requests.get('https://store.steampowered.com/')

    soup = BeautifulSoup(page.text, 'html.parser')

    # OpenChrome()

    print(soup.find(id="topsellers_tier"))

if __name__ == "__main__":
    main()

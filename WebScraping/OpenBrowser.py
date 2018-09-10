# This module comes with python and it opens a webbrowser to a specific page
import webbrowser
import requests
from bs4 import BeautifulSoup

def OpenChrome():
    
    print("Opening Google!")

    # This should open a browser and go to google.com
    webbrowser.open('http://www.google.com')

def main():
    page = requests.get('https://www.macworld.co.uk/feature/mac/best-macbook-2018-3665084/')

    soup = BeautifulSoup(page.text, 'html.parser')

if __name__ == "__main__":
    main()

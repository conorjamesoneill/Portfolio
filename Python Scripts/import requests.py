#Web scraper, prints out link for Github profile picture
import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input GitHub user: ')
url = 'https://github.com/'+github_user #will find the user page of whatever username the user inputs
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_image = soup.find('img')[scr]#scrapes page HTML code to find the specific img tag we want, also getting the src attribute
print(profile_image)

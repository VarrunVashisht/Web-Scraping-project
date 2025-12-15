import requests                     # downloads web pages
from bs4 import BeautifulSoup       # helps with web scraping

url = 'http://www.ibm.com'
data =requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

# find all Links in a page <a href="https://google.com">Google</a>
for link in soup.find_all('a'):
    print(link.get('href'))

# find all Images in a page <img src="logo.png">
for img in soup.find_all('img'):
    print(img.get('src'))


# Scraping Data from an HTML Table
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data = requests.get(URL).text
soup = BeautifulSoup(data, "html.parser")
table = soup.find('table')

for row in table.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) >= 4:
        color_name = cols[2].getText()
        color_code = cols[3].getText()
        print(f"{color_name} ---> {color_code}")








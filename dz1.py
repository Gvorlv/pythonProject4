from bs4 import BeautifulSoup
import requests
import lxml
file = open('/Users/vladimirorlovskij/Downloads/index.html', encoding='utf-8')
soup = BeautifulSoup(file, 'lxml')
print(soup)

from bs4 import BeautifulSoup
import requests
r = requests.get('https://www.defense.gov/Resources/Military-Departments/DOD-Websites/')
soup = BeautifulSoup(r.text, 'lxml')
div_class = soup.find_all('div', class_="DGOVListLinkAlt")
file = open('ListUrls.txt', 'w')
for links in div_class:
	file.write(links.a['href'])
print('[+] Finished [+]')
import requests
from bs4 import BeautifulSoup

response = requests.get('https://jjangsungwon.github.io/')
response.encoding = 'utf-8'
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
l = []
for tag in soup.select('p'):
    l.append(tag.text.strip())
print(l)
print(soup.prettify())
print(soup.get_text())
'''
단순한 문자열 객체 반환
f = open('test.html', 'w')
f.write(html)
f.close()

spliteHTML = html.split(' ')
print(spliteHTML)
print(spliteHTML.count('장성원'))
'''
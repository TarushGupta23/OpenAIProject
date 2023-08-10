import requests
from bs4 import BeautifulSoup
url = "http://127.0.0.1:5555/Old/home.html"

r = requests.get(url)
content_HTML = r.content
soup = BeautifulSoup(content_HTML, 'html.parser')

outBox = soup.select(".output span")[0]
inBox = soup.select(".input")[0]
# print(outBox.string)
print(inBox.string)
# inBox.string.replace_with("This is changed by python")
print(inBox.string)
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

rt = bsObj.find_all(id="text")
print(rt[0].get_text())



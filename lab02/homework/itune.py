from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url ="https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)

data = conn.read()

html_content = data.decode("utf-8")

# f = open("itune.html", "wb")
# f.write(data)
# f.close()
soup = BeautifulSoup(html_content, "html.parser")

div = soup.find('section', 'section chart-grid')
# print(div.prettify())

abc = []
ul = div.ul
li_list = ul.find_all('li')
for li in li_list:
    li_dict = {}
    a = li.h3.a
    li_dict["song"] = a.string
    a = li.h4.a
    li_dict["artist"] = a.string
    abc.append(li_dict)
    options = {
        'default_search': 'ytsearch',
        'max_download': 1,
    }
    dl = YoutubeDL(options)
    dl.download(['{} {}'.format(li_dict["song"],li_dict["artist"])])
pyexcel.save_as(records=abc, dest_file_name="iTunes top songs.xlsx")

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

# 1 download web
url = "http://dantri.com.vn"

# 1.1 create connection
conn = urlopen(url)
# 1.2 read
data = conn.read()
# 1.3 decode
html_content = data.decode("utf-8")
# print(html_content)

# save html to file
# f = open("dantri.html", "wb")
# f.write(data)
# f.close()

# 2 extact ROI (region of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content, "html.parser")
# find by class
ul = soup.find('ul', 'ul1 ulnew')
# print(ul.prettify())

# 3 extract data
abc = []
li_list = ul.find_all('li')
for li in li_list:
    li = li_list[0]
    # li_dict = {}
    a = li.h4.a
    print(a.string)
    print(url + a["href"])
    print("*" * 30)
#     li_dict["title"] = a.string
#     li_dict["link"] = url + a["href"]
#     abc.append(li_dict)
# pyexcel.save_as(records=abc, dest_file_name="dantri.xlsx")




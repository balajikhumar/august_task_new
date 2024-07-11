# Write a Python program that uses web scraping to extract data from a website
# and save it to a file. You can use any web scraping library of your choice ex.
# Beautiful Soup.

import requests
from bs4 import BeautifulSoup
import re
import json


d = requests.get("https://www.augustinfotech.com/")

# print(d)

html_data = d.text
# print(html_data)

with open("page.html", "w", encoding="utf-8") as f:
    f.write(html_data)

ss = BeautifulSoup(html_data, "html.parser")

# North America:
# +1.647.477.8350
# Asia:
# +91.898.000.8230
# Careers:
# +91.968.756.0698

# print(dir(ss))
# print(ss.findAll())
page_data = {
    "phone_numbers" : []
}
for i in ss.findAll("a"):
    # print(i.get_text())
    tmp = i.get_text().strip()
    links = i.get("href")
    # print(links)
    phone_num = r"\+\d{2}\.\d{3}\.\d{3}\.\d{4}|\+\d{1}\.\d{3}\.\d{3}\.\d{4}"
    data = re.findall(phone_num, tmp)
    # break
    if data:
        page_data["phone_numbers"].extend(data)
        # print("Numbers : ",data)
    else:
        if tmp.replace(" ","").isalpha() and links != "#":
            page_data[tmp] = links
    
print(page_data)
with open("data.json", "w") as f:
    json.dump(page_data, f)

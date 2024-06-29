import pandas as pd
from bs4 import BeautifulSoup
import os

btechfile_path=os.listdir("btech/found")
bpharmafile_path=os.listdir("bpharma/found")
html_files=btechfile_path + bpharmafile_path

print("Total html files in both folders is ",len(html_files))

for i in html_files:
    if i=="20011614003_1800265728.html":
        print("match found this exists")
    try:
        file=open(f"btech/found/{i}","r")
    except:
        file=open(f"bpharma/found/{i}","r")
    data=file.read()
    # print(data)
    soup=BeautifulSoup(data,features="html.parser")
    # print(soup.findAll('td',attr={'class':'border1'}))
    # for j in soup.find_all('td',attr={'class':'border1'}):
    #     print("j is ",j)
    data=soup.find('html')
    data12=data.find('body')
    # print(data)
    data1=data12.find_all('div',class_="cont_outer print")
    print(data1)
    for row in data1:
        try:
            data=row.find("table",attr={'class':'cont_DIV_UN'})
            data=data.find('tbody')
            data=data.find('tr')
            data=data.find('td')
            data=data.find('div',attr={'div':'mid_PART_UN'})
        except:
            print("pass")
            pass
    # data=data.find('table')
    # data=data.find('tbody')
    # data=data.find('tr')
    # data=data.find('td')
    # data=data.find('table')
    # data=data.find('tbody')
    # data=data.find('tr')
    # data=data.find_all('td',attr={'class':'border1'})
    print(data)
    break


import pandas as pd
from bs4 import BeautifulSoup
import os

btechfile_path=os.listdir("btech/found")
bpharmafile_path=os.listdir("bpharma/found")
html_files=btechfile_path + bpharmafile_path

print("Total html files in both folders is ",len(html_files))

for i in html_files:
    try:
        file=open(f"btech/found/{i}","r")
    except:
        file=open(f"bpharma/found/{i}","r")
    data=file.read()
    soup=BeautifulSoup(data)
    data=soup.find_all("tr")
    print(data)
    break


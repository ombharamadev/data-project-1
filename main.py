import pandas as pd
from bs4 import BeautifulSoup
import os

btechfile_path=os.listdir("project1/btech/found")
bpharmafile_path=os.listdir("project1/btech/found/bpharma/found")
print(len(btechfile_path)+len(bpharmafile_path))
# data=BeautifulSoup.find()

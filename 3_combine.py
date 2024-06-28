
import os
import pandas as pd
from bs4 import BeautifulSoup

def scrap(filename):
    file_path = filename

    file_read = open(file_path,"r")

    data_file = file_read.read()

    ##ful xpath  /html/body/div[2]/table/tbody/tr[1]/td[2]/div[1]/table/tbody/tr[4]/td/table[4]/tbody/tr[1]/td[2]

    soup = BeautifulSoup(data_file)

    div_a = soup.find("div",{"class":"cont_outer"})

    table_a = div_a.find("table",{"class":"cont_DIV_UN"})

    div_b = table_a.find("div",{"id":"midd_part_UN"})

    table_b = div_b.find("table")

    td_a = table_b.find_all("td",{"class":"border1"})

    cgpa = td_a[-4:-3]

    scgpa = td_a[-5:-4]
    scgpa = scgpa[0].text
    scgpa = scgpa.replace("\xa0 ","").strip()


    cgpa = cgpa[0].text
    cgpa = cgpa.replace("CGPA","")
    cgpa = cgpa.replace("\xa0 ","").strip()
    
    
    
    
    new_js = {
        "file_name":str(filename),
        "cgpa":str(cgpa),
        "scgpa":str(scgpa)
    }
    return new_js


folder_path = "sample"

#list all the file in that folder
files = os.listdir(folder_path)

arr_js= []
for api in files:
    file_path = "sample/"+str(api)+""

    data_js = scrap(file_path)
    #print(data_js)
    arr_js.append(data_js)

#nwo we will save the json data

df = pd.DataFrame(arr_js)

df.to_csv("out.csv")
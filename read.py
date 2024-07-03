#importing packages
import pandas as pd
from bs4 import BeautifulSoup
import os

#reading the files present in directory
btechfile_path=os.listdir("btech/found")
bpharmafile_path=os.listdir("bpharma/found")
html_files=bpharmafile_path+btechfile_path

#counting total files in both directory
print("Total html files in both folders is ",len(html_files))

#creating variables to store data
cgpa_data=[]
sgpa_data=[]
files_name=[]
files_lack_cgpa=[]

#testing array containing file name for basic code creation
html0=["20011715005_1800265223.html","15619_1800265830.html","20011715004_1800265851.html","20011715004_1800265710.html"]

#starting loop to traverse and read all the html file 1 by 1
for i in html_files:
    files_name.append(i)
    print("file name is ->",i)

    #using try and except as the files are in two different directories
    try:
        file=open(f"bpharma/found/{i}","r")
    except:
        file=open(f"btech/found/{i}","r")
        
    #reading the data from the .html file    
    content=file.read()

    #code for reading the cgpa &sgpa from the html files
    soup=BeautifulSoup(content,'lxml')
    if ("CGPA" in content)or("SGPA" in content):
        data=soup.find_all('div',class_="cont_outer print")
        for dat in data:
            data_0=dat.find_all("table",class_='cont_DIV_UN')
            data1=data_0[0].find_all('tr')
            auto_eval=-1
            for dat1 in data1:
                auto_eval=auto_eval+1
                if ("CGPA" in dat1.text)or("SGPA" in dat1.text):
                    auto_eva=auto_eval
            if "CGPA" in data1[auto_eva].text:
                cgpa_data.append(data1[auto_eva].text.split(" ")[1])
                sgpa_data.append(data1[auto_eva-1].text.split(" ")[1])
            else:
                sgpa_data.append(data1[auto_eva].text.split(" ")[1])
                cgpa_data.append(" ")
                
    elif ("CGPA" not in content)or("SGPA" not in content):
        files_lack_cgpa.append(i)
        cgpa_data.append(0)
        sgpa_data.append(0)

#counting the total number of files which donot have cgpa or sgpa in it 
print("files with not cgpa or sgpa are",len(files_lack_cgpa))

#array containing filename,cgpa and sgpa
array=[files_name,sgpa_data,cgpa_data]

#code for writing data in csv file 
#transpose so as to interchange rows and columns
df=pd.DataFrame(array).transpose()

print(df)
#saving the dataframe to csv file
df.to_csv("result.csv")
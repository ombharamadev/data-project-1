import pandas as pd
from bs4 import BeautifulSoup
import os

# Directory paths
btechfile_path = os.listdir("btech/found")
bpharmafile_path = os.listdir("bpharma/found")
html_files = bpharmafile_path + btechfile_path

print("Total html files in both folders is", len(html_files))

# Data storage lists
cgpa_data = []
sgpa_data = []
files_name = []
files_lack_cgpa = []

# Testing array containing file names for basic code creation
html0 = ["20011715005_1800265223.html", "15619_1800265830.html", "20011715004_1800265851.html", "20011715004_1800265710.html"]

for i in html_files:
    files_name.append(i)
    print("file name is ->", i)

    # Using try and except as the files are in two different directories
    try:
        file_path = f"bpharma/found/{i}"
        with open(file_path, "r") as file:
            content = file.read()
    except FileNotFoundError:
        file_path = f"btech/found/{i}"
        with open(file_path, "r") as file:
            content = file.read()
    
    soup = BeautifulSoup(content, 'lxml')

    if ("CGPA" in content) or ("SGPA" in content):
        data = soup.find_all('div', class_="cont_outer print")
        for dat in data:
            data_0 = dat.find_all("table", class_='cont_DIV_UN')
            data1 = data_0[0].find_all('tr')
            auto_eval = -1
            for dat1 in data1:
                auto_eval += 1
                if ("CGPA" in dat1.text) or ("SGPA" in dat1.text):
                    auto_eva = auto_eval
            if "CGPA" in data1[auto_eva].text:
                cgpa_data.append(data1[auto_eva].text.split(" ")[1])
                sgpa_data.append(data1[auto_eva-1].text.split(" ")[1])
            else:
                sgpa_data.append(data1[auto_eva].text.split(" ")[1])
                cgpa_data.append(" ")
    else:
        files_lack_cgpa.append(i)
        cgpa_data.append(0)
        sgpa_data.append(0)

# Counting the total number of files which do not have CGPA or SGPA in it 
print("Files without CGPA or SGPA:", len(files_lack_cgpa))

# Print lengths of the lists to debug
print(f"Length of files_name: {len(files_name)}")
print(f"Length of sgpa_data: {len(sgpa_data)}")
print(f"Length of cgpa_data: {len(cgpa_data)}")

# Data for the CSV
data = {
    "filename": files_name,
    "sgpa": sgpa_data,
    "cgpa": cgpa_data
} 


# Create DataFrame and save to CSV with headers
df = pd.DataFrame(data)
print(df)
df.to_csv("data.csv", index=False)

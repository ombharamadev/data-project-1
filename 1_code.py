import os
import pandas as pd
from bs4 import BeautifulSoup

def scrap(filename):
    with open(filename, "r", encoding='utf-8') as file_read:
        data_file = file_read.read()

    soup = BeautifulSoup(data_file, 'html.parser')

    div_a = soup.find("div", {"class": "cont_outer"})
    if not div_a:
        return None

    table_a = div_a.find("table", {"class": "cont_DIV_UN"})
    if not table_a:
        return None

    div_b = table_a.find("div", {"id": "midd_part_UN"})
    if not div_b:
        return None

    table_b = div_b.find("table")
    if not table_b:
        return None

    td_a = table_b.find_all("td", {"class": "border1"})
    if not td_a or len(td_a) < 5:
        return None

    scgpa = td_a[-5].text.replace("\xa0", "").strip()
    cgpa = td_a[-4].text.replace("CGPA", "").replace("\xa0", "").strip()

    new_js = {
        "file_name": str(filename),
        "cgpa": str(cgpa),
        "scgpa": str(scgpa)
    }
    return new_js

def scrape_directory(folder_path):
    files = []
    for root, dirs, file_names in os.walk(folder_path):
        for file_name in file_names:
            files.append(os.path.join(root, file_name))

    arr_js = []

    for file_path in files:
        data_js = scrap(file_path)
        if data_js:
            arr_js.append(data_js)

    return arr_js

# Define the directories to scrape
btech_folder = "btech"
bpharma_folder = "bpharma"

# Scrape both directories
btech_data = scrape_directory(btech_folder)
bpharma_data = scrape_directory(bpharma_folder)

# Combine data from both directories
all_data = btech_data + bpharma_data

# Save the extracted data into a CSV file
df = pd.DataFrame(all_data)
df.to_csv("out.csv", index=False)

print("Scraping completed. Data saved to out.csv")

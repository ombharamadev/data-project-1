import os
import pandas as pd
from bs4 import BeautifulSoup

def scrape_data_from_html_folder(folder_path):
    data = {"file_name": [], "SGPA": [], "CGPA": []}
    i=0
    try:
        # Iterate through each file in the folder
        for filename in os.listdir(folder_path):
            i+=1
            print(i)
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and filename.endswith('.html'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    # Read the entire content of the HTML file
                    html_content = file.read()
                    # Parse the HTML content
                    soup = BeautifulSoup(html_content, 'html.parser')
                    sgpa_found = False
                    cgpa_found = False
                    for row in soup.find_all('tr'):
                        cells = row.find_all('td')
                        if len(cells) > 1:
                            label = cells[0].text.strip()
                            value = cells[1].text.strip()
                            a = label.split()
                            if a:
                                if "SGPA" == a[0]:
                                    data["SGPA"].append(value)
                                    data["file_name"].append(filename)
                                    sgpa_found = True
                                elif 'CGPA' == a[0]:
                                    data["CGPA"].append(value)
                                    if not sgpa_found:
                                        data["file_name"].append(filename)
                                    cgpa_found = True
                    # If CGPA was found but SGPA wasn't, append an empty SGPA value
                    if cgpa_found and not sgpa_found:
                        data["SGPA"].append('N/A')
                    if sgpa_found and not cgpa_found:
                        data["CGPA"].append('N/A')
        # Convert dictionary to pandas DataFrame
        try:
            df = pd.DataFrame(data)
        except Exception as e:
            print(f"Error creating DataFrame: {str(e)}")
            return None
        
        # Save DataFrame to a CSV file
        csv_file_path = os.path.join(folder_path, 'bpharma_scraped_data.csv')
        df.to_csv(csv_file_path, index=False)
        
        print(f"CSV file saved to: {csv_file_path}")  # Print confirmation message
        
        return df
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None
    
folder_path = 'C:/python practice/day3/btech/found'
extracted_data = scrape_data_from_html_folder(folder_path)
if extracted_data is not None:
    print(extracted_data)
else:
    print("Extraction failed. Check error messages.")

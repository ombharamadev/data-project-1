from bs4 import BeautifulSoup

file_path = "sample/21010305041_1800265903.html"

read_file = open(file_path,"r")
file_data = read_file.read()


soup = BeautifulSoup(file_data)
div_find = soup.find("div",{"class":"cont_outer"})

table = div_find.find("table",{"class":"cont_DIV_UN"})

div_2_find = table.find("div",{"id":"midd_part_UN"})

table_2_all = div_2_find.find("table")

td_data = table_2_all.find_all("td",{"class":"border1 NB_left"})
print(td_data[-3:-2][0].text)
print(td_data[-2:-1][0].text)

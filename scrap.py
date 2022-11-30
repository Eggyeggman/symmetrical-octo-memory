from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
bright_star_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(bright_star_url)
soup = bs(page.text,'html.parser')
star_table=soup.find('table')
templist=[]
table_row = star_table.find_all('tr')
for tr in table_row:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td ]
    templist.append(row)
Star_names=[]
Distence = []
Mass = []
Radius = []
Lum = []
for i in range(1,len(templist)):
    Star_names.append(templist[i][1])
    Distence.append(templist[i][3])
    Mass.append(templist[i][5])
    Radius.append(templist[i][6])
    Lum.append(templist[i][7])
df2 = pd.DataFrame(list(zip(Star_names,Distence,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
df2.to_csv('bright_star_url.csv')
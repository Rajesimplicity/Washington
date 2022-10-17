import requests
import bs4
import pandas as pd

url = 'https://ccfs.sos.wa.gov/#/BusinessSearch/'
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text,'lxml')

name = soup.find('div', attrs={'class':'Entity Name'})
ubi = soup.find('div', attrs={'class':'UBI#'})
bizz_type = soup.find('div', attrs={'class':'Business Type'})
address = soup.find('div', attrs={'class':'Principal Office Address'})
agent = soup.find('div', attrs={'class':'Registered Agent Name'})
stat_us = soup.find('div', attrs={'class':'Status'})

names = []
ubi = []
bizz_type = []
address = []
agent = []
stat_us = []

for i in soup.findAll('soup',href=True, attrs={'class':'ng-scope'}):
    span = i.find('span')
names.append(span.string)
ubi.append(span.string)
bizz_type.append(span.string)
address.append(span.string)
agent.append(span.string)
stat_us.append(span.string)

print(names)
print(ubi)
print(bizz_type)
print(address)
print(agent)
print(stat_us)

df = pd.DataFrame({'Entity Name':names,'UBI#':ubi,'Business Type':bizz_type, 'Principal Office Address':address,'Registered Agent Name':agent, 'Status':stat_us})

df.index = ['Business Name', 'UBI#', 'Business Type', 'Principal Office Address', 'Registered Agent Name', 'Status']

df.to_csv('Result.csv')

import requests, bs4
import pandas as pd
import os

from sympy import false

url = "https://sparkkorea.com/테스트/"
response = requests.get(url).text.encode('utf-8')
response = bs4.BeautifulSoup(response, 'html.parser')

target = response.find('table', {'id':'test_table', 'class':'type07'})

thead = target.find_all('th')

theadList = []

theadLen = len(thead)
for i in range(0,theadLen):
    thead = target.find_all('th')[i].text
    theadList.append(thead)


tbody = target.find('tbody')

trData = tbody.find_all('tr')

tdData = trData[0].find_all('td')

rowList = []
columnList = []

trDataLen = len(trData)
for i in range(0,trDataLen):
    tdData = trData[i].find_all('td')
    
    tdDataLen = len(tdData)
    for j in range(0,tdDataLen):
        element = tdData[j].text
        columnList.append(element)

    rowList.append(columnList)
    columnList = []
    
rowList = pd.DataFrame(rowList,columns=theadList)

rowList.to_excel(excel_writer='test.xlsx')

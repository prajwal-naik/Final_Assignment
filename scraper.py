# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:09:28 2019

@author: Prajwal
"""
import csv
import os 
import requests
from bs4 import BeautifulSoup
url='https://karki23.github.io/Weather-Data/assignment.html'
sauce=requests.get(url)
srccode=BeautifulSoup(sauce.content, "html.parser")
all_cities=srccode.find_all('a')
os.mkdir("datasets")
for i in all_cities:
    s=i.get('href')[0:len(i)-5:]
    url1='https://karki23.github.io/Weather-Data/'+i.get('href')
    sauce1=requests.get(url1)                                                       #this code prints PROPERLY
    srccode1=BeautifulSoup(sauce1.content, "html.parser")
    rows=srccode1.find_all('tr')
    rows.pop(0) 
    file_name="datasets\\"+s+"csv"
    f=open(file_name, "w", newline="")
    headings=srccode1.find_all('th')
    headings_new=[i.text for i in headings]
    writer=csv.writer(f)
    writer.writerow(headings_new)
    for i in rows:    
        columns=i.find_all('td')
        column_new=[j.text for j in columns]
        writer.writerow(column_new)
    f.close()
    


     
    
    
      
    
    
    

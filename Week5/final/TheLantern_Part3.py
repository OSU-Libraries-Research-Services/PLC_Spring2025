# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 17:17:08 2025

@author: murphy.465

ACTIVITY: THE LANTERN - PART 3
Use regular expressions to clean the publication_text column in the 
lantern_text.csv file created in Week4

"""

#1. Import libraries
import requests 
import csv
from bs4 import BeautifulSoup
import re


# 2. Create function to write search results to csv
def writeto_csv(data, filename, columns):
    with open(filename, 'w+', newline='', encoding="UTF-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer = csv.writer(file)
        for element in data:
            writer.writerows([element])

# 3. Define headers for final dataset
columns=['result_number','ltn','title','section_type','document_date']

#4. Create empty dataset to store each row of data for csv file
dataset = []

#5. Define url. Adjust search terms, search dates as needed. 
#The Lantern defaults to 20 search results per page. Split the URL to 
#as Python to incrementally return search results in step 6 below.
# url = 'https://osupublicationarchives.osu.edu/?a=q&hs=1&r=1&results=1&txq=homecoming+AND+parade&dafdq=01&dafmq=01&dafyq=1970&datdq=31&datmq=12&datyq=1971&puq=LTN&txf=txIN&ssnip=txt&e=-------en-20--1--txt-txIN-------&f=XML'
url_part1 = 'https://osupublicationarchives.osu.edu/?a=q&hs=1&r='
url_part2 = '&o=100&results=1&txq=homecoming+parade&dafdq=01&dafmq=01&dafyq=1970&datdq=31&datmq=12&datyq=1971&puq=LTN&txf=txIN&ssnip=txt&e=01-01-1970-31-12-1971--en-20-LTN-1--txt-txIN-------&f=XML' #added &o=100 to start of string to return 100 results per page

#6. Create a loop to search through each page of the search results. 
#range(start, stop, step) is used to ask Python to increment i by 20 for each loop.
#i.e. 1, 21, 41, 61, 81, etc.... i is inserted in the url to request the 
#content for the next page.
for i in range(1,100,100):    
    response=requests.get(url_part1+str(i)+url_part2).content     
    #Parse the content with Beautiful Soup
    soup = BeautifulSoup(response, 'xml')    
    logical_section = soup.find_all("LogicalSection")
    for each_section in logical_section:
        result_number = each_section.SearchResultNumber.string
        ltn = each_section.find("LogicalSectionID").string
        title = each_section.find("LogicalSectionTitle").string
        section_type = each_section.find("LogicalSectionType").string
        document_date = each_section.find("DocumentDate").string
        dataset.append([result_number,ltn,title,section_type,document_date]) #add a list of variable for each section to the dataset
        
writeto_csv(dataset,'lantern_entry_numbers.csv',columns)     #uses the function defined in #2 to create the final .csv file with each row  

#7. Now use the ltn for each section to gather the publication text
columns2=['unique_id','article_title','article_type','publication_date','publication_text']
dataset2=[]

#sample_url='https://osupublicationarchives.osu.edu/?a=d&d=LTN19781023-01.2.24&f=XML'
base_url='https://osupublicationarchives.osu.edu/?a=d&d='

for each_list in dataset:
    unique_id=each_list[1]
    article_title=each_list[2]
    article_type=each_list[3]
    publication_date=each_list[4]
    url=base_url+unique_id+'&f=XML'
    xml=requests.get(url).content
    soup=BeautifulSoup(xml,'xml')
    text=soup.find("LogicalSectionTextHTML").text
    new_text=re.sub(r'\<p dir=\"auto\"\>',"",text)
    publication_text=re.sub(r'\<\/p>',"",new_text)


    
    dataset2.append([unique_id,article_title,article_type,publication_date,publication_text])

writeto_csv(dataset2,'lantern_text.csv',columns2)
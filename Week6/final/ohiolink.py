# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 11:03:16 2025

@author: murphy.465

Search the OhioLINK ETD for dissertations submitted by English PhD students
between 2015 and 2024. Find the dissertation title, author, degree, degree_year,
advisor(s), committee members, and subjects for each student.

https://etd.ohiolink.edu/acprod/odb_etd/r/etd/search/search-results?p1001_advanced=1&clear=0,1001


"""

from bs4 import BeautifulSoup as bs
import re
import pandas as pd

##### STORE SEARCH RESULTS
results=pd.DataFrame(columns=['title','author','degree','degre_year','advisors','committee_members','subjects'])

###### START BY LOOKING AT ONE FILE ONLY!!!!!
page_start=1
page_end=2
filepath_root='English'
filepath_suffix=".html"
# filepath='English1.html'
for page in range(page_start,page_end+1):
    filepath=filepath_root+str(page)+filepath_suffix
    print(filepath)
    contents=open(filepath, encoding='utf-8').read()
    soup=bs(contents, 'html.parser')
    count=1
    etd_contents=soup.find_all(attrs={"class":'t-SearchResults-content'})
    
    ##### FIND ELEMENTS
    for each_record in etd_contents:
        author=each_record.span.text
        title=each_record.a.text
        year=each_record.p.text
        degree=re.search(r"(.*), The Ohio State University", year)[0].replace(", The Ohio State University","").strip()
        try:
            degree_year=re.search(r"[0-9]{4}", year)[0]
        except:
            degree_year='not found'
        misc_records=each_record.find_all("span",attrs={"class":'t-SearchResults-misc'})
        committee=misc_records[0].text
        advisors=[]
        advisors_list=re.findall(r";?\w* \w* \w*? ?\(Advisor\)", committee)
        if advisors_list != None:
            for each_advisor in advisors_list:
                advisors.append(each_advisor.replace(" (Advisor)","").replace(";","").strip())
        advisors=";".join(advisors).rstrip(';')
        committee_members=committee.replace("Committee: ","").replace("(Advisor)","").replace("(Committee Member)","").replace("(Committee Chair)","").replace("(Committee Co-Chair)","")
        subjects=misc_records[1].text.replace("Subjects: ","")
    
    ##### ADD ELEMENTS TO DICTIONARY, ONE ROW AT A TIME; THEN CREATE DICTIONARY FOR
    ##### EACH ROW AND CONCATENATE EACH ROW TO RESULTS
        row={
            'title':title,
            'author':author,
            'degree':degree,
            'degre_year':degree_year,
            'advisors': advisors,
            'committee_members': committee_members,
            'subjects':subjects
            }
        
        each_row=pd.DataFrame(row, index=[0])
        results=pd.concat([each_row, results], axis=0, ignore_index=True)
        
results.to_csv('english_advisors.csv')
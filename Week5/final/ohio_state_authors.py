# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 19:39:49 2025

@author: murphy.465

Normalize Ohio State University addresses
"""

#1. Import libraries needed for project
import pandas as pd
import re

#2. Read in pubmed_author_affiliations.csv
df=pd.read_csv('pubmed_author_affiliations.csv')
df=df.dropna(subset='affiliation')

#3. Create a DataFrame to store results
results=pd.DataFrame(columns=['affiliation','normalized_affiliation'])

#4. Take a close look at the data in the affiliation column. 

##### ALL THE DIFFERENCE WAYS TO SAY THE OHIO STATE UNIVERSITY IN AN ADDRESS!!!! #####
osu_variations=["ohio state","oardc","ohio sate","the ohio, state university","43210",
"james comprehensive cancer center","james cancer hospital","osuccc",
"osu comprehensive cancer center","wexner medical center","osumc.edu",
"davis heart","151 w. woodruff","arts and sciences, columbus",
"biological chemistry and pharmacology, columbus","biomedical sciences graduate program",
"brain and spinal core repair","center for affordable nanoengineering of polymer biomedical devices",
"center for biostatistics, columbus","center for brain and spinal cord repair",
"center for retrovirus research","center for rna biology","clara d. bloomfield",
"college of arts and sciences, osu","college of medicine, columbus",
"college of pharmacy, columbus","college of pharmacy, osu","college of public health, columbus",
"college of veterinary medicine, osu","com, osu","cunz hall",
"department of bioinformatics, columbus","family and community medicine, columbus",
"helene fuld","human ecology, columbus","infectious diseases institute",
"internal medicine, columbus","medical scientist training program",
"microbial interface biology","molecular genetics, columbus",
"osu school of health and rehabilitation sciences","osu, college of medicine",
"osu, college of public health","osu, cph","osu global one health",
"pelotonia institute for immuno-oncology","perinatal psychoneuroimmunology among black american women",
"stefanie spielman","william g lowrie","wright center of innovation"]

#4. Iterate through each row of df. Use regular expressions to identify Ohio State addresses
for idx, row in df.iloc[0:200].iterrows():
    affiliation=str(row.affiliation)
    osu_match=re.match(r"The Ohio State University",affiliation) 
    if osu_match:
        normalized_affiliation=osu_match.group()
        print(f" MATCH {osu_match.group()}: {affiliation}")
    else:
        normalized_affiliation=""
        print("no match")
    osu_search=re.search(r"The Ohio State University",affiliation) 
    osu_search=re.search(r"The Ohio State University",affiliation) 
    if osu_search:
        normalized_affiliation=osu_search.group()
        print(osu_search.group())
    else:
        normalized_affiliation=""
        print(f"No match: affiliation = {affiliation}")
    
    


# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:10:25 2025

@author: murphy.465

ACTIVITY: MEET THE ANIMALS - PART 2

Meet the Animals at the Smithsonian National Zoo & Conservation Biology Institute.

Use pandas to read the i_met_the_animals.csv file into a dataframe and create a list of animal common_names.
Then iterate through the list of common_names to gather the following elements from the webpages for each animal.

Common name
Scientific name
Taxonomic information
    Class
    Order
    Family
    Genus and species
Physical description
Size
Native habitat
Conservation status
Fun facts

"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

# 1. Read in i_met_the_animals.csv and create a list of animals to search
df = pd.read_csv('i_met_the_animals.csv')
animals = df.common_name.tolist()

# 2. Create a DataFrame for the search results
results = pd.DataFrame(columns=['common_name', 'scientific_name', 'class',
                                'order', 'family', 'genus_species', 'physical_description',
                                'size', 'native_habitat', 'status', 'fun_facts'])

# 3. Identify the base url
base_url = 'https://nationalzoo.si.edu/animals/'

# 4. Iterate through the list of animals. Construct a url for each animal's
# website. Then request and parse the HTML for each website.
count = 1
for animal in animals:
    print(f"Starting #{count} {animal}")
    animal_name = animal.strip().lower().replace(' ', '-')
    url = base_url+animal_name
    # print(url)
    response = requests.get(url).text
    soup = BeautifulSoup(response, "html.parser")
    scientific_name = soup.h3.text
    print(f" {count}. {scientific_name}")
    find_taxonomy = soup.find_all("div", class_="text-lg mb-2")
    print(find_taxonomy)
    

    span_tags = []
    try:
        for each_div_tag in find_taxonomy:
    
            find_span_tags = each_div_tag.find_all('span')
            for each_span_tag in find_span_tags:
                span_tags.append(each_span_tag.text)
        animal_class=span_tags[1]
        order=span_tags[3]
        family=span_tags[5]
        genus_species=span_tags[7]
        # print(f"Class={animal_class}")
        # print(f"Order={order}")
        # print(f"Family={family}")
        # print(f"genus_species={genus_species}")
    except:
        animal_class=''
        order=''
        family=''
        genus_species=''
    h2_tags=soup.find_all('h2', class_="block-title border-animals")
    for h2 in h2_tags:
        entry = h2.find_next_sibling()
        if h2.text =="Physical Description" and entry and entry.name == 'div':
            # print("\nPHYSICAL DESCRIPTION")
            # print(entry.text)
            physical_description=entry.text
        if h2.text =="Size" and entry and entry.name == 'div':
            # print("\nSIZE:")
            # print(entry.text)
            size=entry.text
        if h2.text =="Native Habitat" and entry and entry.name == 'div':
            # print("\nNATIVE HABITAT:")
            # print(entry.text)
            habitat=entry.text
        if h2.text =="Fun Facts" and entry and entry.name == 'ol':
            facts=[]
            # print('FUN FACTS!!!')
            lines=entry.find_all('li')
            fact_count=1
            for each_line in lines:
                facts.append('Fact #'+str(fact_count)+': '+each_line.text)
                fact_count += 1
            fun_facts=' | '.join(facts)
    try:
        status=soup.find('ul', id="iucn-list").attrs
        conservation_status=status['data-designation']
        print(conservation_status)
    except:
        conservation_status=''    
        
#5. Create a dictionary to store one row of results
    row={
        'common_name':animal.strip(),
        'scientific_name':scientific_name,
        'class':animal_class,
        'order':order,
        'family':family,
        'genus_species':genus_species,
        'physical_description':physical_description.strip(),
        'size':size.strip(),
        'native_habitat':habitat.strip(),
        'status':conservation_status.strip(),
        'fun_facts': fun_facts }

#6. Create a DataFrame to store the one row of results    
    each_row=pd.DataFrame(row, index=[0])
    
#7. Concatenate each_row of results to the DataFrame created in step #2
    results=pd.concat([each_row,results], axis=0, ignore_index=True)
    
    count += 1
 
#8. Create a .csv file
results.to_csv('national_zoo_animals.csv')

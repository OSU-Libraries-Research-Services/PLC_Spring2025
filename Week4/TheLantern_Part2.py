# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 17:29:58 2025

@author: murphy.465

ACTIVITY 3: THE LANTERN - PART 2

Using Spyder and our XML search for homecoming parade in The Lantern, gather the following elements:

unique_id
article_title
article_type
Then use the unique_id to gather the following elements for each publication:

publication_date
publication_text
Export the elements to a .csv file.

APPROACH

-We use requests to ask Python to get a response from a webpage. Python returns
a response object. We use .content with requests.get(url) to return the 
response content in bytes.   

response=requests.get(url).content

-We import csv to write a function that will create a .csv file that stores our results
-We import BeautifulSoup to parse the xml content returned by requests.get(url).content

 """
#1. Import libraries



# 2. Create function to write search results to csv



# 3. Define headers for final dataset


#4. Create empty dataset to store each row of data for csv file


#5. Define url. Adjust search terms, search dates as needed. 
#The Lantern defaults to 20 search results per page. Split the URL to 
#as Python to incrementally return search results in step 6 below.
# url = 'https://osupublicationarchives.osu.edu/?a=q&hs=1&r=1&results=1&txq=homecoming+AND+parade&dafdq=01&dafmq=01&dafyq=1970&datdq=31&datmq=12&datyq=1971&puq=LTN&txf=txIN&ssnip=txt&e=-------en-20--1--txt-txIN-------&f=XML'


#6. Create a loop to search through each page of the search results. 
#range(start, stop, step) is used to ask Python to increment i by 20 for each loop.
#i.e. 1, 21, 41, 61, 81, etc.... i is inserted in the url to request the 
#content for the next page.

#7. Now use the ltn for each section to gather the publication text

        

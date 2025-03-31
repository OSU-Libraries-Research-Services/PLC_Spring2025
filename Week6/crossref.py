# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 15:17:08 2025

@author: murphy.465
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 20:44:12 2025

@author: murphy.465

Use the doi.csv file first find the publisher, article_title, journal_title, journal_abbr, year, and
reference_count for each doi using the Crossref works API.

Then find the dois for articles referenced by the doi.
Find reference lists for an Ohio State publication supported by
a NSF award search .

Gather 'doi','reference_count','reference_doi','last_updated'

base_url="https://api.crossref.org/works/"
    # dois=['10.1021/bi301260u']
    # dois=['10.1109/TAES.2013.6494427']

"""

#1. Import libraries needed for project

#2. Use datetime to identify today's date.
today=date.today()

#3. Configure logging
formatstring="%(asctime)s - %(levelname)s - %(message)s"
datestring="%m/%d/%Y %I%M%S %p"
logging.basicConfig(filename="cr_errors_find_dois.log", level=logging.ERROR, format=formatstring, datefmt=datestring)

#4. Define function to request url and log HTTP errors
def lookup(target_doi):
    try:
        url=base_url+target_doi
        response=requests.get(url)
        response.raise_for_status() #Raise an HTTP Error for bad responses
        json_data = response.json() #Parse JSON response
        return json_data
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP Error = {http_err}") # Log the HTTP error
        time.sleep(10)
    except Exception as err:
        logging.error(f"Other error = {err}") #Log any other errors
        time.sleep(10)
        

#5.  Read in dois.csv and create list of dois from doi column

#6. Create df to store results

#7. Now use the lookup function to find and gather the reference_dois

#8. Store results in .csv file        
  




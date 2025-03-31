# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 10:18:51 2025

@author: murphy.465
"""

# FIND TORTOISES AT THE NATIONAL ZOO

import pandas as pd
import re

df=pd.read_csv('i_met_the_animals.csv')
animals=df.common_name.tolist()
animals=','.join(animals)
pattern="A[a-z]* ?[a-z]* tortoise,"
tortoises=re.findall(pattern, animals)
for each_tortoise in tortoises:
    print(each_tortoise.replace(',',''))
    
# FIND TORTOISES AT THE NATIONAL ZOO AND REPLACE THE COMMON_NAME WITH "SLOW TORTOISE"
pattern="A[a-z]* ?[a-z]* tortoise,"
tortoises_slow=re.sub(pattern,"SLOW TORTOISE,",animals)
print(tortoises_slow.strip())
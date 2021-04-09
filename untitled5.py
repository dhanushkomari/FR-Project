# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 14:57:11 2021

@author: Dhanush.komari
"""
#%%
from datetime import datetime
def recent_time(a):
    rec_time = a 
    year = rec_time[0:4]
    mon = rec_time[5:7]
    day = rec_time[8:10]
    hour = rec_time[11:13]
    mins = rec_time[14:16]
    sec = rec_time[17:19]
    
    new_date = year+'-'+mon+'-'+day+' '+hour+':'+mins+':'+sec
    last_time = datetime.datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S') 
    #print('last_obj_time: ',last_time)
    now = datetime.datetime.now()
    #print('now_time: ', now)
    difference=float((now-last_time).seconds)
    return difference


#%%

import requests
import re
response=requests.get('http://127.0.0.1:8000/api/patients')

x=response.json()
d = x['created_at']
q = recent_time(d)
id=x['first_name']+str(x['id'])
print(id)
l=(re.findall(r"([a-zA-Z]+)([0-9]+)+", id.upper()))

print(l[0][1])




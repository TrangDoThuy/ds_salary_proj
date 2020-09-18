# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:18:13 2020

@author: trang
"""

import glassdoor_scapper as gs
import pandas as pd
path="C:/Users/trang/Desktop/ds_salary_proj/chromedriver"
df = gs.get_jobs('data-scientist',15,False,path,15)
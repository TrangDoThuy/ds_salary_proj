# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:38:49 2020

@author: trang
"""

import pandas as pd
df = pd.read_csv('glassdoor_job.csv')


#salary parsing
df = df[df['Salary Estimate']!='-1']
salary = df['Salary Estimate'].apply(lambda x:x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))
df['min_salary']=minus_Kd.apply(lambda x:int(x.split('-')[0]))
df['max_salary']=minus_Kd.apply(lambda x:int(x.split('-')[1]))
df['avg_salary']=(df['min_salary']+df['max_salary'])/2
#company name text only
df['company_txt']=df.apply(lambda x: x['Company Name'] if x['Rating']<0 else x['Company Name'][:-3],axis=1)
#state field
df['job_state']= df['Location'].apply(lambda x: x.split(',')[-1])

#age of company
df['age']= df.Founded.apply(lambda x: x if x<1 else 2020-x)
#parsing of job description (backend, data engineer, full stack)
print(df['Job Description'][0])
#backend
df['backend_yn'] = df['Job Description'].apply(lambda x: 1 if "backend" in x.lower() else 0)
print(df.backend_yn.value_counts())
#%%
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if "python" in x.lower() else 0)
print(df.python_yn.value_counts())
#%%
df['java_yn'] = df['Job Description'].apply(lambda x: 1 if "java" in x.lower() else 0)
print(df.java_yn.value_counts())
#%%
df['database_yn'] = df['Job Description'].apply(lambda x: 1 if "database" in x else 0)
print(df.database_yn.value_counts())
#%%
df['linux_yn'] = df['Job Description'].apply(lambda x: 1 if "linux" in x.lower() else 0)
print(df.linux_yn.value_counts())
#%%
df['networking_yn'] = df['Job Description'].apply(lambda x: 1 if "networking" in x.lower() else 0)
print(df.networking_yn.value_counts())
#%%
df['testing_yn'] = df['Job Description'].apply(lambda x: 1 if "test" in x.lower() else 0)
print(df.testing_yn.value_counts())
#%%
df['cyber_yn'] = df['Job Description'].apply(lambda x: 1 if "cyber" in x.lower() else 0)
print(df.cyber_yn.value_counts())
#%%
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if "aws" in x.lower() else 0)
print(df.aws_yn.value_counts())
#%%
df.to_csv('salary_software_engineer.csv',index=False)
import pandas as pd
import numpy as np

df = pd.read_csv('Cleaned_startup.csv')
uniq_investors = pd.read_csv('Unique_investor_names.csv')

def startup_names():
    startup_name = sorted(df['Startup'].unique().tolist())
    return  startup_name

def startup_info(startup):
    # There are some NaN values....deal with them latter. 
    return ('Industry Vertical: ' + df[df['Startup'].str.contains(startup,case=False)]['Industry_Vertical'].values[0])
    

def investor_names():
    Investor_name = uniq_investors['unique_Investor'].tolist()
    return  Investor_name

def investor_recent(text):
    if ',' in text:
        text = text.split(',')[0]

    out_df = df[df['Investor'].str.match(text,case=False,na=False)] 

    if out_df.shape[0]>0:   
        return out_df
    
    else:
        out_df = df[df['Investor'].str.contains(text,case=False,na=False)] 
        return out_df





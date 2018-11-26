
# coding: utf-8

# In[16]:


import csv, os
import pandas as pd


# In[52]:


def combine(directory):
    final_df = []
    
    for filename in os.listdir(directory):
        filepath = directory + filename
        df = pd.read_csv(filepath)
            
        df["Algorithm"] = filename[5:-4]
        
        if len(final_df) == 0:
            final_df = df    
        else:
            final_df = final_df.append(df, ignore_index = True)
        
    final_df.to_csv(directory+'Consolidated.csv', index = False)


# In[53]:


combine('./Easy/')


# In[54]:


combine('./Hard/')


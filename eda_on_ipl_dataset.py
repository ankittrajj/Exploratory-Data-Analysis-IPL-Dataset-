# -*- coding: utf-8 -*-
"""EDA_on_IPL_Dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Kvy4e1ZEWtlpFHRC-JXNdjIQOg0UPBZT

# **Exploratory Data Analysis with IPL dataset**
created by Ankit Raj

Import lib
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Read the csv file"""

from google.colab import files
uploaded=files.upload()

import io
df_matches=pd.read_csv('matches.csv')

"""Observing the Deliveries Dataset"""

df_matches.head()

"""Collecting info about the Deleveries Dataset

Visualizing the missing values of Matches Dataset
"""

df_matches.describe()

df_matches.columns

df_matches.info()

"""Finding the unique value of Umpire3"""

df_matches['umpire3'].unique()

"""Let's drop the Umpire3"""

new_df_matches=df_matches.drop(['umpire3'],axis=1)

new_df_matches.head()

sns.heatmap(new_df_matches.isnull())

new_df_matches.to_csv('matches.csv',index=False)

new_df_matches

print('Total number of matches=',df_matches.shape[0])

print(df_matches['season'].nunique())

df_matches['player_of_match'].value_counts()[:10]

df_matches['winner'].value_counts()[:1]

df_matches.head()

df_matches['winner'].value_counts()[:5]
#df_matches['win_by_runs'].value_counts()[:5]

df_matches['city'].value_counts()

bm=df_matches[(df_matches['win_by_runs']>=100)|(df_matches['win_by_wickets']>=8)]

bm['winner'].value_counts()

df_matches.columns

"""Count of match playes in each city"""

print(df_matches['city'].value_counts())

"""Min & Max win_by_wicket in each city"""


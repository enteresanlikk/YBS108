import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/yasarkucukefe/python-egitim/master/lego_sets.csv")

df[['year','theme_id']].groupby('year').agg({'theme_id':'nunique'}).sort_values(['theme_id']).tail(1)
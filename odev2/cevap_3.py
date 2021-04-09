import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/yasarkucukefe/python-egitim/master/lego_sets.csv")

df['year'].nunique()
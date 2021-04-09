import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/yasarkucukefe/python-egitim/master/lego_sets.csv")

df[df['num_parts'] == df['num_parts'].max()][['name', 'num_parts']]
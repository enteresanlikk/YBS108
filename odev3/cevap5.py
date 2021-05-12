import pandas as pd

df = pd.read_csv('https://plantdx.com/docs/df.csv')

# 1
df.plot.scatter(x='a',y='c')

# 2
df.plot.box()

# 3
df.plot.scatter(x='b',y='d',c='a',s=df['c']*50, cmap='viridis')

# 4
import seaborn as sns
sns.heatmap(df.corr(),annot=True)
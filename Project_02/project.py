import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("mymoviedb.csv", lineterminator='\n')
df.head(5)
df.info()

df['Genre'].head(5)
df.duplicated().sum()
df.duplicated().sum()
df['Genre'].head(5)
df.describe()
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
df.head(5)
df['Release_Date'].dtypes
df['Release_Date'] = df['Release_Date'].dt.year
df.head(5)
df['Release_Date'].dtypes
cols = ['Overview', 'Original_Language', 'Poster_Url']
df.drop(cols, axis = 1, inplace = True)
df.head()
def catigorize_col(df, col, labels):
    edges = [df[col].describe()['min'], df[col].describe()['25%'], df[col].describe()['50%'], df[col].describe()['75%'], df[col].describe()['max']]

    df[col] = pd.cut(df[col], edges, labels = labels, duplicates = 'drop')
    return df

labels = ['not_popular', 'below_avg', 'average', 'popular']
catigorize_col(df, 'Vote_Average', labels)
df['Vote_Average'].unique()
df['Vote_Average'].head()
df['Vote_Average'].value_counts()
df.dropna(inplace = True)
df.isna().sum()

df['Genre'] = df['Genre'].str.split(', ')     #Here we have Modify the Genre section we have removed the Sapce and comma from each section

markdown2 = (df.explode('Genre').reset_index(drop = True))    #Here we have crested a index formate to the genre section so that each genre have to be in seperate line or index

print(markdown2.head())

# #Casting Column into category
#df['Genre'].astype('category')

#To check the info of the changed category we will use df.info method 
#print(df.info())

#To check the unique data from the dataset 
#print(df.unique())

#print(df.head())


#Now we are going to Visualize the data using Matplotlib and Seaborn
sns.catplot(y = 'Genre', data = df, kind = 'count', order = df['Genre'].value_counts().index, color = '#4287f5')
plt.title('Genre column Distribution')
plt.show()
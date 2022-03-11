import numpy as np
import pandas as pd

# print(pd.Series([1, 2, 3], index=['a', 'b', 'c'])) # with index
# print(pd.Series([1,2,3], index=['a','b','c']))
# print(pd.Series(np.array([1,2,3]), index=['a','b','c']))
# print(pd.Series({'a':1,'b':2,'c':3}))
# series  = pd.Series({'a':1,'b':2,'c':3})
# print(series['a'])

# wine_dict = {
#     'red_wine':[3,6,5],
#     'white_wine':[5,0,10]
# }
# sales = pd.DataFrame(wine_dict, index=['adam','bob','charles'])
# print(sales)
# print(sales['white_wine'])

president_df = pd.read_csv('president_heights_party.csv', index_col='name')
# print(president_df.shape)
# print(president_df.shape[0])
# print(president_df.size)

# print(president_df.head(n=3))
# print(president_df.tail())
# print(president_df.info())
# print(president_df.loc['Abraham Lincoln'])
# print(type(president_df.loc['Abraham Lincoln']))
# print(president_df.loc['Abraham Lincoln'].shape)
# print(president_df.loc['Abraham Lincoln':'Ulysses S. Grant'])
# print(president_df.iloc[15])
# print(president_df.iloc[15:18])

# print(president_df.columns)
# print(president_df['age'])
# print(president_df['height'].shape)
# print(president_df[['age','height']].head(n=4))
# print(president_df.loc[:,'order':'height'].head(n=3))

# # Min, Max , Mean
# # Measue of Location
# print(president_df.min())
# print(president_df.max())
# print(president_df.mean())
# print(president_df['age'].quantile([0.25,0.5,0.75,1]))
# print(president_df['age'].mean())
# print(president_df['age'].median())

# # Variance and Standard Deviation
# const  = pd.Series([2,3,4])
# # mean = (2+3+4)/3 = 3.0
# # variation = (2-3)^2 + (3-3)^2+ (4-3)^2 = 1+0+1 
# # =2/(n-1)= 2/(3-1)=1   ___
# # standard deviation = /v
# print(const.mean())
# print(const.var())

# print(president_df['age'].var())
# print(president_df['age'].std())
# print(president_df.std())

# # Description describe()
# # prints out almost all of the summary statistics
# print(president_df['age'].describe())
# print(president_df.describe())

# # Categorical variable uses .value_counts
# print(president_df['party'].value_counts())
# print(president_df['party'].describe())

# GroupBy and Aggregation
print(president_df.groupby('party').mean())
print(president_df.groupby('party')['height'].agg(['min',np.median,max]))
print(president_df.groupby('party').agg({'height':[np.median, np.mean],'age':[min,max]}))
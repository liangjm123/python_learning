# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:54:41 2018

@author: liangjm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 5.1 Object Creation
s = pd.Series([1,3,5,np.nan,6,8])
s

dates = pd.date_range('20130101', periods=6)
dates
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
df2
df2.dtypes

###################
# 5.2 Viewing Data
###################
df.head()
df.tail(3)
df.index
df.columns
df.values
df.describe()
df.T # Transposing your data
df.sort_index(axis=1, ascending=False) # Sorting by an axis
df.sort_values(by='B') # Sorting by values

##################
# 5.3 Selection
#################
df['A']  # Selecting a single column
df[0:3]  # Selecting via [], which slices the rows
df.loc[dates[0]]
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']]
df.loc[dates[0],'A']

df.iloc[3] # Select via the position of the passed integers
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]
df.iloc[1,1]

df[df.A > 0] # Using a single column’s values to select data
df[df > 0]

# Using the isin() method for filtering
df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']
df2[df2['E'].isin(['two','four'])]

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
s1
df['F'] = s1
df.at[dates[0],'A'] = 0 # Setting values by label
df.iat[0,1] = 0 # Setting values by position
df.loc[:,'D'] = np.array([5] * len(df)) # Setting by assigning with a NumPy array

####################
## 5.4 Missing Data
####################
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
df1.dropna(how='any') # To drop any rows that have missing data
df1.fillna(value=5) # Filling missing data
pd.isna(df1) # To get the boolean mask where values are nan

####################
## 5.5 Operations
####################
df.mean() # Performing a descriptive statistic
df.mean(1) # Same operation on the other axis

s = pd.Series([1,3,5,np.nan,6,8], index=dates).shift(2)
df.sub(s, axis='index')

df.apply(np.cumsum) # Applying functions to the data
df.apply(lambda x: x.max() - x.min())

s = pd.Series(np.random.randint(0, 7, size=10))
s.value_counts()

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
s.str.lower()

####################
## 5.6 Merge
####################
# Concat
df = pd.DataFrame(np.random.randn(10, 4))
df
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces)

# Join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pd.merge(left, right, on='key')

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
pd.merge(left, right, on='key')
pd.merge(left, right, left_on='key', right_on='key')

# Append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A','B','C','D'])
df
s = df.iloc[3]
df.append(s, ignore_index=True)

####################
## 5.7 Grouping
####################
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                          'C' : np.random.randn(8),
                          'D' : np.random.randn(8)})   
df.groupby('A').sum()
df.groupby(['A','B']).sum()

####################
## 5.8 Reshaping
####################
# Stack
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'], 
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
df2














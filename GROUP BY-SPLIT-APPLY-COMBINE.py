# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 15:47:16 2018

@author: liangjm
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df.groupby()
grouped.first()
grouped.last()
grouped.sum()
pd.MultiIndex.from_arrays()
grouped.get_group()
len()
grouped.size()
describe()
aggregate()
agg() # Applying multiple functions at once
mean()
count()
std()
var()
sem() # Standard error of the mean of groups
nth() # Take nth value, or a subset if n is a list
min()
max()

rolling()
dropna()
transform()
filter()
#######################################
## 16.1 Splitting an object into groups 
#######################################
# 16.1.1 GroupBy sorting
df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
...: 'foo', 'bar', 'foo', 'foo'],
...: 'B' : ['one', 'one', 'two', 'three',
...: 'two', 'two', 'one', 'three'],
...: 'C' : np.random.randn(8),
...: 'D' : np.random.randn(8)})


grouped = df.groupby('A')
grouped = df.groupby(['A', 'B'])
grouped.groups # 查看df分组的属性
grouped.first() # 查看每一组的第一行
grouped.last() # 查看每一组的最后一行
len(grouped) # 组数
grouped.sum()

lst = [1, 2, 3, 1, 2, 3]
s = pd.Series([1, 2, 3, 10, 20, 30], lst)
grouped = s.groupby(level=0)
grouped.first()
grouped.last()
grouped.sum()

df2 = pd.DataFrame({'X' : ['B', 'B', 'A', 'A'], 'Y' : [1, 2, 3, 4]})
df2.groupby(['X']).sum()
df2.groupby(['X'], sort=False).sum()

df3 = pd.DataFrame({'X' : ['A', 'B', 'A', 'B'], 'Y' : [1, 4, 3, 2]})
df3.groupby(['X']).get_group('A')
df3.groupby(['X']).get_group('B')

# 16.1.3 GroupBy with MultiIndex
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
....: ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
....:
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
# 16.1. Splitting an object into groups 
s = pd.Series(np.random.randn(8), index=index)
grouped = s.groupby(level=0) 
grouped.sum()  
s.groupby(level='second').sum()
s.groupby(['first', 'second']).sum()
s.sum(level='second')

# 16.1.4 Grouping DataFrame with Index Levels and Columns
arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
....: ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
....:
index = pd.MultiIndex.from_arrays(arrays, names=['first', 'second'])
df = pd.DataFrame({'A': [1, 1, 1, 1, 2, 2, 3, 3],
....: 'B': np.arange(8)},
....: index=index)
df
df.groupby([pd.Grouper(level=1), 'A']).sum() # 三种等价表达
df.groupby([pd.Grouper(level='second'), 'A']).sum()
df.groupby(['second', 'A']).sum()

# 16.1.5 DataFrame column selection in GroupBy
grouped = df.groupby(['A'])
grouped_C = grouped['C']


#######################################
## 16.2 Iterating through groups 
#######################################
grouped = df.groupby(['A'])
for name, group in grouped:
    print(name)
    print(group)
for name, group in df.groupby(['A', 'B']):
    print(name)
    print(group)

#######################################
## 16.3 Iterating through groups 
#######################################
grouped.get_group('bar')
df.groupby(['A', 'B']).get_group(('bar', 'one'))


#######################################
## 16.4 Aggregation 
#######################################
grouped = df.groupby('A')
grouped.aggregate(np.sum)
grouped = df.groupby(['A', 'B'])
grouped.aggregate(np.sum)
grouped = df.groupby(['A', 'B'], as_index=False) # 之后会把index设置为列名
grouped.aggregate(np.sum)
df.groupby('A', as_index=False).sum()
grouped.size()
grouped.describe()

grouped = df.groupby('A')
grouped['C'].agg([np.sum, np.mean, np.std]) # Applying multiple functions at once
grouped.agg([np.sum, np.mean, np.std])

grouped.agg({'C' : np.sum, 
             'D' : lambda x: np.std(x, ddof=1)}) # Applying different functions to DataFrame columns
grouped.agg({'C' : 'sum', 'D' : 'std'})
grouped.agg({'D': 'std', 'C': 'mean'}) # 输出时按照前后顺序
grouped.agg(OrderedDict([('D', 'std'), ('C', 'mean')])) # 确保按一定顺序输出

#######################################
## 16.4 Transformation 
#######################################
index = pd.date_range('10/1/1999', periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = ts.rolling(window=100,min_periods=100).mean().dropna() # 滚动平均
ts.head()
ts.tail()

key = lambda x: x.year
zscore = lambda x: (x - x.mean()) / x.std()

transformed = ts.groupby(key).transform(zscore) # 按照 key分组计算，但是输出结果保持index，去除了分组
grouped = ts.groupby(key)
grouped.mean()
grouped_trans = transformed.groupby(key)
grouped_trans.mean()

df_re = pd.DataFrame({'A': [1] * 10 + [5] * 10,
.....: 'B': np.arange(20)})
df_re.groupby('A').rolling(4).B.mean()


#######################################
## 16.5 Filtration 
#######################################
sf = pd.Series([1, 1, 2, 3, 3, 3])
sf.groupby(sf).filter(lambda x: x.sum() > 2)

dff = pd.DataFrame({'A': np.arange(8), 'B': list('aabbbbcc')})
dff.groupby('B').filter(lambda x: len(x) > 2)
dff.groupby('B').filter(lambda x: len(x) > 2, dropna=False)

dff['C'] = np.arange(8)
dff.groupby('B').filter(lambda x: len(x['C']) > 2)


#######################################
## 16.5 Flexible apply 
#######################################
# apply 对象是分组的全部数据进行计算，而之前的例子是对每一个元素进行函数计算
grouped = df.groupby('A')
grouped['C'].apply(lambda x: x.describe())

grouped = df.groupby('A')['C']
def f(group): 
    return pd.DataFrame({'original' : group,
                         'demeaned' : group - group.mean()})
grouped.apply(f)

def f(x): 
    return pd.Series([ x, x**2 ], index = ['x', 'x^2'])
s.apply(f)

d = pd.DataFrame({"a":["x", "y"], "b":[1,2]})
def identity(df): 
    print(df) 
    return df


















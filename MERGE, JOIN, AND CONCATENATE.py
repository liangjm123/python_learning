# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 15:33:26 2018

@author: liangjm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

concat()
append() # concat的简化版本，axis=0, join=outer
merge()
join()
#######################################
## 17.1 Concatenating objects 
#######################################
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
...: 'B': ['B0', 'B1', 'B2', 'B3'],
...: 'C': ['C0', 'C1', 'C2', 'C3'],
...: 'D': ['D0', 'D1', 'D2', 'D3']},
...: index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
...: 'B': ['B4', 'B5', 'B6', 'B7'],
...: 'C': ['C4', 'C5', 'C6', 'C7'],
...: 'D': ['D4', 'D5', 'D6', 'D7']},
...: index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
...: 'B': ['B8', 'B9', 'B10', 'B11'],
...: 'C': ['C8', 'C9', 'C10', 'C11'],
...: 'D': ['D8', 'D9', 'D10', 'D11']},
...: index=[8, 9, 10, 11])

df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'],
...: 'D': ['D2', 'D3', 'D6', 'D7'],
...: 'F': ['F2', 'F3', 'F6', 'F7']},
...: index=[2, 3, 6, 7])

df1
df2
df3
frames = [df1, df2, df3]
result = pd.concat(frames)

pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
keys=None, levels=None, names=None, verify_integrity=False,
copy=True)

# • objs : 要合并的对象
#     a sequence or mapping of Series, DataFrame, or Panel objects. If a dict is passed, the sorted keys will be
# used as the keys argument, unless it is passed, in which case the values will be selected (see below). Any None
# objects will be dropped silently unless they are all None in which case a ValueError will be raised.
# 
# • axis : 设置后，按照两个数据框共有的列作为index，axis=0按行，axis=1按列
#     {0, 1, . . . }, default 0. The axis to concatenate along.
#
# • join : inner内部合并，不产生NAN；outer外部合并，不足的补充NAN
#     {‘inner’, ‘outer’}, default ‘outer’. How to handle indexes on other axis(es). Outer for union and inner
# for intersection.
# 
# • ignore_index : 
#     boolean, default False. If True, do not use the index values on the concatenation axis. The
# resulting axis will be labeled 0, . . . , n - 1. This is useful if you are concatenating objects where the concatenation
# axis does not have meaningful indexing information. Note the index values on the other axes are still respected
# in the join.
# 
# • join_axes : 设置一个具体的axis
#     list of Index objects. Specific indexes to use for the other n - 1 axes instead of performing
# inner/outer set logic.
# 
# • keys : 给每一块dataframe设置一个key
#     sequence, default None. Construct hierarchical index using the passed keys as the outermost level. If
# multiple levels passed, should contain tuples.
# 
# • levels : 
#     list of sequences, default None. Specific levels (unique values) to use for constructing a MultiIndex.
# Otherwise they will be inferred from the keys.
# 
# • names : 
#     list, default None. Names for the levels in the resulting hierarchical index.
# 
#    • verify_integrity : 
#     boolean, default False. Check whether the new concatenated axis contains duplicates.
# This can be very expensive relative to the actual data concatenation.
# 
# • copy : 
#     boolean, default True. If False, do not copy data unnecessarily.


pd.concat(frames, keys=['x', 'y', 'z'])
pd.concat([df1, df4], axis=1, sort=False)
pd.concat([df1, df4], axis=1, join='inner')
pd.concat([df1, df4], axis=1, join_axes=[df1.index])

df1.append(df4)
df1.append(df4, ignore_index=True)
pd.concat([df1, df4], axis=0, ignore_index=True)


#######################################
## 17.2 Database-style DataFrame joining/merging 
#######################################
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True,
suffixes=('_x', '_y'), copy=True, indicator=False,
validate=None)

#• left: A DataFrame object.

#• right: Another DataFrame object.

#• on: Column or index level names to join on. Must be found in both the left and right DataFrame objects. If not
#passed and left_index and right_index are False, the intersection of the columns in the DataFrames
#will be inferred to be the join keys.

#• left_on: Columns or index levels from the left DataFrame to use as keys. Can either be column names, index
#level names, or arrays with length equal to the length of the DataFrame.

#• right_on: Columns or index levels from the right DataFrame to use as keys. Can either be column names,
#index level names, or arrays with length equal to the length of the DataFrame.

#• left_index: If True, use the index (row labels) from the left DataFrame as its join key(s). In the case of a
#DataFrame with a MultiIndex (hierarchical), the number of levels must match the number of join keys from the
#right DataFrame.

#• right_index: Same usage as left_index for the right DataFrame

#• how: One of 'left', 'right', 'outer', 'inner'. Defaults to inner. See below for more detailed
#description of each method.

#• sort: Sort the result DataFrame by the join keys in lexicographical order. Defaults to True, setting to False
#will improve performance substantially in many cases.

#• suffixes: A tuple of string suffixes to apply to overlapping columns. Defaults to ('_x', '_y').

#• copy: Always copy data (default True) from the passed DataFrame objects, even when reindexing is not
#necessary. Cannot be avoided in many cases but may improve performance / memory usage. The cases where
#copying can be avoided are somewhat pathological but this option is provided nonetheless.

#• indicator: Add a column to the output DataFrame called _merge with information on the source of each
#row. _merge is Categorical-type and takes on a value of left_only for observations whose merge key only
#appears in 'left' DataFrame, right_only for observations whose merge key only appears in 'right'
#DataFrame, and both if the observation’s merge key is found in both.

#• validate : string, default None. If specified, checks if merge is of specified type.
#– “one_to_one” or “1:1”: checks if merge keys are unique in both left and right datasets.
#– “one_to_many” or “1:m”: checks if merge keys are unique in left dataset.
#– “many_to_one” or “m:1”: checks if merge keys are unique in right dataset.
#– “many_to_many” or “m:m”: allowed, but does not result in checks.


left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
....: 'A': ['A0', 'A1', 'A2', 'A3'],
....: 'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
....: 'C': ['C0', 'C1', 'C2', 'C3'],
....: 'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left, right, on='key')


left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
....: 'key2': ['K0', 'K1', 'K0', 'K1'],
....: 'A': ['A0', 'A1', 'A2', 'A3'],
....: 'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
....: 'key2': ['K0', 'K0', 'K0', 'K0'],
....: 'C': ['C0', 'C1', 'C2', 'C3'],
....: 'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left, right, on=['key1', 'key2'])
pd.merge(left, right, how='left', on=['key1', 'key2'])
pd.merge(left, right, how='right', on=['key1', 'key2'])
pd.merge(left, right, how='outer', on=['key1', 'key2'])
pd.merge(left, right, how='inner', on=['key1', 'key2'])

df1 = pd.DataFrame({'col1': [0, 1], 'col_left':['a', 'b']})
df2 = pd.DataFrame({'col1': [1, 2, 2],'col_right':[2, 2, 2]})
pd.merge(df1, df2, on='col1', how='outer', indicator=True)
pd.merge(df1, df2, on='col1', how='outer', indicator='indicator_column') #自定义命名




left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
....: 'B': ['B0', 'B1', 'B2']},
....: index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
....: 'D': ['D0', 'D2', 'D3']},
....: index=['K0', 'K2', 'K3'])

left.join(right)
left.join(right, how='outer')
left.join(right, how='inner')
pd.merge(left, right, left_index=True, right_index=True, how='outer')
pd.merge(left, right, left_index=True, right_index=True, how='inner')


left = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
....: 'B': ['B0', 'B1', 'B2', 'B3'],
....: 'key': ['K0', 'K1', 'K0', 'K1']})

right = pd.DataFrame({'C': ['C0', 'C1'],
....: 'D': ['D0', 'D1']},
....: index=['K0', 'K1'])

pd.merge(left, right, left_on='key', right_index=True,
how='left', sort=False)

















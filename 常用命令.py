import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 查看现有的数据结构
type() #数据框类型还是数组矩阵类型
df.type #字符串还是数字格式(Numpy)
df.types #字符串还是数字格式(Pandas)

# 元素在字符串里的位置
a = ["ab","cd",1,3]
a.index(1)
np.split()

df = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo',
                    'G':[1,3,2,2],
                   'H':[1,2,4,3]})
df.sort_values(by='G',ascending=True) # 排序
df.sort_values(by=['G','H'],ascending=True)
df[df['E'].isin("test")]['E'] = 'Test'
df['E'] = df['E'].repalce['test','Test']
set('abracadabra')
type(list(set(df['E'])))
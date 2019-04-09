# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:15:35 2017

@author: Administrator
"""


#创建ndarray
import numpy as np
data = [[1,2,3,4],[5,6,7,8]]
arr = np.array(data)
arr.shape #行列数
arr.ndim #行数
arr.dtype

np.zeros((3,6,2)) #创建元素都是0的array
np.empty((3,2,2))
np.arange(15) #创建0~14的array


#Series
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
obj = Series([4,7,-5,3])
obj
obj.values
obj.index = ['Bob','Steve','Jeff','Ryan']
index = obj.index #是不可修改的对象
index[1] = 'd'
index[1:]

obj2 = Series([4,7,-5,3],index=['d','b','a','c'])
obj2 = obj2.reindex(['a','c']) #重新索引
obj2 = obj2.reindex(['a','c','d','b','e']) #重新索引
obj2 = obj2.reindex(['a','c','d','b','e'],fill_value=0) #重新索引,并填充值
obj2
obj2.index 
obj2['a']
new_obj2 = obj2.drop('c') #丢弃指定轴上的数
new_obj2 = obj2.drop(['e','c']) #丢弃指定轴上的数
obj2[obj2>2]
obj2*2
np.exp(obj2)
'b' in obj2

sdata = {'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3 = Series(sdata)
obj3

states = ['California','Ohio','Oregon','Texas']
obj4 = Series(sdata,index=states)
obj4
obj4.name = 'population'
obj4.index.name = 'state'

pd.isnull(obj4) #检测缺失数据
obj4.isnull()
pd.notnull(obj4)

obj3+obj4

#Dataframe
data = {'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9],
        }
frame = DataFrame(data) #构建数据框
frame = DataFrame(data,columns=['year','state','pop']) #如果指定序列
frame['state']
frame['year'] #读取名称为year的列

frame2 = DataFrame(data,columns=['year','state','pop'],
                   index=['one','two','three','four','five']) #加上索引
frame2
frame2['debt'] = 16.5 #加上新的一列
frame2
frame2['debt'] = np.arange(5.)
frame2
frame2['eastern'] = frame2.state == 'Ohio'
frame2
del frame2['eastern'] #删除数据框中的一列
frame2.T #数据框转置
frame2.values #数据框的数据值情况
frame2.drop['two'] #删除数据框的某一行
frame2[:3] #取数据框的前3行
frame2[frame2['pop']<2] #取满足特定条件的行
frame2.ix['two'] #读取索引为two的行
frame2.ix[2] #选取第3行
frame2.ix[:,2] #选取第3列
frame2.ix[:2,:2] #提取数据框的任意一部分
len(frame2) #查看dataframe的行数
len(frame2.columns) #查看dataframe的列数
frame2.head() #查看dataframe的前5行

         
#算数运算和数据对齐
s1 = Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2 = Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
s1
s2
s1+s2     

df1 = DataFrame(np.arange(9.0).reshape((3,3)),columns=list('bcd'),
               index=['Ohio','Texas','Colorado'])
df2 = DataFrame(np.arange(16.0).reshape((4,4)),columns=list('bade'),
               index=['Ohio','Texas','Colorado','Oregon'])    
df1+df2
df1.add(df2,fill_value=0) #把df2加入df1，df1不够的地方补为0
df1.reindex(columns=df2.columns,fill_value=0) #使用df2的列名重构df1
df1/df2      
df1*df2


#Dataframe和Series之间的运算
arr = np.arange(12.).reshape((3,4))
arr       
arr[0] 
arr-arr[0]

frame = DataFrame(np.arange(16.0).reshape((4,4)),columns=list('bade'),
               index=['Ohio','Texas','Colorado','Oregon'])
series = frame.ix[0]
frame-series
series2 = Series(range(3),index=['b','e','f'])
frame + series2

series3 = frame['d']
frame.sub(series3,axis=0) #让数据框的每一列都减去同样的向量,但列名称要相同
series3 = Series(range(5))
frame.sub(series3,axis=0) #列名称不同时，无法使用
series3 = frame.ix['Ohio']
frame.sub(series3,axis=1) #让数据框的每一列都减去同样的向量

         
#函数应用与映射
frame = DataFrame(np.random.randn(4,3),columns=list('bde'),
                  index=['Utah','Ohio','Texas','Oregon'])
frame

np.abs(frame)
f = lambda x: x.max() - x.min() #构建一个函数
frame.apply(f) #默认axis=0，按列进行运算
frame.apply(f,axis=1) #按行进行

def fun(x):
    return Series([x.min(),x.max()],index=['min','max'])
frame.apply(fun) #默认axis=0，按列进行运算
 
           
#排序和排名
obj = Series([7,-5,7,4,2,0,4])
obj.order()
obj.rank()
obj.rank(method='first') #升续，值越大分值越大
obj.rank(ascending=False,method='max') #降续

frame = DataFrame({'b':[4,7,-3,2],'a':[0,1,0,-1]})
frame
frame.sort_index(by='b') #使数据框按照b列的数值大小排序
frame.rank(axis=1) #按行

df = DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
df
df.ix['b']


#汇总和计算描述统计
df = DataFrame(np.random.randn(4,3),index=['a','b','c','d'])
df
df.sum(axis=1) #按行加总
df.mean(axis=1,skipna=False) #skipna表示排除NA值
df.idxmax() #显示每列的最大值位置
df.idxmin() #显示每列的最小值位置
df.describe() #每一列的描述性统计
df.var() #每一列的方差
df.std() #每一列的标准差
df.cumsum() #每一列的累计和
df.corr() #计算相关系数矩阵，变量个数为列数
df.cov() #计算方差-协方差矩阵，变量个数为列数

      
#唯一值、值计数以及成员资格
obj = Series(['c','a','d','a','a','b','b','c','c'])
obj
obj.unique()
pd.value_counts(obj.values,sort=False) #计数
mask = obj.isin(['b','c'])
obj[mask]


#处理缺失值
string_data = Series(['aa','bb',np.nan,'cc'])
string_data
string_data.isnull()

from numpy import nan as NA
data = Series([1,NA,3.5,NA,7])
data.dropna() #剔除缺失值
data[data.notnull()] #剔除缺失值

data = DataFrame([[1.,6.5,3.],[1.,NA,NA],
                 [NA,NA,NA],[NA,6.5,3.]])
data.dropna() #丢弃缺失值所在行
data.dropna(axis=1) #丢弃缺失值所在列
data.dropna(how='all') #只丢弃全部值都缺失的行
data.dropna(axis=1,how='all') #只丢弃全部值都缺失的列

df = DataFrame(np.random.randn(7,3))
df.ix[:4,1] = NA; df.ix[:2,2]=NA
df
df.dropna(thresh=2) #2表示把缺失值<2的行删除
df.fillna(0) #把缺失值填充为0
df.fillna(df.mean()) #把缺失值填充为每列的均值
df.fillna({1:0.5,2:-1}) #第2列填充为0.5,第3列填充为-1

df = DataFrame(np.random.randn(7,3))
df.ix[4:,1] = NA; df.ix[2:,2]=NA
df
df.fillna(method='ffill') #把缺失值按照上一个数值填充
df.fillna(method='bfill') #把缺失值按照下一个数值填充
df.fillna(method='ffill',limit=2) #把缺失值按照上一个数值填充,每列填充2个缺失值


#层次和索引
data = Series(np.random.randn(10),
              index=[['a','a','a','b','b','b','c','c','d','d'],
                     [1,2,3,1,2,3,1,2,2,3]])
data
data.index
data['b']
data['b':'c']
data.ix[['b','c']]
data[:,2]
data.unstack()
data.unstack().stack()

frame = DataFrame(np.arange(12).reshape((4,3)),
                  index=[['a','a','b','b'],[1,2,1,2]],
                  columns=[['Ohio','Ohio','Colorado'],
                           ['Green','Red','Green']])
frame.index.names = ['key1','key2']
frame.columns.names = ['state','color']
frame
frame['Ohio']
frame.sortlevel(1)
frame.sum(level='key2')
frame.sum(level='color',axis=1)


#使用DataFrame的列
frame = DataFrame({'a':range(7),'b':range(7,0,-1),
                   'c':['one','one','one','two','two','two','two'],
                       'd':[0,1,2,0,1,2,3]})
frame
frame2 = frame.set_index(['c','d'])
frame.set_index(['c','d'],drop=False) #把作为索引的列保留为值
frame2.reset_index() #解除索引，并且把索引放入数据框值中

                  
#合并数据集
df1 = DataFrame({'key':['b','b','a','c','a','a','b'],
                 'data1':range(7)})
df2 = DataFrame({'key':['a','b','d'],
                 'data2':range(3)})
df1
df2
pd.merge(df1,df2,on='key') #取交集
pd.merge(df1,df2,how='outer') #取并集
pd.merge(df1,df2,on='key',how='left')

df3 = DataFrame({'lkey':['b','b','a','c','a','a','b'],
                 'data1':range(7)})
df4 = DataFrame({'rkey':['a','b','d','a'],
                 'data2':range(4)})
df5 = DataFrame({'lkey':['a','b','d','a'],
                 'data2':range(4)})
df3
df4
df5
pd.merge(df3,df4,left_on='lkey',right_on='rkey') #两个不同的基准向量
pd.merge(df3,df5,how='inner')
df3.join(df5,on='lkey')

left = DataFrame({'key1':['foo','foo','bar'],
                  'key2':['one','two','one'],
                  'lval':[1,2,3]})
right = DataFrame({'key1':['foo','foo','bar','bar'],
                   'key2':['one','one','one','two'],
                          'rval':[4,5,6,7]})
left
right
pd.merge(left,right,on=['key1','key2'],how='outer') #两个基准向量的合并
pd.merge(left,right,on=['key1','key2']) #默认取交集

#轴向连接
arr = np.arange(12).reshape((3,4)) #创建一个数组矩阵
np.concatenate([arr,arr],axis=1)
np.concatenate([arr,arr],axis=0) #nump包的函数

s1 = Series([0,1],index=['a','b'])
s2 = Series([2,3,4],index=['b','c','d'])
s3 = Series([5,6],index=['f','g'])

pd.concat([s1,s2]) 
pd.concat([s1,s2],axis=1) #pandas包的函数
pd.concat([s1,s2],axis=1,join='inner') #以index为轴，取交集，不进行组合

frame = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]]) #创建一个dataframe
pd.concat([frame,frame]) #向下合并两个矩阵,需要列名一样
pd.concat([frame,frame],axis=1) #向右合并两个矩阵，需要行名一样

frame1 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]],
                      index=['a','b','c'],
                            columns=['one','two','three','four']) #创建一个dataframe
frame2 = pd.DataFrame([[1,2,3,4],[4,5,6,7],[7,8,9,10]],
                      index=['a','b','e'],
                            columns=['one','two','three','four']) #创建一个dataframe
pd.concat([frame1,frame2],axis=1) #两个矩阵的列名不一样，会去并集，用NaN填充
pd.concat([frame1,frame2],axis=1,ignore_index=True) #列索引会重新编号
pd.concat([frame1,frame2],axis=1,keys=['one','two','three']) #给各个矩阵块命名


#合并重叠数据
a = Series([np.nan,2.5,np.nan,3.5,4.5,np.nan],
           index=['f','e','d','c','b','a'])
b = Series(np.arange(len(a),dtype=np.float64),
           index=['f','e','d','c','b','a'])
b[-1] = np.nan

a
b
np.where(pd.isnull(a),b,a) #用b中的值补齐a中的缺失值
b.combine_first(a) #combine_first函数，用b的值去补齐a，也可用在dataframe中
b[:-2].combine_first(a[2:])


#利用函数映射进行数据转换
data = DataFrame({'food':['bacon','pulled pork','bacon','Pastrami',
'corned beff','Bacon','pastrami','honey ham','nova lox'],
    'ounces':[4,3,12,6,7.5,8,3,5,6]})
meat_to_animal = {'bacon':'pig','pulled pork':'pig','pastrami':'cow',
'corned beef':'cow','honey ham':'pig','nova lox':'salmon'}

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
data['food'].map(lambda x: meat_to_animal[x.lower()])


#重命名索引轴
data_new = data.set_index(['food'],drop=True)
data_new.index = data_new.index.map(str.upper)
data_new.rename(index={'BACON':'goat'},
                columns={'ounces':'pounds'}) #不改变原数据
data_new.rename(index={'BACON':'goat'},
                columns={'ounces':'pounds'},inplace=True) #改变原数据

#替换值
data = Series([1.,-999,2.,-999,-1000,3.])
data.replace(-999,np.nan)
data.replace([-999,-1000],np.nan)




















































# 读取excel文件

import pandas as pd
data = pd.read_excel('C:/Users/Administrator/Desktop/123.xlsx')
data.head()
data.index
data.names
data.ix[0,0]

# 读取csv文件
import pandas as pd
data = pd.read_csv('C:/Users/Administrator/Desktop/124.csv',sep=',')
data.head()

pd.read_csv()

###################
# 一、对列表去重
###################
# 1.用循环查找的方式
li = [1,2,3,3,4,2,3,4,5,6,1]
news_li = []
for i in li:
    if i not in news_li:
        news_li.append(i)
print (news_li)

# 2.用集合的特性set()
li1 = [1,4,3,3,4,2,3,4,5,6,1]
new_li1 = list(set(li1))

# 3.使用itertools模块的grouby方法
    import itertools
    li2 = [1,4,3,3,4,2,3,4,5,6,1]
    li2.sort() # 排序
    it = itertools.groupby(li2)
    for k, g in it:
        print (k)

# 4.运用while循环遍历的方式

    def quchong(lb):
        for x in lb:
            while lb.count(x)>1:
                del lb[lb.index(x)]
        return lb
    li3 = [1,4,3,3,4,2,3,4,5,6,1]
    quchong(li3)

# 5.使用keys()方式

    li4 = [1,0,3,7,7,5]
    formatli = list({}.fromkeys(li4).keys())
    print (formatli)


###################
# 二、对数据框去重
###################
# 1.用unique()对单属性列去重

    import pandas as pd
    data = {'id':['A','B','C','C','C','A','B','C','A'],'age':[18,20,14,10,50,14,65,14,98]}
    data = pd.DataFrame(data)
    data.id.unique()
    #或者
    import numpy as np
    np.unique(data.id)

# 2.用frame.drop_duplicates()对单属性列去重

    data.drop_duplicates(['id'])

# 3.用frame.drop_duplicates()对多属性列去重

    data.drop_duplicates(['id','age'])

# 4.用frame.duplicated()对多属性列去重

    isduplicated = data.duplicated(['id','age'],keep='first')
    data.loc[~isduplicated,:]

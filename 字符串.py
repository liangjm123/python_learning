import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

var1 = 'Hello World!'
var2 = "Python Runoob"
# 访问字符串中的值
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# 字符串更新
var1 = 'Hello World!'
var1 = var1[:6] + 'Runoob!'

## 字符串运算符
# +	字符串连接 a + b
# *	重复输出字符串 a * 2
# []	通过索引获取字符串中字符 a[1]
# [ : ]	截取字符串中的一部分 a[1:4]
# in	成员运算符 - 如果字符串中包含给定的字符返回 True  "H" in a
# not in 	成员运算符 - 如果字符串中不包含给定的字符返回 True "M" not in a
# r/R	原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
#     原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。print r'\n';print R'\n'

# 字符串格式化
# 基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
print ("My name is %s and weight is %d kg!" % ('Zara', 21) )
print ("My name is %s and weight is %f kg!" % ('Zara', 21.15) )
# %c	 格式化字符及其ASCII码
# %s	 格式化字符串
# %d	 格式化整数
# %u	 格式化无符号整型
# %o	 格式化无符号八进制数
# %x	 格式化无符号十六进制数
# %X	 格式化无符号十六进制数（大写）
# %f	 格式化浮点数字，可指定小数点后的精度
# %e	 用科学计数法格式化浮点数
# %E	 作用同%e，用科学计数法格式化浮点数
# %g	 %f和%e的简写
# %G	 %f 和 %E 的简写
# %p	 用十六进制数格式化变量的地址

# 字符串内建函数
1、string.capitalize() 把字符串的第一个字符大写
2、string.center(width) 返回一个原字符串居中, 并使用空格填充至长度 width 的新字符串
# str.center(width[, fillchar])
str = 'runoob'
str.center(20, '*')
str.center(20)
3、string.count(str, beg=0, end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

# sub - - 搜索的子字符串
# start - - 字符串开始搜索的位置。默认为第一个字符, 第一个字符索引值为0。
# end - - 字符串中结束搜索的位置。字符中第一个字符的索引为
# 0。默认为字符串的最后一个位置。

str = "this is string example....wow!!!";
sub = "i";
str.count(sub, 4, 40)
str.count(sub)

4、string.endswith(obj, beg=0, end=len(string)) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
   string.startswith(obj, beg=0,end=len(string))

# str.endswith(suffix[, start[, end]])
# suffix - - 该参数可以是一个字符串或者是一个元素。
# start - - 字符串中的开始位置。
# end - - 字符中结束位置。
str = "this is string example....wow!!!";

suffix = "wow!!!";
str.endswith(suffix);
str.endswith(suffix,20);

suffix = "is";
str.endswith(suffix, 2, 4);
str.endswith(suffix, 2, 6);

5、string.find(str, beg=0, end=len(string)) 检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
   string.rfind(str, beg=0,end=len(string) ) 从右边开始查找.
6、string.isalnum()  如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
7、string.isalpha() 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
8、string.isdigit()  如果 string 只包含数字则返回 True 否则返回 False.
9、string.isnumeric() 如果 string 只包含数字字符则返回 True 否则返回 False.

10、string.join(seq) 以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
str = "-";
seq = ("a", "b", "c"); # 字符串序列
print(str.join( seq ));

11、string.lower() 转换 string 中所有大写字符为小写.
    string.upper() 转换 string 中的小写字母为大写
12、string.replace(str1, str2,  num=string.count(str1)) 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
str.replace(old, new[, max])
str = "this is string example....wow!!! this is really string";
print(str.replace("is", "was"));
print(str.replace("is", "was", 3));

13、string.split(str="", num=string.count(str)) 以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串

str.split(str="", num=string.count(str)).
str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num - - 分割次数。默认为 - 1, 即分隔所有。

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print(str.split( ));       # 以空格为分隔符，包含 \n
print(str.split(' ', 1 )); # 以空格为分隔符，分隔成两个























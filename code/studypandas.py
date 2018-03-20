#1.引入pandas
import numpy as np
import pandas as pd 
#2. 创建数据集
    # 生成创建一个6*4的数据集
data2 = pd.DataFrame(np.random.rand(6,4),columns=list('ABCD'))
#print(data2)
    #先创建一个时间索引
dates = pd.date_range('20170101',periods=6)
#print(dates)
    #在创建一个6*4的数据
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
#print(df)
#3、使用字典来创建数据
df2 = pd.DataFrame({'A':np.random.randn(3)})
#print(df2)
#4、另一种字典创建数据的方法
df3 = pd.DataFrame({'A':pd.Timestamp('20180320'),'B':np.random.randn(3)})
#print(df3)

'''
第二部分：查看数据集
'''
#1.使用dtypes来查看各行的数据格式
#print(df3.dtypes)
#2.查看数据框中所有的数据
#print(df3)
#3.使用head查看前几行数据（默认是前5行）
#print(df.head(3))
#4.使用tail查看后5行数据
#print(df.tail(3))
#5.查看数据框的索引
#print(df.index)
#6.用columns查看列名
#print(df.columns)
#7.用values查看数据值
#print(df.values)
#8.用describe查看描述性文件
#print(df.describe())
#9.用T转置，即行列转换
#print(df.T)
#10.用sort_values对数据进行排序 
#print(df.sort_values(by='C'))
'''
第三部分:选择数据
'''
#1.选择A列的数据进行操作
#print(df['A'])
#2.使用数据的切片操作得到行数据
#print(df[1:3])
#3.使用行标签来指定输出的行（列不限定，行限定）
#print(df['20170102':'20170104'])
#4.使用loc方法选择多行数据（列不限定，行限定）
#print(df.loc[dates[0]:dates[2],:])
#5.使用loc方法选择多列数据（行不限定，列限定）
#print(df.loc[:,'B':'D'])
#6.使用loc方法选择多列数据（行列都限定，且列要特定的列）
#print(df.loc[dates[0]:dates[2],['B','D']])
#7.使用loc方法选择某行数据（如第一行）
#print(df.loc[dates[0]])
#8.使用loc方法只选择某一个数据，可以指定行和列
#print(df.loc[dates[0],'B'])
#9.at方法专门用于获取某个值
#print(df.at[dates[0],'B'])
#10.使用iloc方法提取第四行数据
#print(df.iloc[3])
#11.返回4-5行，2-3列数据
#print(df.iloc[3:5,1:3])
#12.提取不连续的行和列的数，如2，4，6行的B列D列
#print(df.iloc[[1,3,5],[1,3]])
#13.提取某一行或某几行数据，保证所有列都在
#print(df.iloc[1:3,:])
#14.提取某个值，如第二行第二列
#print(df.iloc[1,1])
#15.iat是专门提取某个数的方法，它的效率更高
#print(df.iat[1,1])
'''
第四部分：读取和保存数据

#读取csv文件，
#读取excel文件，
#读取.dat文件
#保存为csv文件
df4 = pd.read_csv(r'E:/work/ML/prml/PRML-FOLLOW/dat/user_info.csv',encoding='gbk')
excel_content = pd.read_excel()
content = pd.read_table()
excel_content.to_csv('',encoding='utf-8',index=False)
'''
'''
第五部分：筛选数据
'''
#1.筛选D列数据中大于0的行
#df[df.D>0]
#2.使用&符号可以实现多条件筛选
#df[(df.D>0)&(df.C<0)]
#3.使用|符号可以实现多条件筛选
#df[(df.D>0)|(df.C<0)]
#4.我们也可先限定行列，在筛选
#df[['A','C']][(df.B>0)&(df.D>0)]
#5.使用isin方法来筛选特定的值，把要筛选的值写到一个列表里
#goal_list = [0.164645,0.646455,0.481654] 
#df['D'].isin(goal_list)
'''
第六部分：增加删除数组
'''
#1.增加列
# 在df数据中增加一列
#df['E'] = pd.Series(np.random.randn(6),index=df.index)
#print(df)
#还可以插入一列数据到任意位置，如第2列
#df.insert(1,'a',np.random.randn(6))
#print(df)
#2.删除列
#永久删除某一列数据用del
#del df['a']
#用drop不改变原有的df中的而数据，而是返回另一个dataframe来存放删除后的数据
#df9=df.drop(['D','E'],axis=1)

'''
第七部分：计数统计
'''




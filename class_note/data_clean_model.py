# pip install xlrd
# pip install missingno
# pip install matplotlib
# pip install seaborn
import pandas as pd
import numpy as np
from collections import Counter
from sklearn import preprocessing
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.special import boxcox1p
import seaborn as sns

%matplotlib inline
# windows下配置 font 为中文字体，自己去该路径找到自己电脑自带的字体
myfont = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)
plt.rcParams['font.sans-serif'] = [myfont.get_name()]  # 中文字体设置-宋体
plt.rcParams['axes.unicode_minus'] = False #解决负号显示问题
# mac下配置 font 为中文字体，自己找到自己电脑自带的字体
# myfont = FontProperties(fname="/System/Library/Fonts/Supplemental/simsun.ttc")
# plt.rcParams['font.sans-serif'] = [myfont.get_name()]  # 中文字体设置-宋体
# plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
sns.set(font=myfont.get_name())  # 解决Seaborn中文显示问题

DATA_PATH ='./plant.xlsx'
data=pd.read_excel(DATA_PATH)
data.head()
data

data.shape
data.describe()

#列级别的判断,但凡某一列有null值或空的，则为真
data.isnull().any()

#将列中为空或者null的个数统计出来，并将缺失值最多的排前
total = data.isnull().sum().sort_values(ascending=False)
print(total)

#输出百分比：
percent =(data.isnull().sum()/data.isnull().count()).sort_values(ascending=False)
missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
missing_data.head(20)

data.duplicated().sum()
data.drop_duplicates() #如果要真正改变原始数据，要data= 

data.columns
id_col=['中文名']
cat_col=['花色','叶序']
cont_col=['花瓣长度','花瓣宽度','植株高度','种子直径']
display(data[cat_col])
display(data[cont_col])

# 去除缺失数据
data_1=data.dropna(axis=0)
data_1

for i in cat_col:
    print(pd.Series(data_1[i]).value_counts())
    plt.plot(data_1[i])

# 对于离散型数据，对其获取哑变量
dummies=pd.get_dummies(data[cat_col])
dummies
# 如果有很多种，就会导致数据量变大，学随机森林时会知道增加了随机森林的深度

a=[1,2,3,4,5,6,73,5,32,9,56]
m1=np.mean(a)
m2=np.std(a)
a=(a-m1)/(m2-m1)
a

#偏度，是统计数据
# 计算偏度
skewed_feats = data[cont_col].apply( lambda x: (x.dropna()).skew() )#compute skewness
print(skewed_feats)
skewed_feats = skewed_feats[skewed_feats > 0.75]
skewed_feats = skewed_feats.index

# 如果偏度很大，进行boxcoxlp变换
lam = 0.15
data_fill_na=data.fillna(data.mean())# 用平均值来填充缺失数据
data_fill_na[skewed_feats] = boxcox1p(data_fill_na[skewed_feats], lam)
skewed_feats

#对于连续型数据，对其进行标准化
#标准化过程
#(data[cont_col[0]]-np.mean(data[cont_col[0]]))/np.std(data[cont_col[0]])

scaled=preprocessing.scale(data_fill_na[cont_col])
scaled=pd.DataFrame(scaled,columns=cont_col)
scaled

m=dummies.join(scaled)
data_cleaned=data[id_col].join(m)
data_cleaned.drop_duplicates()

# 数据间的相关性
corrmat=data_cleaned.corr()
corrmat

def corr_heat(df):
    dfData=df.corr()
    plt.subplots(figsize=(12,9))
    sns.heatmap(dfData, annot=True,vmax=1,square=True,cmap="Blues")
    # plt.savefig ('./BluesStateRelation.png')
    plt.show()

corr_heat(data_cleaned)

def corr_heat(df):
    dfData=abs(df.corr())
    plt.subplots(figsize=(12,9))
    sns.heatmap(dfData, annot=True,vmax=1,square=True,cmap=plt.cm.gray)
    plt.show()

corr_heat(data_cleaned)

k = 4 #number of variables for heatmap
cols = corrmat.nlargest(k, '花色_白' )['花色_白'].index
cm = np.corrcoef(data_cleaned[ cols].values.T)
hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 12}, yticklabels=cols.values, xticklabels =cols.values)
plt.show()



# 数据清洗
+ 有序和无序数据，离散和连续数据
+ 解决中文数据集出现的问题
+ 如果将红白粉定义成1，2，3，如果平均就会出现问题

`假设所有的数据都符合线性关系，假设所有的数据都符合正态分布`
+ 中文字体加载不出来
    - windows下配置中文字体
    - > myfont = FontProperties(fname=r"c:\windows\fonts\simsun.ttc",           size=14)
        plt.rcParams['font.sans-serif'] = [myfont.get_name()]  # 中文字体设置-宋体
        plt.rcParams['axes.unicode_minus'] = False #解决负号显示问题 
    - > \# pip install xlrd         
        \# pip install missingno        
        \# pip install matplotlib       
        \# pip install seaborn      
        import pandas as pd     
        import numpy as np      
        from collections import Counter     
        from sklearn import preprocessing       
        from matplotlib import pyplot as plt        
        from matplotlib.font_manager import FontProperties      
        from scipy.special import boxcox1p      
        import seaborn as sns           
        %matplotlib inline      
        \# windows下配置 font 为中文字体，自己去该路径找到自己电脑自带的字体        
        \# myfont = FontProperties      (fname=r"c:\windows\fonts\simsun.ttc", size=14)     
        \# mac下配置 font 为中文字体，自己找到自己电脑自带的字体
        myfont = FontProperties(fname="/System/Library/Fonts/      Supplemental/Songti.ttc")        
        plt.rcParams['font.sans-serif'] = [myfont.get_name()]  # 中文字体设置-宋体      
        plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题         
        sns.set(font=myfont.get_name())  # 解决Seaborn中文显示问题      


+ 数据缺失不超过20%，但也有例外，量化历史学，比如利用税收人口推断政治情况，但他们常常会缺数据
+ 对于离散型数据而言，缺失数据是不可容忍的


## 哑变量
### 离散变量的处理
`对于离散数据处理的第一步，把所有数据处理成哑变量`
`如果有很多种，就会导致数据量变大，学随机森林时会知道增加了随机森林的深度`
### 连续变量的处理
+ 线性模型的问题在于常常会被一些很大的点影响太大，所以要归一化处理
+ min,max归一化处理（消除数据的大小不同带来的权重过大过小问题）
    - Min-Max：$\frac{x-min}{max-min}$，也可能在后面乘上系数，因为常常会有有些东西的权重确实要比其他的要重
    - 归一化不一定是放到0-1之间，只要范围统一都叫归一化
+ 标准化处理（消除数据的差异度）
    - $\frac{x-Mean}{Stand}$如果本身数据符合正态分布就可以用这种方式让数据处理起来更加简单
+ 消除正态分布的偏度
    - boxcoxlp函数
`以后用随机数时，要保留自己生成的随机种子`


## 相关性分析，对数据做一个相关性处理
+ 相关性的算法很多，包括有用距离计算

## 最后可以做出相关性的图
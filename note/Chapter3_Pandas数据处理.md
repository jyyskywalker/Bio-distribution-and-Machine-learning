# Chapter3 Pandas数据处理
1. Pandas对象简介
+ 三个基本数据结构：Series,DataFrame,Index
    - Series对象
        + **`Series是特殊的字典`** 
        + Series对象是一个带索引数据构成的一维数组
        + 用values属性和index属性
            - index属性返回结果类型是pd.Index
        + 可以直接定义索引，定义成自己想要的类型000 
        + ***`可以在创建Series对象时显式定义索引，最后只会保留显式定义的键值对`***
    - DataFrame对象
        + DataFrame可以看作由行索引和列索引的二维数组
        + index和columns
        + 创建DataFrame
    - Index对象
        + `可以将Index对象看成是一个不可变数组或有序集合（实际上是一个多集，因为Index对象可能包含重复值）`
        + 看成不可变数组 
            - Index对象的索引是**不可变**的，可以索引共享时更加安全
        + 看成有序集合
            - 遵循数据结构set的用法，并集、交集、差集

2. 数据取值与选择
+ Series数据选取方法  
    - 将Series看作字典
        +   我们还可以用 Python 字典的表达式和方法来检测键 / 索引和值：
            >   In[3]: 'a' in data      
                Out[3]: True        
                In[4]: data.keys()      
                Out[4]: Index(['a', 'b', 'c', 'd'], dtype='object')         
                In[5]: list(data.items())       
                Out[5]: [('a', 0.25), ('b', 0.5), ('c', 0.75), ('d', 1.0)]      
    - 将Series看作一维数组
        + 切片是绝大部分混乱之源。需要注意的是，当使用 显式索引（即 data['a':'c']）作切片时，结果包含最后一个索 引；而当使用隐式索引（即 data[0:2]）作切片时，结果不包含 最后一个索引。
    - 索引器：loc、iloc和ix
        + loc,取值和切片都是显式的
        + iloc取值和切片都是隐式的
        + ix是两种索引形式混合形式，ix主要用于DataFrame对象
        + **`Python 代码的设计原则之一是“显式优于隐式”。使用 loc 和 iloc 可以让代码更容易维护，可读性更高。特别是在处理整数索引的对 象时，我强烈推荐使用这两种索引器。它们既可以让代码阅读和理 解起来更容易，也能避免因误用索引 / 切片而产生的小 bug`**
+ DataFrame数据选取方法
        - data['area'], data.area
        - 避免对用属性形式选择的列直接赋值
        - values,T(转置) 

3. Pandas数值运算方法
+ **`Pandas 也实现了一些高效技巧：对于一元运算（像函数与三角函 数），这些通用函数将在输出结果中保留索引和列标签；而对于二元运 算（如加法和乘法），Pandas 在传递通用函数时会自动对齐索引进行计 算。这就意味着，保存数据内容与组合不同来源的数据——两处在 NumPy 数组中都容易出错的地方——变成了 Pandas 的杀手锏。`**
+ 通用函数：索引对齐

4. 处理缺失值
+ 主要涉及的缺失值有三种形式：null,NaN或NA
+ 选择处理缺失值的方法
    - 通过一个覆盖全局的掩码表示缺失值
    - 用一个标签值表示缺失值
+ Python使用标签值表示缺失值
    - 第一种None，但是只能用object类型
        + 如果用sum()或者min()常常会出现错误
    - NaN，一种特殊的浮点数
        + 如果使用sum(),min(),max()等操作虽然不会报错，但是也会出错  
+ 处理缺失值
    - isnull()  创建一个布尔类型的掩码标签缺失值。
    - notnull() 与 isnull() 操作相反。 
    - dropna()  返回一个剔除缺失值的数据。
        + how参数any,all
        + thresh参数设置行或列中非缺失值的最小数量 
    - fillna()  返回一个填充了缺失值的数据副本
        + 可以用缺失值前面的有效值来从前往后填充（forward-fill）：
        + > data.fillna(method='ffill')
        + 也可以用缺失值后面的有效值来从后往前填充（back-fill）：
        + > data.fillna(method='bfill')
        + DataFrame需要在填充时设置坐标参数axis

5. ***层级索引*** P210
+ 直接获取


6. 合并数据集:Concat和Append操作
+ pd.merge()实现了一对一、多对一和多对多

7. 累计与分组
+ pandas的累计方法
    - count(),first(),last(),mean(),median(),min(),max(),std(),var(),mad(),prod(),sum()
+ GroupBy:分割、应用和组合
    - GroupBy 中最重要的操作可能就是 aggregate、filter、transform 和 apply（累计、过滤、转换、应用）了

8. 数据透视表
+ 
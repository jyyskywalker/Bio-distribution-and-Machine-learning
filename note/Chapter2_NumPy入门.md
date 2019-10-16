#NumPy入门
## Python中的数据类型
1. Python中的整型不只是整数
    + > struct _longobject{     
            &emsp;  long ob_refcnt; //用于引用计数      
            &emsp;  PyTypeObject *ob_type;//将变量类型编码      
            &emsp;  size_t ob_size;//指定接下来数据成员大小         
            &emsp;  long ob_digit[1];//包含我们希望Python变量表示的实际整型值        
            }
    + 列表也不只是列表
        - 列表中可以包含不同类型的数据
        - Python列表包含一个指向指针块的的指针，然后指针再指向各自的结构体 
2. python中固定类型数组
    + python自带的array
    + NumPy中的ndarray
3. np.array
    + 创建数组
        - numpy可以使用多种方式创建数组
            + zeros, ones, arange, random.random, random.normal, random.randint, linspace, eye 
    + 用dtype关键词设置数据类型
        - numpy中的数据类型和c语言中的类似 
    + 可以指定为多维的
        > np.array([range(i,i+3) for i in [2,4,6]]) 
        > np.zeros((3,3),dtype=int16)
        

## NumPy数组基础
**`注意区别数组和矩阵`**
1. 数组的属性
    + *`在生成随机树时，可以未NumPy随机数生成器设置一组种子值，以确保每次程序执行时可以生成同样的随机数组`*
       - > np.random.seed(0) #设置随机数种子
    + 可以直接指定参数**size=(x1,x2,x3)**
        - 数组有**nidm**（数组的维数）、**shape**（数组每个维数的大小）和**size**（数组的总大小）属性
        - 还有dtype  
        - 表示每个数组元素字节大小的itemsize和总字节nbytes
2. 数组的索引
    + 下标索引以及负号索引，多维数组用索引元组
3. 数组的切分
    + 切片语法
        - > x[start:stop:step] 
        - **方便的逆序数组方式：> x[::-1]** 
        - 多维子数组切片，用同样方式处理，然后用**,**隔开
        - 获取数组的行和列
            + 可以将索引与切片组合起来，用":"表示空切片
            + > x2[:,0]  
        - **`切片返回的是数组数据的视图，而不是副本，所以修改会改变原来的，这种方式在处理非常大的数组集时，可以获取或处理这些数据集的片段，而不用复制底层数据缓存`** 
        - 用**copy()**就可以创建副本
4. 数组的变形
    + 最方便的是用**reshape()**实现的，将一维数组转化为二维的行或列的矩阵
    + 可以用reshape(),也看可以用**newaxis()**
5. 数组的拼接和分裂
    + 数组的拼接
        - **np.concatenate** 
        - > np.concatenate([x,y,z])
        - 沿着固定维数处理数组时，用**np.vstack**（垂直栈）和**np.hstack**（水平栈）会更方便
        - np.dstack将沿着第三个维数拼接数组
    + 数组的分裂 
        - **np.split, np.hsplit, np.vsplit**
        - 可以向它们传递索引列表作为参数

## NumPy数组的计算
`让计算变快利用向量化操作，通常在函数ufunc中实现`
1. 循环会非常慢
2. 通用函数
    1. 一元通用函数
        + 就像matlab中的一样 
        + 运算符其实对应的时NumPy内置函数的封装器
            - 如+对应add，//对应地板除法运算，其实就是除了之后还是整数
        + **np.abs(),三角函数，指数对数:np.exp(x), np.exp2(x), np.power(3,x), np.ln(x), np.log2(x), np.log10(x)** 
        + 一些特殊版本，有更好的精度：exp(x)-1:expm1(x)  log(1+x):np.log1p(x)
        + 晦涩的通用函数来源时子模块**scipy.special**，包含很多在统计学中用到的
    2. 二元通用函数
3. 高级的通用函数特性
    + 用**out**参数指定输出，较大数组慎用out参数
    + 聚合：> np.add.reduce(x), np.mutiply.reduce(x)
        - 需要存储中间结果用**accumulate**
    + **outer()** 实现矩阵外积 
4. 聚合
    + numpy自带sum, min, max
    + 多维度聚合
        - axis关键词指定的是数组会被折叠的维度 
    + 还有其他的聚合函数可查表 
5. 数组的计算：广播
    + `即将低维的转化为高位后进行运算，或是将不同维数的匹配`
    + 广播规则
    + 变形数组关键词：**np.newaxis**
    + 广播的用处：
        - 归一化处理
        - 画出二维数组
            >   x=np.linspace(0,5,50)       
                y=np.linspace(0,5,50)[:, np.newaxis]        
                z=np.sin(x)**10+np.cos(10+y*x)*np.cos(x)        
                %matplotlib inline          
                import matplotlib.pyplot as plt         
                plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')      
                plt.colorbar(); 

6. 比较、掩码和布尔逻辑
    + `你想基于某些准则抽取、修改、计数或对一个数组中的值进行其他操作时，就可以使用掩码。例如统计数组中有多少个值大于某一给定值，或删除所有超出某些门限值的异常点`
    + 用比较运算符返回布尔数据类型的数组
    + 操作布尔数组：
        - 统计记录的个数
            + 使用**np.count_nonzero**(也可以用sum，sum的好处是可以沿着行或列进行)
            + > np.count_nonzero(x<6)  
            + 统计存在或所有用**any和all**，也可以沿着特定坐标轴
        - 布尔运算符 
            + &、|、^、~ 
    + 将布尔数组作为掩码
        - 将布尔数组作为索引：
        - > x[x<5]
        - **`and 和 or对整个对象执行单个布尔运算，&和| 对一个对象的内容（单个比特或者字节）执行多个布尔运算`**

7. 花哨的索引
+ 通过先设计特殊的索引数组，得到自己想要的索引
+ 同样可以对多为数组进行操作：
    - > row = np.array([0,1,2])       
        col = np.array([2,1,3])     
        X[row,col]
    - 如果将一个列向量和一个行向量组合在一个索引中，会得到一个二维结果
+ 示例：选择随机点
    - > mean = [0, 0]        
        cov = [[1, 2],               
        [2, 5]]        
        X = rand.multivariate_normal(mean, cov, 100)        
        X.shape
        %matplotlib inline        
        import matplotlib.pyplot as plt        
        import seaborn; seaborn.set()  # 设置绘图风格

        plt.scatter(X[:, 0], X[:, 1]);
    - > indices = np.random.choice(X.shape[0], 20, replace=False)        
        selection = X[indices]  # 花哨的索引        
        selection.shape
        plt.scatter(X[:, 0], X[:, 1], alpha=0.3)        
        plt.scatter(selection[:, 0], selection[:, 1], facecolor='none', edgecolor='b', s=200);
+ 利用索引修改值操作时注意重复
    - 错误结果：
        + > In[21]: i = [2, 3, 3, 4, 4, 4]        
                    x[i] += 1        
                    x
            Out[21]: array([ 6.,  0.,  1.,  1.,  1.,  0.,  0.,  0.,  0.,  0.]
    - 所以如果希望累加，可以使用at():
        + np.add.at(x,i,1) 
        + 也可以使用reduceat()实现数组中不同位置的reduce
            - np.add.reduceat(np.arange(8),[0,4,1,5,2,6,3,7])[::2] 
+ 示例：数据区间划分:***P148***
    - **`直接提供plt.hist()画出直方图`**
    - 有时候适合大数据集的不适合小数据集，所以要有自己编好的函数集

8. 数组的排序
+ numpy中的sort默认是快速排序$o(NlogN)$
    - argsort返回的是原始数组排好序的索引值
    - 可以通过axis参数沿着多维数组的行或者列排序，但同时会丧失行列间的关系
+ sort
    - 用axis确定多维方向
    - argsort显示索引
+ 使用np.partition找到数组中第K小的值,输出结果新数组，最左是需要的值
    - np.partition(x,3)
    - np.argpartition
    - 计算距离的快速方法:
        +  dist_sq = np.sum((X[:,np.newaxis,:] - X[np.newaxis,:,:]) ** 2, axis=-1)

9. 结构化数据：NumPy的结构化数组
+ 可以使用pandas中的DataFrame代替
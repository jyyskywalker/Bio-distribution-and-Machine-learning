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
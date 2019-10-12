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
    + 用dtype关键词设置数据类型
    + 可以指定为多维的
        > np.array([range(i,i+3) for i in [2,4,6]]) 
# Chapter 1: Ipython
## 帮助文档
1. 获取文档信息
   + help(len)
   + len?
   + 记得在自己写函数时添加一句
        > """Return the square of a."""
2. 获取源代码
+ 用'??': square??
+ 如果查询对象不是用python实现的，??在这种情况下等同于?后缀（这种情况很多）
3. Tab
+ 用Tab可以补全属性和方法:名称+.+Tab键
    - > L.\<TAB>
    - > L.cou\<TAB>
+ 通配符匹配
    - 用*来实现通配符匹配
    - *Warning?
    - str.\*find\*?


## 快捷键
## IPython命令
## 输入和输入历史获得

## IPython和shell命令
``在IPython终端可以直接执行shell命令，一行后任何在！之后的内容将通过系统命令行运行``
1. shell常用命令：
    - > echo pwd ls mkdir cd 
    - mv(移动文件): mv../myproject.txt ./ #这里将myproject.txt从上一级(../)移动到当前路径(./)
2. 将shell命令输入保存到一个python列表
    > contents=!ls
3. !cd无法使用，必须使用 %cd，事实上，也可以直接使用cd
   + 类似的还有%cat, %cp, %env, %ls, %man, %mkdir, %more, %mv, %pwd, %rm, %rmdir

# 代码的分析和计时
1. %timeit 和 %time
   + 其中%%timeit实现多行代码的运行
   + %timeit比%time要更快，%timeit避免了底层的一些时间
   + 但是对于必须只能算一次的代码，必须得用%time    
2. %prun用来分析整个脚本
    + 会显示整个代码运行时不同函数调用的时间，分析后可以考虑调整哪一块
3. line_profiler包专业分析代码
    + `但是安装需要visual c++14`
4. %memit 和 %mprun内存分析
    + %memit分析单个语句内存
    + 逐行分析要用%mprun，但是这个支队独立模块内部有用，所以要先创建模块
        - > %%file mprun_demo.py      
           ...      
           from mprun_demo import sum_of_lists     
           %mprun -f sum_of_lists sum of lists(1000000) 

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
   
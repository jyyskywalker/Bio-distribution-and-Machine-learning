# 第五课：python爬虫
## requests与bs4库

+ 基本爬虫命令
    >import requests           
    >text = requests.get("http://www.baidu.com", timeout=50)        
    >print(text.content)        
    >text_name = "./download/test.htm"      
    >with open(text_name, 'wb') as f:       
    >&emsp;&emsp;f.write(text.content)

+ 循环爬取
    >for i in range(1,500):     
        &emsp;&emsp;a="http://z.eflora.cn/frps/"+str(i)     
        &emsp;&emsp;text=requests.get(a)        
        &emsp;&emsp;text_name="./download/"+str(i)+".htm"       
        &emsp;&emsp;with open(text_name,'wb')as f:      
            &emsp;&emsp;&emsp;&emsp;f.write(text.content)       
+ 查询爬取文件中特定的字符
    - ./images+.png
+ 利用搜索引擎爬取
    - 爬取照片
    - **`作业`**:爬取校园植物的照片
    - csv格式保存，在notepad或其他里面保存，然后要保存为UTF-8
    - 用pandas库读取
        > TEST_PATH='./test.csv'        
            test_matrix =pandas.read_csv(TEST_PATH,header=0)        
            for index, row in test_matrix.iterrows():       
                        &emsp;&emsp;downloadImages=DownloadImages(str(row[0]),row[1],int(row[2]))       
                        &emsp;&emsp;downloadImages.start_download()
+ 专业植物网站"http://www.cfh.ac.cn/Spdb/spsearch.aspx"
    - 用ajax动态写的
    - 发现网址没有任何改变
    - 找到数据传输的网址
    - **`作业`**:
        + 将旧版网址换成新版
        + 如何不报错
        + 从专业网站上20种植物下载100张图片
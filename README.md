# spider_emoticon  
多进程爬虫试验，爬取一个表情包的站
## 依赖  
```python
pip36 install jieba
pip36 install requests
pip36 install lxml
```
## 部署  
a. 运行spider_run.py爬取指定图片  
> * PCNT参数：多进程爬取时启动的进程个数  
> * TCNT参数：多线程爬取时启动的线程个数  
> * SAVE_PATH参数：图片保存路径  
> * url_base参数：定义基础url路径  
> * URL_LIST参数：真正爬取时调用的url参数列表，通过修改range数量，来控制爬取的页数  

b. 运行query_run.py 查询指定关键词的图片
> * w1参数：图片的一级分类  
> * w2参数：图片的关键词，若w1下查询该关键词，总LIMIT未达到限制，则通过该关键词查询所有分类  
> * LIMIT参数：返回结果的总条数

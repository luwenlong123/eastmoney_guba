# eastmoney_guba
东方财富网的股吧信息爬虫
用来获取股吧的帖子信息，实现了全部沪深A股所有个股的帖子名、阅读量、回复量、作者获取
复制文件至python的包路径即可

em_get文件实现了爬虫函数的封装

em_spyder文件是通过em_get中的函数实现爬虫的示例

使用示例：
pl_df = get_guba(600000,1)
返回Dataframe结构类型数据，获取600000股吧第1页的阅读量、评论量、标题、作者、发布时间、更新时间

以000831做为爬取与分析示例
提供了000831的爬取结果的xlsx文件
爬取时间是按发帖时间排序，但缺少发帖的年份，再补充年份时，发现网站按发帖时间排序时会有BUG，2010年的老帖子乱入到了前端
后续有两个analysis文件是用于分析爬取的数据与行情的关系
做了简单分析

# 爬取堆糖网图片

使用`scrapy`爬取堆糖网的图片，并下载,拼凑成马赛克图

运行项目：
1.爬虫
```
scrapy crawl duitang
```
2.合成图片
```
python puzzle.py -i test.jpeg -d database/full/ -o output/
```

参考项目：
[https://github.com/NoisyWinds/puzzle](https://github.com/NoisyWinds/puzzle)
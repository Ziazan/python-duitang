import scrapy  
from scrapy.crawler import CrawlerProcess  
from scrapy.utils.project import get_project_settings  
process = CrawlerProcess(get_project_settings())
print(process)
process.crawl('duitang')  
process.start()
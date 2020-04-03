import scrapy
import json
from duitang.items import DuiTangItem


class DuiTangSpider(scrapy.Spider):
    name = 'duitang'
    #爬头像分类
    CATE_NAME = '头像'
    MAX_CATCH_PAGES = 4000
    limit = 100
    next_start = 3000
    allowed_domains = ['duitang.com']
    # 第一个请求会从start_urls发起
    start_urls = [
        "https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,sender,album,reply_count&limit=%s&filter_id=%s&start=%s&_=1585905865134" %(limit,CATE_NAME,next_start)
    ]
    item = DuiTangItem()
    def parse(self, response):
        res = json.loads(response.body_as_unicode())
        if(res['status'] == 1):
            data = res['data']
            self.item['url'] = 'www.duitang.com'
            self.next_start = data['next_start'] 
            if(self.next_start < self.MAX_CATCH_PAGES):
                url = "https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments,is_root,source_link,item,buyable,root_id,status,like_count,sender,album,reply_count&limit=%s&filter_id=%s&start=%s&_=1585905865134" %(self.limit,self.CATE_NAME,self.next_start)
                yield scrapy.Request(url, callback = self.parse)
            self.item['image_urls'] = []
            self.item['card_list'] = []
            for card in data['object_list']:
                self.item['image_urls'].append(card['photo']['path'])
                card['link'] = 'https://www.duitang.com/blog/?id=%s' %card['id']
                self.item['card_list'].append(card)
            yield self.item
        else:
            print('接口失败%s'%res.status)
    # def post_page(self,response):
    #     images_url = response.xpath("//div[@id='entry-content']//img/@src").extract()
    #     print('find %d images' % len(images_url))
    #     self.item['images'] = images_url
    #     return self.item
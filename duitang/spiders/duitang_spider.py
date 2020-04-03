import scrapy
import json
from duitang.items import DuiTangItem

class DuiTangSpider(scrapy.Spider):
    name = 'duitang'
    allowed_domains = ['duitang.com']
    # 第一个请求会从start_urls发起
    start_urls = [
        "https://www.duitang.com/napi/blog/list/by_filter_id/?include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Csender%2Calbum%2Creply_count&filter_id=%E5%AE%B6%E5%B1%85%E7%94%9F%E6%B4%BB&start=24&_=1585884865316"
    ]
    item = DuiTangItem()
    def parse(self, response):
        res = json.loads(response.body_as_unicode())
        if(res['status'] == 1):
            data = res['data']
            self.item['url'] = 'www.duitang.com'
            self.next_start = data['next_start']
            self.item['image_urls'] = []
            self.item['card_list'] = []
            for card in data['object_list']:
                self.item['image_urls'].append(card['photo']['path'])
                card['link'] = 'https://www.duitang.com/blog/?id=%s' %card['id'];
                self.item['card_list'].append(card)
            yield self.item
        else:
            print('接口失败%s'%res.status)
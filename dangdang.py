# -*- coding: utf-8 -*-
import scrapy
from dangdang_25.items import Dangdang25Item
from scrapy.http import Request
class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls=["http://category.dangdang.com/cp01.54.00.00.00.00.html"]
    def parse(self, response):
        grocery=Dangdang25Item()
        grocery["titl"]=response.xpath("//a[@class='pic']/@title").extract()
        grocery["link"]=response.xpath("//a[@class='pic']/@href").extract()
        grocery["comment"]=response.xpath("//a[@class='search_comment_num']/text()").extract()
        print("成功")
        yield grocery
        for i in range(2,10):
            urls="http://category.dangdang.com/pg"+str(i)+"-cp01.54.00.00.00.00.html"
            yield Request(urls,callback=self.parse)
if __name__=="__main__":
    pass

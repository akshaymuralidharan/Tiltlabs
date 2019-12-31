# -*- coding: utf-8 -*-
import scrapy
from ..items import FlipkartscrappingItem


class FlipkartSpiderSpider(scrapy.Spider):
    name = 'flipkart_spider'
    page_number = 2
    i = 0
    start_urls = ['https://www.flipkart.com/search?q=nokia+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=nokia+mobiles%7Cin+Mobiles&requestId=21894d77-18aa-4eb0-ad9d-4b78fd4d9b8f&as-searchtext=nokia&page=1']

    def parse(self, response):
        items = FlipkartscrappingItem()


        product_name = response.css('._3wU53n::text').extract()
        product_price = response.css('._2rQ-NK::text').extract()
        # product_image_link = response.css('._30XEf0::attr(src)').extract()
        product_image_link = "qwerty"
        # product_imagelink = response.xpath('//_30XEf0/@src').extract()

        # print("***************************")
        # print(product_name[1])
        # print(product_name)
        # print(product_image_link[1])
        # print("************************")

        for i in range(len(product_name)):
            items['product_name'] = product_name[i]
            items['product_price'] = product_price[i]
            items['product_image_link'] = product_image_link

            yield items



        next_page = 'https://www.flipkart.com/search?q=nokia+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_pr&otracker1=AS_QueryStore_OrganicAutoSuggest_0_5_na_na_pr&as-pos=0&as-type=RECENT&suggestionId=nokia+mobiles%7Cin+Mobiles&requestId=21894d77-18aa-4eb0-ad9d-4b78fd4d9b8f&as-searchtext=nokia&page='+ str(FlipkartSpiderSpider.page_number) +''
        if FlipkartSpiderSpider.page_number <= 8:
            FlipkartSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)




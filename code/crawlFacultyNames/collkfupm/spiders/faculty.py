# -*- coding: utf-8 -*-
import scrapy
import logging


class FacultySpider(scrapy.Spider):
    name = 'faculty'
    allowed_domains = ['faculty.kfupm.edu.sa/web/general']
    start_urls = ['https://faculty.kfupm.edu.sa/web/general/facultybydep.aspx']

    def parse(self, response):
        #title = response.xpath("//b/text()").get
        #faculty = response.xpath("//td/font/a/text()").getall()
        faculty = response.xpath("//td/a")
        for department in faculty:
            dept = department.xpath(".//text()").get()
            link = department.xpath(".//@href").get()
       
        #absolute_url = f"https://faculty.kfupm.edu.sa/web/general/facultybydep.aspx{link}"
        #absolute_url = response.urljoin(link)


        yield response.follow(url=link, callback=self.parse_department)
        #yield response.follow(url=link)
        #yield scrapy.Request(url=absolute_url)


    

    def parse_department(self, response):
        #logging.info(response.url)
        rows = response.xpath("//td[@class= 'f4']/text()").get()
       
        yiled {
            'rows': rows
        }

        




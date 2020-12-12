# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['faculty.kfupm.edu.sa/web/general']
    start_urls = ['https://faculty.kfupm.edu.sa/web/general/facultybydep.aspx']
    
    def parse(self, response):
        faculty = response.xpath("//td/a")
        for dept in cfaculty:
            name = dept.xpath(".//text()").get()
            link = dept.xpath(".//@href").get()

            # absolute_url = f"https://www.worldometers.info{link}"
            # absolute_url = response.urljoin(link)

            yield response.follow(url=link, callback=self.parse_dept, meta={'dept_name': name})
    
    def parse_dept(self, response):
        name = response.request.meta['dept_name']
        rows = response.xpath("//td[@class= 'f4']")
        for row in rows:
            row.xpath(".//td[1]/text()").get()
            
            yield {
                'dept_name': name,
                
            }

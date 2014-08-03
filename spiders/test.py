from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from Supreme.items import Supreme

class MySpider(BaseSpider):
  name = "Supreme"
  allowed_domains = ["hypebeast.com"]
  start_urls = ["http://www.hypebeast.com"]

  def parse(self, response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select("//span[@class='pl']")
      items = []
      for titles in titles:
          item = Supreme()
          item ["title"] = titles.select("a/@title()").extract()
          item ["link"] = titles.select("a/@href").extract()
          items.append(item)
      return items

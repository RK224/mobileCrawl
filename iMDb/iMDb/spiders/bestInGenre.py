import scrapy

class bestInGenre(scrapy.Spider):
	name = "bestInGenre"
	start_urls = ["https://www.imdb.com/feature/genre/?ref_=nv_ch_gr_3"]

	def parse(self,response):
		for genreLink in response.css("div.image a::attr(href)").extract():
			url = response.urljoin(genreLink)
			yield scrapy.Request(url,callback = self.parseGenre)

	def parseGenre(self,response):
		heading = response.css("div.article h1::text").extract_first()
		yield heading
		for row in response.css('div.lister-item'):
			yield{
				'Name': row.css('h3.lister-item-header a::text').extract_first(),
				'Year': row.css("h3.lister-item-header span.lister-item-year::text").extract_first(),
				'Description': row.css("div.lister-item-content p.text-muted::text").extract()
				
			}
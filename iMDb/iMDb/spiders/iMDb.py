import scrapy

class iMDbSpider(scrapy.Spider):
	name = "iMDb"
	start_urls=["https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250_3"]

	def parse(self,response):
		i = 1
		for show in response.css("tbody tr"):
			yield {
				"rank" : i,
				'title' : show.css(".titleColumn a::text").extract_first(),
				'year':	show.css(".titleColumn span.secondaryInfo::text").extract_first(),
				'iMDb rating': show.css(".imdbRating strong::text").extract_first(),
			}
			i = i+1
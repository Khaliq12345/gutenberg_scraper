import scrapy


class GetbooksSpider(scrapy.Spider):
    name = 'getBook'
    allowed_domains = ['www.gutenberg.org']
    start_urls = ['https://www.gutenberg.org/browse/recent/last7']

    def parse(self, response):
        allBooks = response.css('.pgdbetext')
        for bookLink in allBooks:
            yield response.follow('https://www.gutenberg.org' + bookLink.css('.pgdbetext a::attr(href)').get(),
            callback = self.getBookData)

    def getBookData(self, response):
        yield {
            'author' : response.css('a[rel="marcrel:aut"]::text').get(),
            'illustrator' : response.css('a[rel="marcrel:ill"]::text').get(),
            'Loc No' : response.css('a.external::text').get(),
            'Loc link' : response.css('a.external::attr(href)').get(),
            'title' : response.css('[itemprop="headline"]::text').get(),
            'languague' : response.css('[property="dcterms:language"] td::text').get(),
            'Loc class' : response.css('[datatype="dcterms:LCC"] td a::text').get(),
            'Loc class link' : 'https://www.gutenberg.org' + response.css('[datatype="dcterms:LCC"] td a::attr(href)').get(),
            'subject' : response.css('[datatype="dcterms:LCSH"] a::text').get(),
            'subject link' : 'https://www.gutenberg.org' + response.css('[datatype="dcterms:LCSH"] a::attr(href)').get(),
            'category' : response.css('[datatype="dcterms:DCMIType"]::text').get(),
            'release date' : response.css('[itemprop="datePublished"]::text').get(),
            'copyright' : response.css('[property="dcterms:rights"]::text').get(),
            'downloads' : response.css('[itemprop="interactionCount"]::text').get(),
        }


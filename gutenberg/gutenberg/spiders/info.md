# CSS selectors

allBooks = response.css('.pgdbetext')
link = 'https://www.gutenberg.org' + response.css('.pgdbetext a::attr(href)').get()

author = response.css('a[rel="marcrel:aut"]::text').get().strip()
illustrator = response.css('a[rel="marcrel:ill"]::text').get().strip()
Loc No = response.css('a.external::text').get().strip()
Loc link = response.css('a.external::attr(href)').get().strip()
title = response.css('[itemprop="headline"]::text').get().strip()
languague = response.css('[property="dcterms:language"] td::text').get().strip()
Loc class = response.css('[datatype="dcterms:LCC"] td a::text').get().strip()
Loc class link = 'https://www.gutenberg.org' + response.css('[datatype="dcterms:LCC"] td a::attr(href)').get().strip()
subject = response.css('[datatype="dcterms:LCSH"] a::text').get().strip()
subject link = 'https://www.gutenberg.org' + response.css('[datatype="dcterms:LCSH"] a::attr(href)').get().strip()
category = response.css('[datatype="dcterms:DCMIType"]::text').get().strip()
release date = response.css('[itemprop="datePublished"]::text').get().strip()
copyright = response.css('[property="dcterms:rights"]::text').get().strip()
downloads = response.css('[itemprop="interactionCount"]::text').get().strip()

import lxml.html as lh

doc=lh.parse('1237732688247222')


div=doc.xpath('./body/div/div/div/div/div/div/div/div[@id="artigos-completos"]')[0]

artigos = (div.find_class('artigo-completo'))

numArtigos = (len(artigos))

i = 0

while(i < numArtigos):
	div2=doc.xpath('./body/div/div/div/div/div/div/div/div/div[@class="artigo-completo"]')[i]
	print(div2.text_content())
	i = i + 1





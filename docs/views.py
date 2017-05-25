from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template.context_processors import request
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import lxml.html as lh
import json
import re
from listaProfes import *
from baixaLattes import *


def index(request):
    return render_pagina(request, 'docs.html', None)

@csrf_exempt 
def inf(request):
    c = geradict()
    return render_pagina(request, 'inf.html', c)

def render_pagina(request, destino, c):
    return render(request, destino, c)


@csrf_exempt 
def professor(request):
	cvPath = './docs/CVs/'
        request_body = json.loads(request.body)
	idLattes = request_body['id']
	cvPath += idLattes

	if os.path.exists(cvPath):
		arquivoH = open(cvPath)
		cvLattesHTML = arquivoH.read()
		
	else:
		cvLattesHTML = baixaCVLattes(idLattes)
		file = open(cvPath, 'w')
		file.write(cvLattesHTML)
		file.close()


	response = {}
	return HttpResponse(response, content_type="application/json")
@csrf_exempt 
def geraResp(request):
	cvPath = './docs/CVs/'
        request_body = json.loads(request.body)
	idLattes = request_body['id']
	cvPath += idLattes
	doc=lh.parse(cvPath)
	div=doc.xpath('./body/div/div/div/div/div/div/div/div[@id="artigos-completos"]')[0]
	artigos = (div.find_class('artigo-completo'))
	numArtigos = (len(artigos))
	i = 0
	artigosString = ''
	artigosString += '<div style="text-align:left"><font size="4">'
	while(i < numArtigos):
		div2=doc.xpath('./body/div/div/div/div/div/div/div/div/div[@class="artigo-completo"]')[i]
		for elem in div2:
			artigosString+= elem.text_content().replace('\n','') 
			
	
		artigosString+= '<br><a class="icone-producao icone-doi" href="' 
		try:artigosString+= elem.xpath('//a[contains(@href,"doi")]/@href')[i] 
		except: pass
		artigosString+= '" target="_blank">view</a>		'
		artigosString += '<br><br>'
		i+=1
	
	artigosString+='</font></div>'
	artigosString+='<a class="w3-btn-floating w3-hover-green" href=""><</a>'
	
	
	return HttpResponse(artigosString, content_type="application/json")

def geradict():
    c = {
	'DIC' : INF
    }
    return c


@csrf_exempt 
def geraDisplayDict(request):
    request_body = json.loads(request.body)
    string = request_body['string']

    dic = geradict()['DIC']
    dicPorKey = {k:v for k,v in dic.iteritems() if re.match(string, k, re.I)}	
    dicPorValue ={}
    for k in dic:
	for v in dic[k]:
	    if v == 'nome':
	        for word in dic[k][v].split(' '):
		    if re.match(string, word, re.I):
		        dicPorValue.update({k: dic[k]})
	    elif re.match(string, dic[k][v], re.I):
	        dicPorValue.update({k: dic[k]})
	    
		
    dicSearch = dict(dicPorKey.items() + dicPorValue.items())
    



    displayHtml = geraDisplayHTML(dicSearch)

    if not displayHtml:
	displayHtml = "Sem resultados para '"+string+"'."
	
	
	
    response = {
	'displayHtml': displayHtml,
    }
    return HttpResponse(displayHtml, content_type="application/json")


def geraDisplayHTML(dic):
	displayFinal = ''
	for key, value in dic.items():
		display = '<div class="w3-quarter w3-center w3-hover-opacity">'
		display+= '<a id="'
		display+= value['idLattes'] 
		display+= '" class="profe" onclick="profe(this);">'
		display+= '<img src="' + value['pic'] + '" style="height:200px" >'
		display+= '<h3>' +  key + '</h3>'
		display+= '<h5>' + value['nome'] + '</h5>'
		display+= '<p>' + value['idLattes'] + '</p>'
		display+= '</a></div>'
		displayFinal += display
	return displayFinal

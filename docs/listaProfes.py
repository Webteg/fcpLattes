from django.conf import settings
from django.conf.urls.static import static
import os
import Image
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'listaProfes.txt')
file_path_pic = os.path.join(module_dir, 'static/images/picsProfes/')

pathPic = '/static/images/picsProfes/'

INF = {
	'oliveira':{
		'nome':'Manuel Menezes de Oliveira Neto',
		'idLattes':'3083628377406351',
		'pic':pathPic+'oliveira.jpg'
	},
	'avillavicencio':{
		'nome':'Aline Villavicencio',
		'idLattes': '4849566723209094',
		'pic': pathPic+'avillavicencio.png'
	},
	'lmduarte':{
		'nome':'Lucio Mauro Duarte',	
		'idLattes': '6137513161750332',
		'pic': pathPic+'lmduarte.jpg'
	},
	'calisboa':{
		'nome':'Carlos Arthur Lang Lisboa',	
		'idLattes':'3358821967712943',
		'pic': pathPic+'calisboa.jpg'
	},	
}

fo = open(file_path, 'r')
dic = INF
op=1
for line in fo:	
	if line.strip():
		ine = line.replace('\t','')
		line = line.replace('\n','')
		if op==1:
			nome = line
			op = 2
			continue
		if op==2:
			idInf = line
			idInf = idInf.replace('\t','')
			dic.update({line: {'nome':nome} })
			op = 3
			continue
		if op==3:
			dic[idInf].update({'idLattes':line})
			
			op = 1
			
			path = file_path_pic + idInf + '.jpg'
			try:
				Image.open(path)
				pathImg = pathPic + idInf + '.jpg'
				
			except:	pathImg = pathPic + idInf + '.png'

			dic[idInf].update({'pic':pathImg})
			continue




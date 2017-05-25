pathPic = '/static/images/picsProfes/'

fo = open('listaProfes.txt', 'r')
dic = {}
op=1
for line in fo:	
	if line.strip():
		ine = line.replace('\t','')
		line = line.replace('\n','')
		if op==1:
			nome = line
			op = 2
			print nome
			continue
		if op==2:
			dic.update({line: {'nome':nome} })
			idInf = line
			print dic
			op = 3
			continue
		if op==3:
			dic[idInf].update({'id':line})
			op = 1
			try: dic[idInf].update({'pic':pathPic + idInf + '.jpg'})
			except: dic[idInf].update({'pic':pathPic + idInf + '.png'})
			continue
		

	

	



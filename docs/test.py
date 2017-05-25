from baixaLattes import *
from listaProfes import *
from pyavltree import *
#from parserLattes import *

cvPath = './CVs/4849566723209094'

if os.path.exists(cvPath):
	arquivoH = open(cvPath)
	cvLattesHTML = arquivoH.read()
	print "(*) Utilizando CV armazenado no cache: "+cvPath
else:
	cvLattesHTML = baixaCVLattes('4849566723209094')
	file = open(cvPath, 'w')
	file.write(cvLattesHTML)
	file.close()
	print " (*) O CV esta sendo armazenado no Cache"
cvLattesHTML  = cvLattesHTML.decode('iso-8859-1', errors='ignore')

#avl = AVLTree(INF)





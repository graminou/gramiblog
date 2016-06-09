# coding: utf-8
import glob
from classes import *
from navbar import barreNavigation

##le principal
if __name__ == '__main__':
 
    #construction des articles
    liste = []
    
    for file in glob.glob('contenu/*json'):
        article = Article(file)
        liste.append(article)
   
    #récupérer la liste des menus et contruire la barre de navigation
    menus = [a.menu for a in liste]
    navbar = barreNavigation(menus)

    #construire les pages html : HEAD + NAVBAR + BODY + FOOTER
    for article in liste :
        article.generateHtml(navbar)



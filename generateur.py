# coding: utf-8
import glob
from classes import *

##def menusList(liste):
##    '''constructeur de la liste des menus'''
##    return set([a.menu.replace(', ', '/')+'/' for a in liste])

def navbarPremierNiveau(liste):
	'''Génère les titres de menu de premier niveau'''
	return set([m["1"] for m in liste])

def navbarParMot(liste, mot):
        '''retourne la liste des sous menus d'un menu donné'''
        l=[]
        for m in liste:
            if mot in m.values():
                l.append(list(m.values()))
        return list(filter(None, l))

     
def premierNiveau(liste):
    nav = ''
    for m in navbarPremierNiveau(liste):
        nav = nav+'<li>'+m+'</li>'
    return '<ul>'+nav+'</ul>'


def insertSubmenu(liste, mot):
    t = [elt[1] for elt in navbarParMot(liste, mot) if len(elt)>1]
    n= premierNiveau(liste)
    if t==[]:
        return n
    else:
        n= n.partition(mot)
        nav = n[0]+n[1]+'<ul>'
        for e in t:
            nav=nav+'<li>'+e+'</li>'
        return nav+'</ul>'+n[2]


##le principal
if __name__ == '__main__':

    #construction des articles.html et de leur liste
    liste = []
    
    for file in glob.glob('contenu/*json'):
        article = Article()
        article.parseFromJson(file)
        article.generateHtml()
        liste.append(article)
       
    #récupérer la liste des menus
    menus = [a.menu for a in liste]
    
    #récupérer la profondeur maximale des menus
    n = max([max(m.keys()) for m in menus])

    # construire la navbar Niveau 1

    #pour chaque élément de navbar, insérer, s'ils existent, les menus de niveau suivant

    # reboucler autant de fois que n.
    
    #construction de la navbar
##    categories, menus = [], menusList(liste)
##
##    for m in menus:
##        cat = Category()
##        cat.getMenu(m)
##        print (cat.menu)
    
##        print('Titre de mon article : ', article.title)
##        print('Chemin de mon article : ', article.slug)
##        print('Menu de mon article : ', article.menu)
##        print('Date de mon article : ', article.date)
##        print('Auteur de mon article : ', article.author)
##        print("le slug : ", article.slug)
##        print('Résumé : ', article.abstract)
##        print('Mots clé : ', article.tags)
##        print('Corps html de mon article :', article.body)
    print(n)
    print(menus)
    for mot in navbarPremierNiveau(menus):
        print(insertSubmenu(menus, mot))

##        print('Metadonnees du fichier : ', article.createHead())

    

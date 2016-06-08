# coding: utf-8
##les classes
from os.path import join
import json
from settings import *


class Article():
    '''classe des articles construits à partir des fichiers json rédigés'''
    def __init__(self):
        self.title = ''
        self.slug = ''
        self.menu = ''
        self.date = ''
        self.author = ''
        self.abstract = '' 
        self.tags = ''
        self.body = ''

    def parseFromJson(self, article):
        '''ouvre le fichier, le parse et construit l'objet article correspondant'''
        with open(article) as a:
            f = json.load(a)
            self.title = f["title"]
            self.slug = f["slug"]
            self.menu = f["menu"]
            self.date = f["date"]
            self.author = f["author"]
            self.abstract = f["abstract"]
            self.tags = f["tags"]
            self.body = f["body"]

    def giveUrl(self):
        '''retourne l'url racine+arbo du menu+slug'''
        # return RACINE + '/'.join(self.menu.split('-')) + '/' + self.slug
        pass

    def createHead(self):
        '''crée les métadonnées du head'''
        title = '<title>'+self.title+'</title>'
        keywords = '<meta name="keywords" content="'+self.tags+'">'
        description = '<meta name="description" content="'+self.abstract+'">'
        author = '<meta name="author" content="'+self.author+'">'
        return title+keywords+description+author
    
    def generateHtml(self):
        '''crée le html de l'article dans out/'''
        with open(join('out/', (self.slug+'.html')), 'w') as f:
            f.write(HTML[0]+self.createHead()+HTML[1]+self.body+HTML[2])


class Category():
    '''classe des pages d'accueil des menus, construites à partir des fichiers json rédigés'''
    def __init__(self):
        self.menu = ''
        self.submenus = []
        # self.abstract = '' 
        self.articles = []
        
    def getMenu(self, menu):
        '''renvoie menu à partir de la liste menus'''
        #self.menu = menu
        pass

    def getSubmenus(self, liste):
        '''récupère la liste des sous menus de ce menu en parsant la liste des articles'''




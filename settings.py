# coding: utf-8

RACINE = 'http://www.devetdadam.fr/'

## Le template base
HTML = [
    #0 - début du fichier
    '<!doctype html><html lang="fr"><head><meta charset="utf-8"><head><meta charset="utf-8">', 
    #1 après title et les metas keywords,description et author
    '<link href="http://fonts.googleapis.com/css?family=Roboto+Condensed|Open+Sans:400,300,700|Yesteryear" rel="stylesheet" type="text/css" /><link href="./assets/css/style.css" rel="stylesheet" type="text/css" media="screen" /></head><body><div id="menu-wrapper"><div id="menu">',
    #2 après la navbar
    '</div></div><div id="header-wrapper"><div id="header"><div id="logo"><h1><a href="#">Forthright</h1></div></div></div><div id="wrapper"><div id="page"><div id="page-bgtop"><div id="page-bgbtm"><div id="content">',
    #3 après le post
    '</div><div style="clear: both;">&nbsp;</div></div></div></div></div><div id="footer"><p>&copy; 2016 | DEV &amp; d\'Adam, le blog !</p></div></body></html>',
]


## Le template du bloc article
ARTICLE = [
    #0
    '<div class="post"><h2 class="title">',
    #1 après le titre article.title
    '<p class="meta"><span class="date">May 10, 2013</span><span class="posted">Posté par ',
    #2après l'auteur article.author
    '</span></p><div style="clear: both;">&nbsp;</div><div class="entry">',
    #3 après le body de l'article article.body
    '</div></div>',
    ]

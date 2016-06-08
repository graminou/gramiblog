#*Attention : en cours de construction - le générateur ne fonctionne pas encore*

# gramiblog
Un script Python pour créer et gérer mon blog perso

##Utilisation
- chaque article/page est un fichier json stocké dans contenu/ 
- lancer la commande : ```$python generateur.py```
- le site complet est stocké dans out/
- il suffit alors de transférer les fichiers sur votre hébergement (automatisation prévue)

##Fonctionnement
###Structure des .json
Les articles et pages du blog sont enregistrées comme fichiers .json de la structure suivante :
```{
	"title": "Construire un générateur de site statique - Part 2",
	"slug": "construire-un-generateur-de-site-statique-part-2",
	"menu": "Python, Scripting",
	"date": "2016-05-17",
	"author": "Jean-Marc LEGRAND - DEV & d'Adam",
	"tags": "script, générateur, python, site statique, html, css",
	"abstract": "La seconde parftie de mon tuto",
	"body": "<h1>Maintenant, on rendre dans le dur !</h1><p>C'est la seconde partie de mon super tuto.</p>"
}
```

###La barre de navigation
*to be documented*
###Le template
*to be documented*

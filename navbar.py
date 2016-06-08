def menuBase(liste):
    '''
    Retourne la liste des menus de premier niveau.
    Exemples :
    >>> liste = ['Python, Scripting', 'Python, Django', 'Lilypond', 'Culture, Livres, Romans', 'Culture, Livres, Romans', 'Culture, Livres, Policiers', 'Culture, Films, Action', 'Python, Scripting', 'Humeurs, Politique, Loi Travail, Nuit Debout']
    >>>menuBase(liste)
    <ul><li>Culture</li><li>Humeurs</li><li>Lilypond</li><li>Python</li></ul>
    >>>liste = []
    >>>menuBase(liste)
    <ul><li></li></ul>
    '''
    m=sorted(set([e.split(',')[0] for e in liste]))
    return ('<ul><li>'+str.join('</li><li>', m)+'</li></ul>', m)


def deepness(liste):
    '''
    Retourne la profondeur des menus de la liste.
    La prodondeur est le nombre maximal d'éléments séparés par une virgule dans la liste.
    Exemples:
    >>> liste = ['Python, Django', 'Lilypond', 'Culture, Livres, Romans']
    >>> deepness(liste)
    3
    >>> liste = ['Lilypond']
    >>> deepness(liste)
    1
    >>> liste=[]
    >>> deepness(liste)
    0
    '''
    if liste!=[]:
        return max([len(e.split(',')) for e in liste])
    else:
        return 0


def menuChild(mot, liste):
    '''
    Retourne un string html contenant les sous menus d'un élément mot de la liste.
    S'il n'y en a pas ou si la liste est vide, retourne un string vide.
    Si le mot n'est pas dans la liste, ou si le mot est '', retourne un string vide.
    Exemples:
    >>> liste = ['Python, Django', 'Python, Scripting','Lilypond']
    >>> menuChild('Python', liste)
    '<ul><li>Django</li><li>Scripting</li></ul>'
    >>> menuChild('Lilypond', liste)
    ''
    >>> liste = []
    >>> menuChild('Python', liste)
    ''
    >>> liste = ['Python, Django', 'Python, Scripting','Lilypond']
    >>> menuChild('Livres', liste)
    ''
    >>> liste = ['Python, Django', 'Python, Scripting','Lilypond']
    >>> menuChild('', liste)
    ''    
    '''
    if mot=='':
        return ''
    else:
        c=[]
        for e in liste:
            if mot in e:
                m=e.split(', ')
                if len(m)>m.index(mot)+1:
                    c.append(m[m.index(mot)+1])
        if c != []:
            return ('<ul><li>'+str.join('</li><li>', sorted(set(c)))+'</li></ul>', c)
        else:
            return ('', c)



def barreNavigation(liste):
    '''
    Retourne la navbar html d'une liste de menus issus des json du contenu
    Exemple:
    >>>menus = ['Python, Scripting', 'Python, Django', 'Lilypond', 'Culture, Livres, Romans', 'Culture, Livres, Romans',
    'Culture, Livres, Policiers', 'Culture, Films, Action', 'Humeurs, Politique, Loi Travail, Nuit Debout',
    'Culture, Films, Action, Navets', 'Culture, Livres, Romans, Culte'
    ]
    >>>barreNavigation(menus)
    <ul>
      <li>Culture
        <ul>
          <li>Films
            <ul>
              <li>Action
                <ul><li>Navets</li></ul>
              </li>
            </ul>
          </li>
          <li>Livres
            <ul>
              <li>Policiers</li>
              <li>Romans
                <ul><li>Culte</li></ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
      <li>Humeurs
        <ul>
          <li>Politique
            <ul>
              <li>Loi Travail
                <ul><li>Nuit Debout</li></ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
      <li>Lilypond</li>
      <li>Python
        <ul>
          <li>Django</li>
          <li>Scripting</li>
        </ul>
      </li>
    </ul>
    '''
    n=deepness(menus)
    mb = menuBase(menus)

    navbar = mb[0]
    done = mb[1]

    for i in range(n+1):
        for mot in done:
            m = menuChild(mot, menus)
            navbar = navbar.partition(mot)[0] + navbar.partition(mot)[1] + m[0] + navbar.partition(mot)[2]
            for elt in m[1]:
                if elt not in done:
                    done.append(elt)
            done = sorted(set([e for e in done if e != mot]))
    return navbar

    
    

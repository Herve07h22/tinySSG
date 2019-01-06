---
titre: Les variables par défaut
author: Herve
description: Tiny SSG génère un fichier HTML par fichier markDown. Il met à disposition des variables utilisables dans les fichiers template.
layout: Post
---

Tiny SSG génère un fichier HTML par fichier markDown. Il met à disposition des variables utilisables dans les fichiers template, en complément de celles mentionnées dans le [front-matter](frontmatter.html).


### site

La variable `site` est la liste de toutes les pages du site.
Elle est utile pour afficher une liste de posts. Par exemple, pour affiche la liste de toutes les pages dont le template est `Post`, on peut écrire :

```
{% for page_item in site if page_item.layout=="Post" %}
    <h1> {{ page_item.titre }} <h1>
    <p> {{ page_item.content | safe }}
{% endfor %}
```

### page

La variable `page` est la page courante qui est en cours d'affichage.
On accède à ses variables prédéfinies ou définies dans le front-matter ainsi :

```
<!-- Affichage de l'url de la page et de son titre -->
<a href ="{{ page.slug }}"> {{ page.titre}} </a>
```

### slug

La variable `page` est l'URL de la page statique. Elle correspond au nom du répertoire dans lequel se situe le fichier md. 

### content

La variable `content` est le contenu du fichier MarkDown transformé en HTML. 

```
<!-- Affichage du contenu de la page : le HTML construit à partir du MarkDown -->
<!-- Le filtre "safe" indique que le HTML généré est sûr                      -->

{{ page.content | safe }}

```

### id

La variable `id` est Le nom du fichier MarkDown sans l'extension `.md`.

### createdDate

La variable `createdDate` est est la date (système) de dernière modification du fichier MarkDown.
Elle est au format numérique. Elle donne une date exprimée en nombre de secondes écoulées depuis *l'heure 0*. Sur UNIX, l'heure 0 est 01/01/1970.
Cette valeur numérique est intéressante pour ordonner une liste d'articles, du plus récent au plus ancien par exemple :

```
{% for page_item in site|sort(attribute='createdDate', reverse=True) if page_item.layout=="Post" %}
```

### createdDateTxt

La variable `createdDateTxt` est la date `createdDate` au format texte : jour mois (en 3 lettres) et années.
Ce format est modifiable dans le fichier ssg.py :

```
self.createdDate = strftime("%d %b %Y", gmtime(getmtime(md_file)))
```

### Les images

Tous les sous-répertoires voisins du fichier MarkDown sont réputés contenir des images.
Chaque sous-répertoire créera une variable comportant la liste des images du sous répertoire.

Par exemple, la struture de fichier ci-dessous :

```
myPage
  |--- text.md
  |--- carousel
  |      |--- image1.jpg
  |      |--- image2.jpg
  |      |--- image3.jpg
  |--- gallery
         |--- gal1.jpg
         |--- gal2.jpg
```

TinySSG va mettre à disposition 2 variables : 

- `carousel` qui sera une liste de 3 images (`image1.jpg`, `image2.jpg`, `image3.jpg`), et
- `gallery` qui sera une liste de 2 images (`gal1.jpg`, `gal2.jpg`).

Pour les utiliser dans le fichier template, on invoquera :

```
{% for im in page.gallery %}
    <!-- use lazy loading -->
    <img class="lozad" src="blur/{{im}}"  data-src="original/{{im}}">
{% endfor %}
```


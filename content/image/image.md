---
titre: La gestion des images
author: Herve
description: Tiny SSG repère automatiquement les fichiers image au format jpg et png. Il sait les redimensionner et pré-calculer les rendus pour le lazy loading
layout: Post
---

Dans les CMS, il est fréquent de passer du temps sur la gestion des images. En effet, il faut parfois :

- charger les images d'origine dans le CMS,
- établir une copie re-dimensionnée des images, pour afficher des vignettes ou des aperçus,
- les rogner pour homogénéiser leurs tailles,
- mettre un place un système de chargement différé "à la demande" (lazy-loading) pour éviter que la page ne soit trop longue à charger, notamment sur un smartphone.

Pour le lazy-loading, un challenge supplémentaire concerne la réservation de l'encombrement de l'image dans l'attente de son chargement, pour éviter la désagréable réorganisation automatique des éléments de la page.

Confronté à ces différents challenges lors de la refonte d'un site vitrine comportant plus de 300 images, j'ai donc doté tinySSG de quelques fonctions utiles au pré-traitement des images.

### Stocker les images au bon endroit

Pour conserver une bibliothèque d'image bien organisée, il est préférable de structurer le contenu du site de la façcon suivante :

```
content
 |
 |-page1
 |  |--- text.md
 |  |--- carousel
 |  |      |--- image1.jpg
 |  |      |--- image2.jpg
 |  |      |--- image3.jpg
 |  |--- gallery
 |          |--- gal1.jpg
 |          |--- gal2.jpg
 |-page2
 |  |--- anothertext.md
 |  |--- carousel
 |  |      |--- image4.jpg
 |  |      |--- image5.jpg
 |  |      |--- image6.jpg
 |  |--- gallery
 |          |--- gal3.jpg
 |          |--- gal4.jpg
```

Chaque page du blog est un répertoire, comportant 
- un seul fichier Markdown avec l'extension `.md`. C'est lui qui déclenche la génération d'une page HTML.
- zéro, un ou plusieurs sous répertoire comportant les images originales.

### Le lazy loading

Pour lancer la génération du site, on écrit :

Cela conduira à la cration par défaut de 2 sous répertoires dans le répertoire de destination `dist` :

- un sous-répertoire `original` comportant une copie des fichiers d'origine (non modifiés)
- un sous-répertoire `blur` comportant des fichiers unifiés : de même dimension que le fichier original, mais avec un fond uni de la couleur dominante du fichier d'origine. 

Les images du sous-répertoire `blur` sont beaucoup plus légères que celles d'origine, mais elles ont une dimension équivalente. 
Cela permet d'appliquer le lazy-loading, en commençant à charger les images légères, en attendant d'avoir chargé les images d'origine lorsqu'on en a besoin.

### Les images sur-mesure

Dans certains cas, on a besoin d'images redimensionnées à une taille prédéfinies.
Pour les générer, il suffit d'invoquer la commande `addImageProcessing` :

```python
# Fichier main.py
mon_site.addImageProcessing( label='square', x=400, y=400  )
```

Ceci va créer un sous répertoire `square` dans le répertoire de destination comportant toutes les images du site redimensionnées à la taille de 400x400px.

### Du rectangle au carré

Dans l'exemple ci-dessus, rien ne garantie que l'image d'origine soit carrée. Si elle est rectangle, au format 1200x800 par exemple :

* tinySSG va commencer par la rogner pour avoir le ratio attendu. Sur notre exemple, une sous image de taille 800x800 px sera extraite d'une zone centrale. Les deux bandes latérales d'une largeur de 200 px seront donc perdues. L'image d'origine n'est pas modifiée, on travaille bien sur une copie.
* Après l'obtention d'une image de 800x800 au ratio désiré, une réduction de taille à 400x400 est réalisée.










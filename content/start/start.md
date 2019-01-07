---
titre: Bien débuter avec TinySSG
author: Herve
description: Tiny SSG est un générateur de site statique développé en Python. Ses points forts sont la gestion des images et la facilité d'écriture des layouts au format Jinja2.
layout: Post
---

### Installation

Pour démarrer, le plus rapide est de cloner le dépôt git.

```
git clone https://github.com/Herve07h22/tinySSG.git
```

Ensuite, installer les dépendances dans un environnement dédié.

```
cd tinySSG
python -m venv tinyenv
./tinyenv/Script/activate
pip install -r requirements.txt
```

*NB : tinySSG a été testé sur la version 3.6.6 de python.*   

Générer l'exemple et vérifier que tout fonctionne.

```
python main.py
```

Cela doit conduite à la création d'un répertoire `dist` comportant la totalité du site statique.

### Editer le contenu

Le plus simple est de coller à la structure suivante dans le répertoire `content` :

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

Lors du lancement de la génération du site :

* chaque fichier MarkDown au format `.md` déclenchera la génération d'une page sous la forme d'un fichier HTML dans le répertoire de destination
* chaque sous répertoire voisin comportant des images sera rattaché à cette page. Chaque image sera copiée dans le répertoire de destination, dans le sous-répertoire `original`. 

### Créer les templates

Les fichiers dans le répertoire `templates` permettent de décrire la façon dont les pages HTML seront générées à chaque fois qu'un fichier MarkDown sera analysé.
Le nom du fichier template à utiliser doit être spécifié dans [l'entête](frontmatter.html) du fichier MarkDown.
Le fichier template doit être au format HTML, en y incluant des directives [Jinja2](http://jinja.pocoo.org/docs/2.10/).
Les directives utilisent les [variables de la page](variables.html) pour générer le contenu.  

### Lancer la génération

La génération du site statique est réalisée par le script `main.py`.

```
# -*- coding: utf-8 -*-

from ssg.ssg import ssg
from os.path import join
from os import getcwd

if __name__ =='__main__':
    
    # Create instance of ssg class. Pass the content dir to the constructor.
    mon_site = ssg(contentDir=join(getcwd(), "content"))
    
    # Copy the assets to the destination dir
    mon_site.renderAssets( assetDir=join(getcwd(), "assets") , destination_dir=join(getcwd(), "dist") )
    
    # render the site
    mon_site.render( template_dir=join(getcwd(), "templates") , destination_dir=join(getcwd(), "dist") )
```

On spécifie :

* l'emplacement du répertoire contenant les fichiers MarkDown et les images (`ContentDir`),
* l'emplacement du répertoire contenant les fichiers css, jss et autres nécessaires à l'affiche du site (`assetDir`). Tous les fichiers du répertoire seront simplement recopiés dans le répertoire de destination,
* l'emplacement du répertoire contenant les templates (`template_dir`),
* l'emplacement du répertoire de destination comportant tout le site généré (`destination_dir`)

Le lancement de la génération s'effectue ainsi :
```
python main.py
```


### Optimiser les images

Par défaut, le répertoire de destination comportera des sous répertoires `original` et `blur`. Les images du répertoire `blur` servent au [lazy loading](image.html).

Pour générer des images supplémentaires au format voulu, il suffit d'invoquer la méthode `addImageProcessing` :

```
# label : target sub-dir for the resized images
# x : new width (optionnal)
# y : new height (optionnal)
mon_site.addImageProcessing( label='square', x=400, y=400  )
```

Le traitement des images sert à créer des vignettes par exemple. Consulter [ce post](image.html) pour en savoir plus. 

### déployer sur Netlify

Netlify est mon hébergeur préféré pour les sites statiques. En particulier, si votre environnement est dans un dépot git, sa mise à jour déclenchera la re-gérénation de votre site.

Pour mettre en ligne cet exemple avec Netlify, cliquer ici :

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/Herve07h22/tinySSG)

---
titre: Bien débuter avec TinySSG
author: Herve
description: Tiny SSG est un générateur de site statique développé en Python. Ses points forts sont la gestion des images et la facilité d'écriture des layouts au format Jinja2.
layout: Post
---

# Installation

Créer un environnement virtuel et installer les dépendances.

```
git clone xxxxxx
cd tinySSG
python -m venv tinyenv
pip install -r requirements.txt
```

# Création des articles

Les articles et leurs images se trouvent dans les sous répertoires du répertoire `content`.

Chaque sous répertoire contient :
* un fichier *.md au format MarkDown, avec un front-matter contenant des paramètres utiles aux fichiers templates
* un ou plusieurs sous-répertoires, contenant des images.

Chaque fichier MarkDown donnera lieu à la génération d'une page HTML.


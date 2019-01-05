---
titre: Les variables par défaut
author: Herve
description: Tiny SSG génère un fichier HTML par fichier markDown. Il met à disposition des variables utilisables dans les fichiers template.
layout: Post
---

# Liste des variables 

Tiny SSG génère un fichier HTML par fichier markDown. Il met à disposition des variables utilisables dans les fichiers template.

## site

## page

## slug

L'URL de la page statique

## content

Le contenu du fichier MarkDown transformé en HTML. Pour l'afficher dans un template, il suffit d'utiliser la directive :
```
{{ page.content | safe}}
```

## id

Le nom du fichier MardDown.

## createdDate

La date de création du fichier.
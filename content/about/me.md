---
titre: A propos de moi
description: Je suis développeur freelance installé au bord de la mer, dans le Cotentin.
layout: About
slug: about.html
---

## Hello, je suis Hervé de camilab.co

Mais non, cette photo n'est pas la mienne ! 

Il s'agit seulement d'illustrer la façon dont on peut générer une vignette carrée de dimension 400x400 à partir d'une [photo](original/max-nelson-536248-unsplash.jpg) dont la taille initiale est de 6000x4000.
Au passage, le redimensionnement a considérablement allégée la photo, qui passe de 1.9 Mo à 15 Ko !

## Comment faire ?

Pour générer des images redimensionnée, il suffit d'ajouter une seule ligne dans votre générateur :

```python
# Fichier main.py
mon_site.addImageProcessing( label='square', x=400, y=400  )
```

Ceci va créer un sous répertoire `square` dans le répertoire de destination comportant toutes les images du site redimensionnées à la taille de 400x400px.

Consulter le post [sur le traitement des images](image.html) pour en savoir plus sur la façon dont le redimensionnement est réalisé lorsqu'on passe d'une image rectangulaire à une image carrée.

## Qui es-tu ?

Je suis développeur freelance, installée dans le Cotentin à coté de Cherbourg. J'aime coder en Python et en Javascript.
Pour me joindre ou discuter, vous pouvez utiliser le [formulaire de contact](contact.html).  

A bientôt

Hervé

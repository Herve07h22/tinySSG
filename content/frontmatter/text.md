---
titre: Le front-matter
author: Herve
description: Tiny SSG exploite les données d'entête au format front matter. Elle deviennent disponibles dans des variables Python utilisables dans les fichiers template.
layout: Post
---

Dans le fichier MarkDown, il est très utile d'insérer une en-tête comportant des informations utiles. Par exemple : le template à utiliser pour générer la page, un titre, une catégorie, etc...
On utile pour cela le format "Front-Matter", qui est encadré par une succession de trois tirets.

A titre d'exemple, le front matter de ce post est :

```
---
titre: Le front-matter
author: Herve
description: Tiny SSG exploite les données d'entête au format front matter. Elle deviennent disponibles dans des variables Python utilisables dans les fichiers template.
layout: Post
---
```

Ainsi, dans le template qui affiche le post, je peux utiliser la variable `page.titre` pour affiche le titre de mon article.
La variable `layout` est **requise afin de spécifier le fichier template à utiliser pour générer le fichier HTML**. L'extension `.html` est optionnelle. 

Il est aussi possible d'utiliser des structures de données plus complexes, comme des listes. Par exemple, pour spécifier des mot-clés associés à ce post, on pourrait écrire :
```
motcles:
- front-matter
- format
- autre chose
```

La variable `page.motcles` ainsi disponible dans le template sera la liste des 3 mots clés.

Lors de la construction d'une page, TinySSG génére des [variables pré-définies](variables.html). Elles peuvent être remplacées par des valeurs personnalisées dans le front-matter.
Par exemple, tinySSG affecte l'url de la page à la variable `slug`. Mais si `slug` figure parmi les variables du front-matter, alors sa valeur sera celle du front-matter.

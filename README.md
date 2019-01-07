# What is TinySSG ?

Tiny SSG is a static site generator built with Python. 
It can read markdown files, but it has also some interesting features for pre-processing the images.

I made this tool for a client who wanted to turn his website into a static one, in order to improve the security and the performances.
As the original site included more than 300 images, I needed to code something to process all of them in various sizes, 
and to implement a lazy loading. 

Site the demo [here](https://tinyssg.netlify.com)

## Installation

The fastest way to start with tinySSG is to clone the git repo.

```
git clone https://github.com/Herve07h22/tinySSG.git
```

Then install the dependencies in a dedicated virtual environment.

```
cd tinySSG
python -m venv tinyenv
./tinyenv/Script/activate
pip install -r requirements.txt
```

*NB : tinySSG was built with python 3.6.6.*   

Build the example blog to check everything is OK.

```
python main.py
```

That should create a 'dist' directory containing all the files (HTML, css, js).

## Edit the content

It's recommanded to stick to the structure available in the `content` directory (1 sub directory per page).

Far example :

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

Launching the static site generation will :

* generate one HTML page per markdown `.md` file,
* check all the siblings directories containing some images, and attach them to this page. Each image will be copied to the destination directory, in a sub directory named `original`.


## Write the templates

The files in the `templates` directory describe how to generate the HTML pages from the markdown files.
The name of the template file has to be set in the `layout` variable in the head of markdown `.md` file (using front-matter syntax).

The template file will be processed by the [Jinja2](http://jinja.pocoo.org/docs/2.10/) rendering engine.

## Launch the SSG

The static site generation start with the `main.py` script.

```
# -*- coding: utf-8 -*-

from ssg.ssg import ssg
from os.path import join
from os import getcwd

if __name__ =='__main__':
    
    # Create instance of ssg class. Pass the content dir to the constructor.
    mon_site = ssg(contentDir=join(getcwd(), "content"))
    
    # Copy the assets to the destination dir, with renderAssets method
    mon_site.renderAssets( assetDir=join(getcwd(), "assets") , destination_dir=join(getcwd(), "dist") )
    
    # render the site, with render method
    mon_site.render( template_dir=join(getcwd(), "templates") , destination_dir=join(getcwd(), "dist") )
```

The various parameters are the names of the directories that contains :

* the Markdown files and the images (`ContentDir`),
* the css files, js files and all others static assets (`assetDir`). Theses files will simply be copied to the destination directory,
* the template files (`template_dir`),
* the generated files (`destination_dir`)

Just launch the generation like this :
```
python main.py
```


## Images pre-processing

The destination directory will include the default sub directories `original` and `blur`. 
The images in `blur` are the placeholders that are displayed waiting for the lazy loading of the original images.

If you need to display additionnal sizes of the original images, you just have to call the `addImageProcessing` method :

```
# label : target sub-dir for the resized images
# x : new width (optionnal)
# y : new height (optionnal)
mon_site.addImageProcessing( label='square', x=400, y=400  )
```

This pre processing may be very usefull to create some thumbnails for example. 

## Deploy to Netlify

Netlify is my favourite hosting service for static sites. 
If you update a git repo, it gonna launch a new generation of the static website. 

To put the example blog on-line, try this :

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/Herve07h22/tinySSG)


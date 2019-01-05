# -*- coding: utf-8 -*-

from os.path import isfile, splitext, join, basename, isdir, getmtime
from os import listdir, getcwd, walk, mkdir
import markdown2
import frontmatter
from jinja2 import Environment, FileSystemLoader, select_autoescape
from PIL import Image
from shutil import copyfile


class page():
    id = ""
    content = ""
    createdDate = None
    slug=""
    imageFiles = []
    
    def __init__(self, mdFile, contentDir):
        print("creating new page :" + mdFile + " - " + contentDir)
        md_file = join(contentDir, mdFile)
        if isfile(md_file) :
            post = frontmatter.load(md_file)
            self.content =  markdown2.markdown(post.content)
            self.id = basename(contentDir)
            self.slug = self.id+".html"
            self.createdDate = getmtime(md_file)
            for key in post.keys():
                setattr(self,key,post[key])
        if isdir(contentDir):
            for sub_dir in filter(lambda d : isdir(join(contentDir, d)), listdir(contentDir)) :
                setattr(self, sub_dir, [f for f in listdir(join(contentDir, sub_dir)) if isfile(join(contentDir, sub_dir, f)) and splitext(f)[1] != ".md" ])
                self.imageFiles.extend( [ join(contentDir, sub_dir, f) for f in getattr(self,sub_dir) if splitext(f)[1].lower() in (".jpg", ".png") ] )


class ssg():

    # list of pages
    site = []
    images = [ { 'label' : 'original', 'x': None, 'y': None } ]
    asset_env = None

    def buildSite(self, contentDir="/"):
        # walk through the directories and build pages each time a md file is found
        list_of_md_files = [f for f in listdir(contentDir) if isfile(join(contentDir, f)) and splitext(f)[1]==".md" ]
        for md_file in list_of_md_files:
            self.site.append( page(md_file, contentDir) )
        
        list_of_sub_dirs = [f for f in listdir(contentDir) if not isfile(join(contentDir, f)) ]
        for sub_dir in list_of_sub_dirs:
            self.buildSite(join(contentDir, sub_dir))

    def __init__(self, contentDir="/"):
        self.buildSite(contentDir)

    def addImageProcessing(self, label="thumbnails", x=40, y=40):
        # Pre precessing image size to improve perfs
        self.images.append( {'label' : label, 'x':x, 'y':y } )

    def renderAssets(self, assetDir, destination_dir):
        # list all the files in assetDit and sub dirs
        def getAllFiles(filterFunc = lambda f : f):
            for (sourceDir, subDir, foundFiles) in walk(assetDir):
                for foundFile in foundFiles:
                    if filterFunc(foundFile):
                        yield join(sourceDir,foundFile)

        # just copy the others
        print("Copying assets to dist")        
        return list(map( lambda fichier : copyfile(fichier, join(destination_dir, basename(fichier) )), 
                        getAllFiles(filterFunc = lambda f : f ) ))
        

    def render(self, template_dir, destination_dir):
        env = Environment(loader=FileSystemLoader( template_dir ), autoescape=select_autoescape(['html', 'xml']))
        for page in filter(lambda p: hasattr(p, 'layout'),  self.site) :
            
            print("Generating " + page.slug)
            
            # Generating html
            template = env.get_template( page.layout if splitext(page.layout)[1] else page.layout+".html")
            fichier_sortie = open(join(destination_dir, page.slug) , 'w+', encoding='utf-8')
            fichier_sortie.write(template.render(page = page, site=self.site, asset_env=self.asset_env ))
            fichier_sortie.close()

            # generating images
            for imageToProcess in page.imageFiles:
                for imageProperties in self.images:
                    
                    # check if dir already exists
                    if not isdir( join(destination_dir, imageProperties['label']) ):
                        mkdir(join(destination_dir, imageProperties['label']))
                    
                    im = Image.open(imageToProcess)
                    # firstly crop to get the expected ration
                    if imageProperties['x'] and imageProperties['y']:
                        if (float(im.size[0])/float(im.size[1])) > (float(imageProperties['x'])/float(imageProperties['y'])):
                            # we need to crop x
                            xRatio = float(imageProperties['x'])/float(im.size[0])
                            # crop box is a (left, upper, right, lower)-tuple.
                            left = (im.size[0] - imageProperties['x']*float(im.size[1])/float(imageProperties['y']) )/2
                            right = left+imageProperties['x']*float(im.size[1])/float(imageProperties['y'])
                            upper=0
                            lower = im.size[1]
                        else :
                            left=0
                            right = im.size[0]
                            upper = (im.size[1] - imageProperties['y']*float(im.size[0])/float(imageProperties['x']) )/2
                            lower = upper+imageProperties['y']*float(im.size[0])/float(imageProperties['x'])
                        im = im.crop( (int(left), int(upper), int(right), int(lower) ) )
                        
                    im.thumbnail( size=(imageProperties['x'] if imageProperties['x'] else 10000, imageProperties['y'] if imageProperties['y'] else 10000),resample=Image.LANCZOS )
                    im.save(join(destination_dir, imageProperties['label'], basename(imageToProcess)))
                    


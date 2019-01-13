# -*- coding: utf-8 -*-

from ssg.ssg import ssg
from os.path import join
from os import getcwd

if __name__ =='__main__':
    mon_site = ssg(contentDir=join(getcwd(), "content"), exif=False)
    mon_site.addImageProcessing( label='dimension400x200', x=400, y=200  )
    mon_site.addImageProcessing( label='square', x=400, y=400  )
    mon_site.renderAssets( assetDir=join(getcwd(), "assets") , destination_dir=join(getcwd(), "dist") )
    mon_site.render( template_dir=join(getcwd(), "templates") , destination_dir=join(getcwd(), "dist") )
    mon_site.renderServiceWorker( template_dir=join(getcwd(), "templates") , destination_dir=join(getcwd(), "dist") )

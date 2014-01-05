#!/usr/bin/env python

import gdata.photos.service
from pelican import signals

def process_album(albumname):
    username = "dan@zem.org.uk" 
    gd_client = gdata.photos.service.PhotosService()


    albums = gd_client.GetUserFeed(user=username)
    target = None
    for album in albums.entry:
        if album.title.text == albumname:
            target = album

    if not target:
        print "ERROR: Cannot find album %s" % albumname


    photos = gd_client.GetFeed(
            '/data/feed/api/user/%s/albumid/%s?kind=photo&imgmax=1024' % (
            username, target.gphoto_id.text))

    galleryimages = []
    for photo in photos.entry:
        image = {}
        image['thumb'] = photo.media.thumbnail[1].url
        image['image'] = photo.content.src
        galleryimages.append(image)
        
    return galleryimages
        

def add_picasa_article(generator):
    for article in generator.articles:
        if 'picasa' in article.metadata.keys():
            albumname = article.metadata.get('picasa')
            article.album = albumname
            article.galleryimages = process_album(albumname)

def add_picasa_page(generator):
    for page in generator.pages:
        if 'picasa' in page.metadata.keys():
            albumname = page.metadata.get('picasa')
            page.album = albumname
            page.galleryimages = process_album(albumname)

def register():
    signals.article_generator_finalized.connect(add_picasa_article)
    signals.page_generator_finalized.connect(add_picasa_page)

#!/usr/bin/env python

import gdata.photos.service

username = "dan@zem.org.uk" 
albumname = "Gentse Feesten 2013"
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
for photo in photos.entry:
    print 'Photo title:', photo.title.text, photo.content.src
    print photo
    print ""

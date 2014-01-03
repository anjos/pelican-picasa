#!/usr/bin/env python

import gdata.photos.service

username = "dan@zem.org.uk" 
gd_client = gdata.photos.service.PhotosService()


albums = gd_client.GetUserFeed(user=username)
for album in albums.entry:
  print 'title: %s, number of photos: %s, id: %s' % (album.title.text,
      album.numphotos.text, album.gphoto_id.text)

photos = gd_client.GetFeed(
        '/data/feed/api/user/%s/albumid/%s?kind=photo&imgmax=1024' % (
        username, '5903435707841931601'))
for photo in photos.entry:
  print 'Photo title:', photo.title.text, photo.content

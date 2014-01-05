Picasa
======

A plugin for [Pelican](http://blog.getpelican.com/) that pull photo albums from Picasa / Google+ in to a Pelican article or page.

Installation / Configuration
----------------------------

Place the `pelican-picasa` something in your `PELICAN_PATH`. See http://docs.getpelican.com/en/latest/plugins.html for details on using plugins in Pelican.

Add `PICASA_USER` to your `pelicanconf.py` for the default user , e.g.
```
PELICAN_USER='dan@zem.org.uk
```

Usage
-----

Add the `picasa:` metadata tag to a article or post containing the full name of the Album you want to display. e.g.
```
picasa:Gentse Feesten 2013
```

This will generate a list of photos called `galleryimages` that is then available for use within your templates.

Templates
~~~~~~~~~

The following data is available to a template

* `album`: The album name
* `galleryimages`: A list images. Each image is a python dictionary containing the following information:

* `thumb`: A URL to the thumbnail of the image.
* `image`: A URL to the full sized image.

See an example template snippet in `examples/gallery.html`. This can then be included in your other templates with `{% include 'gallery.html' %}`.

Albums owned by other users
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you wish to display an Album owned by a different user, you can specify the user in the article/page using the `picasa-user:` metadata, e.g.
```
picasa-user:foo@example.com
```



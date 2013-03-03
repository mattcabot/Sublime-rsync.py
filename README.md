Features
----------

+   rsync folder on Sublime save
+   custom rsync commands support

Platform
----------
**Mac OS**, **Linux**

Installing
----------
Sublime package [Installation Instructions](https://cancerhermit.github.com/sublime-installation.html)

Usage
----------
plugin looks for **rsync.txt** or **rsync.sh** in folder

#### rsync.txt

edit destignation, for [example](https://github.com/cancerhermit/Sublime-rsync.py/blob/master/rsync.txt):

    ~/Library/Application Support/Sublime Text 2/Packages

every save execute this code

    /usr/bin/rsync -rtu --delete %folder %destignation

#### rsync.sh
**rsync.sh** if exists executes custom code

notice: make rsync.sh executable
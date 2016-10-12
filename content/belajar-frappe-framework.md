Title: Install Frappe Framework id Ubuntu 14.04
Date: 2016-10-12 00:00
Author: egig
Category: Bagi2Pengalaman
Slug: install-frappe-framework-ubuntu-14
Status: draft

Dilihat dari software yang dibutuhkan, rasanya agak ribet kalo di-install di PC yang sudah install macam-macam, jadi saya putuskan untuk buat VM baru Ubuntu 14.04.

Install di ubuntu 14.04

Referensi:
https://github.com/frappe/bench
https://nodejs.org/en/download/package-manager/
http://tecadmin.net/install-mariadb-10-on-ubuntu/
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-redis
https://packages.debian.org/jessie/i386/libjpeg62-turbo/download
sudo apt-get install xfonts-75dpi
sudo apt-get install git
sudo apt-get install python-dev

Traceback (most recent call last):
  File "/usr/local/bin/bench", line 5, in <module>
    from pkg_resources import load_entry_point
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 2749, in <module>
    working_set = WorkingSet._build_master()
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 444, in _build_master
    ws.require(__requires__)
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 725, in require
    needed = self.resolve(parse_requirements(requirements))
  File "/usr/lib/python2.7/dist-packages/pkg_resources.py", line 628, in resolve
    raise DistributionNotFound(req)
pkg_resources.DistributionNotFound: MarkupSafe

easy_install --upgrade pip


Upgrade python: http://askubuntu.com/questions/725171/update-python-2-7-to-latest-version-of-2-x

sudo apt-get install libmariadbclient-dev

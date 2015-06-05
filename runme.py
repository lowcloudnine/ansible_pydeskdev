#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Purpose
-------

To bootstrap a known python environment on any linux system with Python 2.6
or greater.  Then use said environment to install a suite of useful tools
for Python developers.

"""
# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------


from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
from subprocess import call

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse

# -----------------------------------------------------------------------------
# Functions
# -----------------------------------------------------------------------------


def download_file(url, desc=None):
    u = urllib2.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    if not filename:
        filename = 'downloaded.file'
    if desc:
        filename = os.path.join(desc, filename)

    with open(filename, 'wb') as f:
        meta = u.info()
        if hasattr(meta, 'getheaders'):
            meta_func = meta.getheaders
        else:
            meta.get_all

        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print("Downloading: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = "{0:16}".format(file_size_dl)
            if file_size:
                status += "   [{0:6.2f}%]"\
                    .format(file_size_dl * 100 / file_size)
            status += chr(13)
            print(status, end="")
        print()

    return filename

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main():
    """ Runs the script as a stand alone application. """
    # Download Miniconda3
    url='https://repo.continuum.io/miniconda/' + \
        'Miniconda3-latest-Linux-x86_64.sh'
    filename = download_file(url)

    # Install Miniconda3
    pytools_dir = "/opt/py_devtools"
    try:
        os.stat(pytools_dir)
    except:
        os.makedirs(pytools_dir, 755)

    call(['bash', filename, '-b', '-p', pytools_dir + '/miniconda3'])

# -----------------------------------------------------------------------------
# Name
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    main()


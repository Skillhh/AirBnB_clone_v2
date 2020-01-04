#!/usr/bin/python3
""" Generates a .tgz archive from
    web_static
"""
from fabric.api import *
from datetime import datetime
from os import path


def do_pack():
    """ Compress web_static """
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    name = 'versions/web_static_{}.tgz'.format(date)

    try:
        if path.exists('versions') is False:
            local('mkdir versions')
        local('tar -zcvf {} web_static'.format(name))
        return name
    except Exception:
        return None

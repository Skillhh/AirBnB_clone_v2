#!/usr/bin/python3
""" Distributes an archive to your web servers """

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['34.74.157.171', '35.243.248.124']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Deploy to server """
    if path.isfile(archive_path) is False:
        return False

    file_orig = archive_path.split('/')[-1]
    file_dest = file_orig.replace('tgz', '')
    path = '/data/web_static/releases/{}'.format(file_dest)

    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir {}/'.format(path))
        run('sudo tar -xvf /tmp/{} -C {}/'.format(file_orig, path))
        run('sudo rm /tmp/{}'.format(file_orig))
        run('sudo mv {}/web_static/* {}/'.format(path, path))
        run('sudo rm -rf {}/web_static'.format(path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(path))
        print('New version deployed!')
        return True
    except Exception:
        return False

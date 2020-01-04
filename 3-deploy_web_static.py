#!/usr/bin/python3
""" Generates a .tgz archive from
    web_static
"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['34.74.157.171', '35.243.248.124']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """ Deploy to server """
    if path.isfile(archive_path) is False:
        return False

    file_orig = archive_path.split('/')[-1]
    file_dest = file_orig.replace('.tgz', '')
    new = '/data/web_static/releases/{}'.format(file_dest)

    try:
        put(archive_path, '/tmp/')
        run('sudo mkdir {}/'.format(new))
        run('sudo tar -xvf /tmp/{} -C {}/'.format(file_orig, new))
        run('sudo rm /tmp/{}'.format(file_orig))
        run('sudo mv {}/web_static/* {}/'.format(new, new))
        run('sudo rm -rf {}/web_static'.format(new))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/web_static/current'.format(new))
        print('New version deployed!')
        return True
    except Exception:
        return False


def deploy():
    """ Deploy to all Servers """
    try:
        deploy_all = do_pack()
    except Exception:
        return False

    return do_deploy(deploy_all)

#!/usr/bin/python3
"""
distributes an archive to your web servers
"""
import os
from fabric.api import *

env.hosts = ["100.24.255.168", "100.25.161.76"]
env.user = "ubuntu"
env.key = "/root/.ssh/id_rsa"


def do_deploy(archive_path):
    """
    distributes an archive to your web servers
    Args:
        archive_path(str): path to archive to distribute
    Returns:
       Returns True if all operations have been done correctly,
       otherwise returns False
    """
    if not os.path.exists(archive_path):
        return (False)
    try:
        put(archive_path, "/tmp")
        file_name = archive_path.split('/')[-1]
        folder_name = file_name.split('.')[0]
        run('sudo mkdir -p /data/web_static/releases/{}/'.format(folder_name))
        run('sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(file_name, folder_name))
        run('sudo rm /tmp/{}'.format(file_name))
        run('sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(folder_name, folder_name))
        run('sudo rm -rf /data/web_static/releases/{}//web_static/'
            .format(folder_name))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(folder_name))
        return (True)
    except Exception as e:
        return (False)

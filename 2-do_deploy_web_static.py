#!/usr/bin/python3
"""
Fabric script that distributes an archive
"""
import os
from fabric.api import *

env.hosts = ["100.24.255.168", "100.25.161.76"]
env.user = "ubuntu"
env.key = "/root/.ssh/id_rsa"


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return (False)
    try:
        put(archive_path, "/tmp/")
        arch_file = archive_path.split('/')[-1]
        folder = file_name.split('.')[0]
        run("sudo mkdir -p /data/web_static/releases/{}/".format(folder))
        run("sudo tar -xzf {} -C /data/web_static/releases/{}/"
            .format(arch_file, folder))
        run("sudo rm /tmp/{}".format(arch_file))
        run("sudo mv /data/web_static/releases/{}/web_static/*  \
            /data/web_static/releases/{}/".format(folder, folder))
        run("sudo rm -rf /data/web_static/releases/{}/web_static/"
            .format(folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(folder))
        return (True)
    except Exception as e:
        return (False)

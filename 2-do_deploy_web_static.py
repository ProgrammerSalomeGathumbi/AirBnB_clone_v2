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
        run("sudo mkdir -p {}".format(folder))
        run("sudo tar -xzf {} -C {}/".format(arch_file, folder))
        run("sudo rm {}".format(arch_file))
        run("sudo mv {}/web_static/* {}".format(folder, folder))
        run("sudo rm -rf {}/web_static".format(folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder))
        return (True)
    except Exception as e:
        return (False)

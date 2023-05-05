#!/usr/bin/python3
"""
Fabric script that distributes an archive
"""
import os
from fabric.api import *


env.hosts = ["100.24.255.168", "100.25.161.76"]


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if os.path.exists(archive_path):
        put(archive_path, "/tmp/")
        arch_file = os.path.basename(archive_path)
        folder = "/data/web_static/releases/" + arch_file[:-4]
        run("sudo mkdir -p {}".format(folder))
        run("sudo tar -xzf {} -C {}/".format(arch_file, folder))
        run("sudo rm {}".format(arch_file))
        run("sudo mv {}/web_static/* {}".format(folder, folder))
        run("sudo rm -rf {}/web_static".format(folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder))
        return (True)
    return (False)

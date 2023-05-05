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
    if os.path.exists(archive_path):
        arch_file = archive_path.split('/')[1]
        f_file = archive_path.split('.')[0]
        folder = "/data/web_static/releases/{}".format(f_file)
        arch = "/tmp/{}".format(arch_file)
        put(archive_path, arch)
        run("sudo mkdir -p {}".format(folder))
        run("sudo tar -xzf {} -C {}/".format(arch_file, folder))
        run("sudo rm {}".format(arch_file))
        run("sudo mv {}/web_static/* {}".format(folder, folder))
        run("sudo rm -rf {}/web_static".format(folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder))
        print("New version deployed!")
        return (True)
    return (False)

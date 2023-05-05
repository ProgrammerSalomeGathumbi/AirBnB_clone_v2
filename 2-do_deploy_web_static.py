#!/usr/bin/python3
"""
Fabric script that distributes an archive
"""
import os
from fabric.api import *

env.hosts = ["100.24.255.168", "100.25.161.76"]
env.user = "ubuntu"
env.key = "/root/.ssh/id_rsa"


def do_pack():
    """
    Generates a .tgz archive
    """
    try:
        local("mkdir -p versions")
        t = datetime.now().strftime("%Y%m%d%H%M%S")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(t))
        return ("versions/web_static_{}.tgz".format(t))
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if os.path.exists(archive_path):
        arch_file = archive_path[9:]
        folder = "/data/web_static/releases/{}" + arch_file[:-4]
        arch_file = "/tmp/" + arch_file
        put(archive_path, "/tmp/")
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

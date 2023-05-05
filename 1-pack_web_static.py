#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive
from the contents of the web_static
"""
from fabric.api import local
from datetime import datetime


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

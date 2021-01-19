#!/usr/bin/python3
"""fabric script"""
import os
from datetime import datetime
from fabric.api import local


def do_pack():
    """Packs web_static into tgz"""
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + current_time + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + file_path + " web_static")
    if os.path.exists(file_path):
        return file_path
    else:
        return None

def do_deploy(archive_path):
    """ deploy the server """

    if os.path.exists(archive_path):
        
    else:
        return False
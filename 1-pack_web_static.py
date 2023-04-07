#!/usr/bin/python3
<<<<<<< HEAD
'''Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime

from fabric.decorators import runs_once
=======
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import local, runs_once
>>>>>>> f2aa8d8fe1d4219cd873615a987c4b01d464e090


@runs_once
def do_pack():
<<<<<<< HEAD
    '''generates .tgz archive from the contents of the web_static folder'''
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return None
    return path
=======
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    cur_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        cur_time.year,
        cur_time.month,
        cur_time.day,
        cur_time.hour,
        cur_time.minute,
        cur_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output
>>>>>>> f2aa8d8fe1d4219cd873615a987c4b01d464e090

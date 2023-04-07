#!/usr/bin/python3
<<<<<<< HEAD
"""Deploy an archive of static html to my web servers with Fabric3"""

from fabric import api
from fabric.contrib import files
import os


api.env.hosts = ['52.91.154.135', '54.87.207.246']
api.env.user = 'ubuntu'
api.env.key_filename = '~/.ssh/alx_server'


def do_deploy(archive_path):
    """Function to transfer `archive_path` to web servers.
    Args:
        archive_path (str): path of the .tgz file to transfer
    Returns: True on success, False otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    with api.cd('/tmp'):
        basename = os.path.basename(archive_path)
        root, ext = os.path.splitext(basename)
        outpath = '/data/web_static/releases/{}'.format(root)
        try:
            putpath = api.put(archive_path)
            if files.exists(outpath):
                api.run('rm -rdf {}'.format(outpath))
            api.run('mkdir -p {}'.format(outpath))
            api.run('tar -xzf {} -C {}'.format(putpath[0], outpath))
            api.run('rm -f {}'.format(putpath[0]))
            api.run('mv -u {}/web_static/* {}'.format(outpath, outpath))
            api.run('rm -rf {}/web_static'.format(outpath))
            api.run('rm -rf /data/web_static/current')
            api.run('ln -sf {} /data/web_static/current'.format(outpath))
            print('New version deployed!')
        except:
            return False
        else:
            return True
=======
"""A module for web application deployment with Fabric."""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once


env.hosts = ["34.229.67.42", "52.86.76.59"]
"""The list of host server IP addresses."""


@runs_once
def do_pack():
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


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
>>>>>>> f2aa8d8fe1d4219cd873615a987c4b01d464e090

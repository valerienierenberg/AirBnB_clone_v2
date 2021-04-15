#!/usr/bin/python3
""" This module contains a Fabric script that creates and
distributes an archive to your web servers, using the function deploy
"""
from fabric.api import *
from datetime import datetime
from os.path import exists
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


env.hosts = ['34.75.91.40', '34.207.184.116']  # <IP web-01>, <IP web-02>


def deploy():
    """ creates and distributes an archive to your web servers
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result

# The script has the following steps:
# Call the do_pack() function and store the path of the created archive
# Return False if no archive has been created
# Call the do_deploy(archive_path) func, using the path of the new archive
# Return the return value of do_deploy

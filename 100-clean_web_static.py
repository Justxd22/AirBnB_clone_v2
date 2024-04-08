#!/usr/bin/python3
"""Clean."""
from fabric.api import env, local, put, run, lcd, cd
import os

env.hosts = ["52.3.254.46", "100.26.211.242"]


def do_clean(number=0):
    """Delete old Archives."""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

from fabric.api import run
from fabric.api import local

def hello(name="world"):
    print("Hello %s!" % name)
def host_type():
    run('uname -s')


def commit():
    local("git add .")
    local("git commit")

def push():
    local("git push")

def prepare_deploy():
    commit()
    push()

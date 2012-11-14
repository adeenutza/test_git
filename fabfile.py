from fabric.api import run
from fabric.api import local

def hello(name="world"):
    print("Hello %s!" % name)
def host_type():
    run('uname -s')

def prepare_deploy():
	local("git add .")
	local("git commit")
	local("git push")

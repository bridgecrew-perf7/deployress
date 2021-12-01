from typing import Optional

from fastapi import FastAPI

import git
import json
#import docker
import subprocess

#client = docker.from_env()

app = FastAPI()


TARGET_PATH = '/home/ress/ak_notes'
BUILD_TAG = 'alexress/ak_notes/deployress'

@app.get("/")
def read_root():
    return {"Hello": "deploy"}

#@app.get("/ps/list")
#def read_list():
#    l = client.containers.list()
#    formatted = []
#    for c in l:
#        formatted.append({'name': c.name, 'image': c.image.tags, 'status': c.status})
#    return {"containers list": formatted}



@app.get("/deploy")
def aknotes_deploy():
    
    repo = git.Repo(TARGET_PATH)
    # print(repo.git.status())
    o = repo.remotes.origin
    o.pull()

    #img = client.images.build(path=TARGET_PATH, tag=BUILD_TAG)
    #print(img)

    #client.containers.run(BUILD_TAG, detach=True)

    # get running container
    def get_ps() -> str:
        return subprocess.check_output(['docker', 'ps', '-a', '-q', '--filter', f'ancestor={BUILD_TAG}']).decode('ascii').strip()

    def kill_container(id: str) -> None:
        return subprocess.call(['docker', 'kill', id])

    def build_image() -> None:
        return subprocess.call(['docker', 'build', '-t', BUILD_TAG, TARGET_PATH])
    
    def run_container() -> None:
        return subprocess.call(['docker', 'run', '--rm', '-d', '-p', '5001:5001', BUILD_TAG])

    ancestor = get_ps()
    #container = client.containers.get(ancestor)
    #container.kill()

    #client.containers.run(BUILD_TAG, detach=True)
    build_image()
    kill_container(ancestor)
    run_container()
    

    #l = client.images.list()
    #formatted = []
    #for c in l:
    #    formatted.append({'id': c.id, 'tags': c.tags})

    return {"ancestor": ancestor}


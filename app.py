import os
import venv
import subprocess
import git
import time
import shutil
import json


def new_projet(projet_name,virenv=True,git=True):
    with open("config.json", "r") as variable:
        data = json.load(variable)

    working_directory = data['path']
    #loggin = data['githublogin']
    #password = data['githubpass']

    PROJET_PATH = os.path.join(working_directory, projet_name)
    APP_PATH = os.path.join(PROJET_PATH, "app")
    APP_FILE = os.path.join(APP_PATH,"app.py")
    README_FILE = os.path.join(PROJET_PATH,"app.py")
    ENV_PATH = os.path.join(PROJET_PATH,"env")
    #BIN_PATH = os.path.join(ENV_PATH, "bin")

    if not os.path.exists(PROJET_PATH):
        os.mkdir(PROJET_PATH)
        with open(README_FILE, "a"):
            os.utime(APP_FILE, None)

    if not os.path.exists(APP_PATH):
        os.mkdir(APP_PATH)  

    if not os.path.exists(APP_FILE):
        with open(APP_FILE, "a"):
            os.utime(APP_FILE, None)

    if virenv == True:
        if not os.path.exists(ENV_PATH): 
            venv.create(ENV_PATH,with_pip=True)
            time.sleep(2)
            
    os.chdir(PROJET_PATH)
    cmd = 'code .'
    os.system(cmd)
    time.sleep(2)        
        
    if git == True:
        gitignore_origine = "/home/kilann/Documents/Dev_Learning/New_Project_Creator/.gitignore_default"
        gitignore_dest = os.path.join(PROJET_PATH, '.gitignore')
        if not os.path.exists(gitignore_dest):
            with open(gitignore_dest, "a"):
                os.utime(APP_FILE, None)

        shutil.copy2(gitignore_origine, gitignore_dest)
        subprocess.Popen("git init", stdout=subprocess.PIPE, shell=True)
        os.chdir(APP_PATH)
        time.sleep(1)
        subprocess.Popen("git add app.py", stdout=subprocess.PIPE, shell=True)
        time.sleep(1)
        subprocess.Popen("git commit -m 'first commit'", stdout=subprocess.PIPE, shell=True)
    
if __name__ == '__main__':
    projet_name = input("nom du projet: ")
    new_projet(projet_name,virenv=True,git=True)

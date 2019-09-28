import os
import venv
import subprocess

def new_projet(projet_name):
    CUR_DIR = os.path.dirname(__file__)
    PROJET_PATH = os.path.join(CUR_DIR, projet_name)
    APP_PATH = os.path.join(PROJET_PATH, "app")
    APP_FILE = os.path.join(APP_PATH,"app.py")
    ENV_PATH = os.path.join(PROJET_PATH,"env")
    BIN_PATH = os.path.join(ENV_PATH, "bin")

    if not os.path.exists(PROJET_PATH):
        os.mkdir(PROJET_PATH) 

    if not os.path.exists(APP_PATH):
        os.mkdir(APP_PATH)  

    if not os.path.exists(APP_FILE):
        with open(APP_FILE, "a"):
            os.utime(APP_FILE, None)

    if not os.path.exists(ENV_PATH):
        venv.create(ENV_PATH,with_pip=True)
       
if __name__ == '__main__':
    projet_name = input("nom du projet")
    new_projet(projet_name)

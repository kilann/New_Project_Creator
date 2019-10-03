import os
import venv
import subprocess
import git
import time
import shutil
import json
from selenium import webdriver


def new_projet(projet_name,virenv=True,git=True,github=True):
    with open("config2.json", "r") as variable:
        data = json.load(variable)

    working_directory = data['path']
    loggin = data['githublogin']
    password = data['githubpass']

    PROJET_PATH = os.path.join(working_directory, projet_name)
    APP_PATH = os.path.join(PROJET_PATH, "app")
    APP_FILE = os.path.join(APP_PATH,"app.py")
    README_FILE = os.path.join(PROJET_PATH,"app.py")
    ENV_PATH = os.path.join(PROJET_PATH,"env")
    #BIN_PATH = os.path.join(ENV_PATH, "bin")

    if not os.path.exists(PROJET_PATH):
        os.mkdir(PROJET_PATH)

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

    if github == True:
        name = projet_name

        browser = webdriver.Chrome('/home/kilann/Documents/mes_modules/chromedriver')
        browser.get('https://github.com/new')
        time.sleep(1)
        user_name = browser.find_elements_by_xpath("//*[@name='login']")[0]
        user_name.send_keys(loggin)
        user_name = browser.find_elements_by_xpath("//*[@name='password']")[0]
        user_name.send_keys(password)
        user_name = browser.find_elements_by_xpath("//*[@name='commit']")[0]
        user_name.click()
        time.sleep(1)
        user_name = browser.find_elements_by_xpath("//*[@name='repository[name]']")[0]
        user_name.send_keys(name)
        time.sleep(1)
        user_name = browser.find_elements_by_xpath("//*[@data-disable-with='Creating repository…']")[0]
        user_name.click()

        time.sleep(1)
        git_path = browser.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div/div[1]/div[1]/div/div[3]/div/span/input").get_attribute("value")
        browser.close()
        print(git_path)
        time.sleep(1)
        subprocess.Popen("git remote add origin "+ git_path, stdout=subprocess.PIPE, shell=True)
        time.sleep(1)
        subprocess.Popen("git remote -v", stdout=subprocess.PIPE, shell=True)

    
    
if __name__ == '__main__':
    projet_name = input("nom du projet: ")
    new_projet(projet_name,virenv=True,git=True,github=True)

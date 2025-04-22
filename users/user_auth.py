import json
import os
from utils.styling import title,success

DATA_PATH ='data/tasks.json'

def get_username():
    title("Welcome to Personal Task Manager")
    username=input("Enter your name: ").strip().capitalize()

    if os.path.exists(DATA_PATH):
        with open(DATA_PATH,'r') as f:
            try:
                data=json.load(f)
            except json.JSONEncoder:
                data={}
    else:
        data={}    

    if username in data:
        success(f"Welcome back, {username}!")
    else:
        success(f"Helllo {username}, looks like you are are new here!")
        data[username]=[]

        with open(DATA_PATH,'w') as f:
            json.dump(data,f,indent=4)

    return username               

import os
import json

def apply_settings():
    
    path = '../env/ai.json'
    if not os.path.exists(path):
        print(f'File {path} does not exist')
        return
    
    f = open(path)
    settingsJson = json.load(f)    
    del f

    print('Applying os.environ variables:')
    for key in settingsJson:
        print(f'Applying {key}')
        os.environ[key] = settingsJson[key]
        
    del settingsJson
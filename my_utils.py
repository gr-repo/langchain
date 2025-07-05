
####################################################################################
#!pip install requests beautifulsoup4 

import requests
from bs4 import BeautifulSoup
import json

def get_weather(city):    
    # https://github.com/chubin/wttr.in
    # https://wttr.in/Cape Town?format='Temperature (Actual):%t+, Moon Phase:%m, Rain:%p, Wind:%w'"
    return get_url_text(f"https://wttr.in/{city}?format='Temperature (Actual):%t+, Moon Phase:%m, Rain:%p, Wind:%w'")

def get_url_text(url):
    response = requests.get(url)
    return response.text    

def get_all_recipes_com_recipe(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the script tag by id
    script_tag = soup.find("script", id="allrecipes-schema_1-0")

    # Parse and print JSON
    if script_tag:
        data = json.loads(script_tag.string)
        #print(json.dumps(data, indent=2))
        return data
    else:
        print("Script tag not found.")
        return {"error": "Can't find recipe"}
    
from datetime import datetime
import json

def log(message):
    message = '[{}] {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message)
    print(message)

def load_json(name):
    with open(name) as f:
        return json.load(f)

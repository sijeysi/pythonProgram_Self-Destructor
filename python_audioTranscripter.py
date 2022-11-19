import json
from datetime import datetime

r = sr.Recognizer()
run = True
data = {}
with open ("notepad.json", "r") as f:
    data = json.load()
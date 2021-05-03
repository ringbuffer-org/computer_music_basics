#!/usr/bin/env python3

import requests
import json

response = requests.get("https://www.boredapi.com/api/activity")
data     = response.json()
    
print(json.dumps(data, sort_keys=True, indent=4))
    
# print(data["activity"])
.. title: Using APIs with Python
.. slug: using-apis-with-python
.. date: 2020-11-05 13:47:51 UTC
.. tags:
.. category: basics:webaudio
.. priority: 20
.. link:
.. description:
.. type: text
.. priority: 4


Python & APIs
-------------


With the modules ``requests`` and ``json`` it is easy to get data from APIs with Python.
Using the above introduced methods for sequencing, the following example requests a response from  https://www.boredapi.com/:


.. code-block:: python

  #!/usr/bin/env python3

  import requests
  import json

  response = requests.get("https://www.boredapi.com/api/activity")
  data     = response.json()

  print(json.dumps(data, sort_keys=True, indent=4))

  # print(data["activity"])

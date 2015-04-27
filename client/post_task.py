__author__ = 'mpetyx'

import requests

task = {"title": "Clean dishes" }
resp = requests.post('http://apiathens.herokuapp.com/tasks/', data=task)
if resp.status_code != 201:
    raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))
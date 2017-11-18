import pytest, json
from pprint import pprint

def test_wellformedjson():

    data = json.load(open('simplewellformed.json'))
#    pprint(data)
#    data["maps"][0]["id"]
#    data["masks"]["id"]
#    print data["om_points"]
    assert data["om_points"] == 'value'
    assert bool(1) is True

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

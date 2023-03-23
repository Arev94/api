import requests
import pytest
import json
import jsonpath


def test_get_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'

    response = requests.get(base_url + endpoint)

    assert response.status_code == 200, "Status code not math"

def test_create_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    request_json = {
        "id": 0,
        "idBook": 201,
        "firstName": "First Name 610",
        "lastName": "Last Name 610"
    }
    response = requests.post(base_url + endpoint, json=request_json)
    assert response.status_code == 200, "Status code not math"

def test_update_authors():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    request_json = {
        "id": 2,
        "idBook": 201,
        "firstName": "First Name 589",
        "lastName": "Last Name 589"
    }
    response = requests.put(base_url + endpoint + '2', json=request_json)
    assert response.status_code == 200, "Status code not math"

def test_get_authors_books():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    authors_books = "authors/books/"

    response = requests.get(base_url + endpoint + authors_books + "200")
    assert response.status_code == 200, "Status code not math"

def test_get_author():

    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'

    response = requests.get(base_url + endpoint + "1")
    assert response.status_code == 200, "Status code not math"

def test_delete_author():

    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'

    response = requests.delete(base_url + endpoint + '1')
    assert response.status_code == 200, "Status code not math"
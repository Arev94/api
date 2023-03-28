import requests
import pytest
import json
import jsonpath



def url_variables():
    base_url = 'https://fakerestapi.azurewebsites.net/'
    endpoint = 'api/v1/Authors/'
    authors_books = 'authors/books/'

def test_employees():
    base_url = 'https://dummy.restapiexample.com/'
    endpoint = 'api/v1/'
    employees = 'employees/'
    employee = 'employee/'
    new_employee = 'create'
    employee_update = 'update/'
    employee_delete = 'delete/'



def test_get_employees():
    base_url = "https://dummy.restapiexample.com/"
    endpoint = "api/v1/"
    employees = "employees/"

    response = requests.get(base_url + endpoint + employees)
    assert response.status_code == 200, "Status code not math"


def test_get_employee():
    base_url = "https://dummy.restapiexample.com/"
    endpoint = "api/v1/"
    employee = "employee/"

    response = requests.get(base_url + endpoint + employee + "3600")
    assert response.status_code == 200, "Status code not math"
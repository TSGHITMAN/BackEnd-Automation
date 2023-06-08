import requests
from behave import *

from datapayload import *
from utilities.resources import *
from utilities.configuration import *


@given('the Books details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.header = {"Content-Type": "application/json"}
    context.data = dataload("sachin", "789")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.addbook_response = requests.post(context.url, json=context.data, headers=context.header, )


@then('book is successfully added')
def step_impl(context):
    print(context.addbook_response.json())
    response_json = context.addbook_response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json['Msg'] == "successfully added"


@given('the Books details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.header = {"Content-Type": "application/json"}
    context.data = dataload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = ('saching123473@gmail.com', getPassword())
    context.url2 = ApiResources.githubRepo


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(context.url2)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode
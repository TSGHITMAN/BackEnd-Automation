import requests

from utilities.configuration import *
from utilities.resources import *


def after_scenario(context, scenario):
    if "library" in scenario.tags:

        context.url_delete = getConfig()['API']['endpoint'] + ApiResources.deleteBook
        context.response_deleteBook = requests.post(context.url_delete, json={'ID': context.bookId}, headers=context.header, )
        assert context.response_deleteBook.status_code == 200
        res_json = context.response_deleteBook.json()
        print(res_json['msg'])
        assert res_json['msg'] == "book is successfully deleted"

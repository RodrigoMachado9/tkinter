from datetime import datetime
from settings.settings import collection
from bson.objectid import ObjectId
import json

data_mock = [
            {
                'name': 'rodrigo',
                'age': 24,
                'middle_name': 'machado',
                'profession': 'system developer',
                'address': [
                    {
                        'neighboorhood': 'limão',
                        'number': 168,
                        'street': 'Albano Fragoso'
                    }
                ],
                'cell_phone': 952841555,
                'religion': 'christian',
                'hobbie': 'programming',
                'degree': 'bacharelor',
                'meta_data': [
                    {
                        'favorite_color': 'blue',
                        'created_at': 'datetime.now()'
                    }
                ]
            }]


def insert_data(_id):
    res = collection.insert({'jsons': json.dumps(data_mock)})
    print(res)

def find_data(_id):
    for data in collection.find():
        if data.get('jsons'):
            new_data = json.loads(data.get('jsons'))
            print(new_data)
            data_mock[0]['name'] = 'hello world'
            new_data.append(data_mock[0])

            return new_data

def transform_json_and_added_data(_id):
    res = collection.find({'_id': _id})
    print(res)

# insert_data('5e7bfd7973f24cf705a7dd3e')
# transform_json_and_added_data('5e7bfd7973f24cf705a7dd3e')


def update_data(_id, new_data):
    condition = {'_id': ObjectId(_id)}
    myquery = {
        "$set": {
            "jsons": json.dumps(new_data)
        }
    }

    res = collection.update(condition, myquery)
    print('update_res', res)

new_data = find_data('5e7c00d89fa1349a37cbabef')
print(new_data)
# update_data('5e7c00d89fa1349a37cbabef', new_data)



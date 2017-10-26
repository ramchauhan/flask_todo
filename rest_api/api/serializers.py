from flask_restplus import fields
from api.api_provider import api

todo_list = api.model('Todo List post', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of Todo List'),
    'title': fields.String(required=True, description='Todo List Title'),
    'description': fields.String(required=True, description='Todo List description'),
})

item_of_todo_list = api.inherit('Item of Todo List', todo_list)

from flask import request

from flask_restplus import Resource
from api.db_actions import create_todo_list, update_todo_list, delete_todo_list, get_all_records
from api.serializers import todo_list, item_of_todo_list
from api.api_provider import api
from database.models import TodoList

name_space = api.namespace('todolist_apis', description='Todo List Operations')


@name_space.route('/')
class TodoListCollection(Resource):

    @api.marshal_with(item_of_todo_list)
    def get(self):
        """
        Returns list of TodoList
        """
        return get_all_records()

    @api.expect(todo_list, validate=True)
    def post(self):
        """
        Creates new TodoList
        """
        create_todo_list(request.json)
        return request.json, 201


@name_space.route('/<int:id>')
@api.response(404, 'TodoList not found.')
class TodoListItem(Resource):

    @api.marshal_with(item_of_todo_list)
    def get(self, id):
        """
        Returns a TodoList
        """
        return TodoList.query.filter(TodoList.id == id).one()

    @api.expect(todo_list, validate=True)
    @api.response(204, 'TodoList successfully updated.')
    def put(self, id):
        """
        Updates a TodoList.
        """
        data = request.json
        update_todo_list(id, data)
        return None, 204

    @api.response(204, 'TodoList successfully deleted.')
    def delete(self, id):
        """
        Deletes a TodoList.
        """
        delete_todo_list(id)
        return None, 204

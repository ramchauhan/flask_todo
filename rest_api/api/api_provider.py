# Api provider for Rest calls

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

api = Api(version='1.0', title='Todo List Apis',
          description='Basic crud operation for todo list, click on todolist_apis(link) or Show/Hide link for the exploring the apis')


@api.errorhandler(NoResultFound)
def no_result_found_handler(e):
    return {'message': 'There are not result was required but none was found.'}, 404

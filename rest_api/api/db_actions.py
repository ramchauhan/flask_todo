from datetime import datetime
import dateutil.parser

from database import db, reset_database
from database.models import TodoList


def create_todo_list(data):
    title = data.get('title')
    description = data.get('description')
    todo_list = TodoList(title, description)
    db_engine = db.engine
    # check if table not exists then create the table otherwise add the data in the table
    if not db_engine.dialect.has_table(db_engine, 'todo_list'):
        print("==========================Creating the table===============================")
        reset_database()

    db.session.add(todo_list)
    db.session.commit()


def update_todo_list(todo_list_id, data):
    todo_list = TodoList.query.filter(TodoList.id == todo_list_id).one()
    todo_list.title = data.get('title')
    todo_list.description = data.get('description')
    todo_list.action_date = dateutil.parser.parse(data.get('action_date'))
    todo_list.modified_date = datetime.utcnow()
    db.session.add(todo_list)
    db.session.commit()


def delete_todo_list(todo_list_id):
    todo_list = TodoList.query.filter(TodoList.id == todo_list_id).one()
    db.session.delete(todo_list)
    db.session.commit()


def get_all_records():
    db_engine = db.engine
    if not db_engine.dialect.has_table(db_engine, 'todo_list'):
        reset_database()
    return TodoList.query.all()

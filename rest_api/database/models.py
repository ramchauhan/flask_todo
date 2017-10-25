from datetime import datetime

from database import db


class TodoList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    published_date = db.Column(db.DateTime)
    modified_date = db.Column(db.DateTime)
    action_date = db.Column(db.DateTime)    
    

    def __init__(self, title, description, action_date):
        self.title = title
        self.description = description
        self.published_date = datetime.utcnow()
        self.modified_date = datetime.utcnow()
        self.action_date = action_date

    def __repr__(self):
        return '<TodoList %r>' % self.title

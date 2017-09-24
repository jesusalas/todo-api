from sqlalchemy import inspect
from src.db import db


class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<id {0}>'.format(self.id)

    def to_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

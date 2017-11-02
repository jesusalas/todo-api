from sqlalchemy import inspect
from ....db import db

class Todo(db.Model):
    __tablename__ = 'todo'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<id {0}>'.format(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        if self != None:
            db.session.delete(self)
            db.session.commit()
            return self
        return {}

    def to_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    @classmethod
    def fetch_all(cls):
        todos = cls.query.all()
        todo_list = []

        for todo in todos:
            todo_list.append(todo.to_dict())

        return todo_list

    @classmethod
    def find_by_id(cls, id):
        return cls.query.get(id).to_dict() if cls.query.get(id) else {}

    @classmethod
    def create(cls, name):
        return cls(name).save().to_dict() if name != None else {}

    @classmethod
    def remove_by_id(cls, id):
        return cls.query.get(id).delete().to_dict() if cls.query.get(id) else {}
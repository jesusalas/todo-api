from ....db import db


class TodoItem(db.Model):
    __tablename__ = 'todo_item'
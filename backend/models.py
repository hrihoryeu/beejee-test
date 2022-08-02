from datetime import datetime

import sqlalchemy_utils

from extensions import db


class IsActive(db.Model):
    __abstract__ = True

    is_active = db.Column(db.Boolean)


class CreatedAt(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)


class UpdatedAt(db.Model):
    __abstract__ = True

    updated_at = db.Column(db.DateTime(timezone=True), onupdate=datetime.now)


class Note(IsActive, CreatedAt, UpdatedAt):
    __tablename__ = 'note'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(sqlalchemy_utils.EmailType, nullable=False)
    note_text = db.Column(db.String(150), nullable=False)
    is_done = db.Column(db.Boolean, nullable=False)

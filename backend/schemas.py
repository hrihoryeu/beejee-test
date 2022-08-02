from marshmallow_sqlalchemy import auto_field
from marshmallow import validate

from extensions import ma
from models import Note


class NoteSchema(ma.SQLAlchemyAutoSchema):
    """
    {
    "username": "Name LastName",
    "email": "email@email.com",
    "note_text": "Note text",
    "is_done": "True"
}
    """
    class Meta:
        model = Note
        load_instance = True

    id = auto_field()
    username = auto_field()
    email = auto_field(validate=validate.Email())
    note_text = auto_field()
    is_done = auto_field()

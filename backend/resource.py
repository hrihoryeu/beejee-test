from flask import jsonify, request
from flask_restful import Resource

from extensions import db
from models import Note
from schemas import NoteSchema


class NoteResource(Resource):
    def get(self):
        note = (
            db.session.query(Note)
            .all()
        )

        note_data = NoteSchema(many=True).dump(note)

        return jsonify(note_data)

    def post(self):
        request_payload = request.get_json(force=True)

        new_note = NoteSchema().load(request_payload)

        db.session.add(new_note)
        db.session.commit()

        return(jsonify(request_payload))

from models import db, Director
from flask_restx import Resource, Namespace
from schemas import DirectorSchema


ns_directors = Namespace('directors')       # Создание неймспейса


schema_directors = DirectorSchema(many=True)
schema_director = DirectorSchema()                  # Создание экзмепляров схем


@ns_directors.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(Director).all()

        return schema_directors.dump(directors), 200


@ns_directors.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        director = db.session.query(Director).get(pk)

        return schema_director.dump(director), 200

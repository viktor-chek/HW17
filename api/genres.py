from models import db, Genre
from flask_restx import Resource, Namespace
from schemas import GenreSchema


ns_genre = Namespace('genres')          # Создание неймспейса


schema_genres = GenreSchema(many=True)
schema_genre = GenreSchema()                # Создание экзмепляров схем


@ns_genre.route('/')
class GenresView(Resource):
    def get(self):
        genres = db.session.query(Genre).all()

        return schema_genres.dump(genres), 200


@ns_genre.route('/<int:pk>')
class GenreView(Resource):
    def get(self, pk):
        genre = db.session.query(Genre).get(pk)

        return schema_genre.dump(genre), 200


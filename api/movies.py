from flask import request, json
from models import db, Movie
from flask_restx import Resource, Namespace
from schemas import MovieSchema


ns_movie = Namespace('movies')          # Создание неймспейса


schema_movies = MovieSchema(many=True)               # Создание экзмепляров схем
schema_movie = MovieSchema()


@ns_movie.route('/')
class MoviesView(Resource):
    def get(self):
        request_director = request.args.get('director_id', type=int)
        movies = Movie.query.filter(Movie.director_id == request_director).all()

        request_genres = request.args.get('genre_id', type=int)
        movies_for_genres = Movie.query.filter(Movie.genre_id == request_genres).all()

        if request_director:
            return schema_movies.dump(movies), 200

        if request_genres:
            return schema_movies.dump(movies_for_genres), 200

        movies = db.session.query(Movie).all()
        return schema_movies.dump(movies), 200


    def post(self):
        datas = json.loads(request.data)
        movie_new = Movie(**datas)
        with db.session.begin():
            db.session.add(movie_new)

        return "", 201


@ns_movie.route('/<int:pk>')
class MovieView(Resource):
    def get(self, pk):
        movie = db.session.query(Movie).get(pk)

        return schema_movie.dump(movie), 200


    def put(self, pk):
        body_request = json.loads(request.data)
        datas = Movie.query.get(pk)
        datas.title = body_request['title']
        datas.description = body_request['description']
        datas.trailer = body_request['trailer']
        datas.year = body_request['year']
        datas.rating = body_request['rating']
        datas.genre_id = body_request['genre_id']
        datas.director_id = body_request['director_id']
        db.session.add(datas)
        db.session.commit()

        return "", 204


    def delete(self, pk):
        dlt_movie = Movie.query.get(pk)
        db.session.delete(dlt_movie)
        db.session.commit()

        return "", 204

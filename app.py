from flask import Flask
from flask_restx import Api
from api.movies import ns_movie
from api.directors import ns_directors
from api.genres import ns_genre
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                # Настройки проекта
app.config['RESTX_JSON'] = {'ensure_ascii': False}
app.config['JSON_SORT_KEYS'] = False


db.init_app(app)                # Инициализация Alchemy в приложении
app.app_context().push()


api = Api(app)
api.add_namespace(ns_movie)
api.add_namespace(ns_directors)           # Импорт неймспейсов
api.add_namespace(ns_genre)


if __name__ == '__main__':
    app.run(debug=True)

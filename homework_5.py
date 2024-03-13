# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from pydantic import BaseModel
import logging
from enum import Enum


app = FastAPI()
movies = []

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Genre(Enum):
    detective = 'detective'
    novel = 'novel'
    comedy = 'comedy'
    fantasy = 'fantasy'

class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: Genre


@app.get('/')
async def root():
    return {'message': 'Hello, World'}

@app.get('/movies/', response_model=list[Movie])
async def get_movies():
    logger.info("Выполнен вывод всех фильмов")
    return movies

@app.post('/movies/', response_model=Movie)
async def add_movie(movie: Movie):
    movies.append(movie)
    logger.info("Добавлен новый фильм")
    return movie

@app.get('/genre_movies/{genre}/', response_model=list[Movie])
async def get_genre_movies(target_genre):
    target_genre = Genre(target_genre)
    result = []
    for movie in movies:
        if movie.genre == target_genre:
            result.append(movie)
    logger.info("Выполнен вывод всех фильмов по жанру")
    return result



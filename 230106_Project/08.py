import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

genres_json = open("data/genres.json", encoding="UTF8")
genres_list = json.load(genres_json)

# 이하 문제 해결을 위한 코드 작성
movie_info = {}
key_list = ['id', 'title', 'vote_average', 'overview', 'genre_names']
genre_names = []
genre_ids = movie['genre_ids']

for genre in genres_list:
    if genre['id'] in genre_ids:
        genre_names.append(genre['name'])
movie['genre_names'] = genre_names

for key in key_list:
    movie_info[key] = movie[key]

pprint(movie_info)
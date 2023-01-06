import json
from pprint import pprint

# 아래 코드 수정 금지
movie_json = open("data/movie.json", encoding="UTF8")
movie = json.load(movie_json)

# 이하 문제 해결을 위한 코드 작성
movie_info = {}
key_list = ['id', 'title', 'vote_average', 'overview', 'genre_ids']

for key in key_list:
    movie_info[key] = movie[key]

pprint(movie_info)
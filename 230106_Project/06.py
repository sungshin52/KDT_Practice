import json
from pprint import pprint

# 아래 코드 수정 금지
movies_json = open("data/movies.json", encoding="UTF8")
movies_list = json.load(movies_json)

# 이하 문제 해결을 위한 코드 작성
movies_info = {}
movies_info_list = []
key_list = ['id', 'title', 'vote_average', 'overview', 'genre_ids', 'poster_path']

for movie in movies_list:
    for key in key_list:
        movies_info[key] = movie[key]
    movies_info_list.append(movies_info)
    movies_info = {}

pprint(movies_info_list)
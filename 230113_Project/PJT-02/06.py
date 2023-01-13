import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')

def credits(title):
    cast_crew_dict = {'cast': [], 'crew': []}

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': API_KEY,
        'query': title,
        'language': 'ko',
        'region': 'KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()

    movie = response.get('results')

    if (len(movie) <= 0):
        return None

    movie_id = movie[0].get('id')

    cast_path = f'/movie/{movie_id}/credits'
    cast_params = {
        'api_key': '9fa3e8d8bf99d49c77ebd8a4d22302ba',
        'language': 'ko'
    }

    ppl_dict = requests.get(BASE_URL+cast_path, params=cast_params).json()

    for actor in ppl_dict['cast']:
        if (actor['cast_id'] < 10):
            cast_crew_dict['cast'].append(actor['name'])
    
    for crew in ppl_dict['crew']:
        if (crew['department'] == 'Directing'):
            cast_crew_dict['crew'].append(crew['name'])

    return cast_crew_dict


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None

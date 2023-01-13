import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')

def search_movie(title):
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

    else:
        return movie[0].get('id')

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id 반환
    검색한 결과 영화가 없다면 None을 반환
    """
    print(search_movie('기생충'))
    # 496243
    print(search_movie('그래비티'))
    # 959101
    print(search_movie('검색할 수 없는 영화'))
    # None

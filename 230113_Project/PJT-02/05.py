import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')

def recommendation(title):
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

    rec_path = f'/movie/{movie_id}/recommendations'
    rec_params = {
        'api_key': '9fa3e8d8bf99d49c77ebd8a4d22302ba',
        'language': 'ko'
    }

    movies_dict = requests.get(BASE_URL+rec_path, params=rec_params).json().get('results')

    recommend_movies = [movie.get('title') for movie in movies_dict]

    return recommend_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None

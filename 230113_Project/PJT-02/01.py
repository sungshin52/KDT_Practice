import requests
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
API_KEY = os.getenv('API_KEY')

def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': API_KEY,
        'language': 'ko',
        'region': 'KR'
    }

    response = requests.get(BASE_URL+path, params=params).json()
    return len(response['results'])


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20

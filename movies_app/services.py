import requests
from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
from tenacity import retry,stop_after_attempt,wait_fixed
import os

MOVIE_API_URL=os.getenv('MOVIE_API_URL',"https://demo.credy.in/api/v1/maya/movies/")
MOVIE_API_USERNAME=os.getenv('MOVIE_API_USERNAME')
MOVIE_API_PASSWORD=os.getenv('MOVIE_API_PASSWORD')

@retry(stop=stop_after_attempt(3),wait=wait_fixed(3))
def get_movie(page_url=None):
  # username=os.getenv('MOVIE_API_USERNAME')
  # password=os.getenv('MOVIE_API_PASSWORD')

  # retry_strategy=Retry(
  #   total=3,
  #   backoff_factor=0.1, 
  #   status_forcelist=[429,500,502,503,504],
  # )
  # adapter=HTTPAdapter(max_retries=retry_strategy)
  # session=requests.Session()
  # session.mount('https://',adapter)

  # try:
  #   response=session.get(MOVIE_API_URL,auth=(username,password),params={'page':page})
  #   response.raise_for_status()
  #   return response.json()
  # except requests.RequestException as e:
  #   print(f'Error fetching movie: {e}')
  #   return None

  url=page_url or MOVIE_API_URL

  try:
    response=requests.get(url,auth=HTTPBasicAuth(MOVIE_API_USERNAME,MOVIE_API_PASSWORD),timeout=5,verify=False)
    response.raise_for_status()
    return response.json()
  except requests.RequestException as e:
    print(f'An error occurred while fetching movie: {e}')
    raise

# def fetch_all_movies():
#   page=1
#   movies=[]
#   while True:
#     data=get_movie(page)
#     if data and 'data' in data:
#       movies.extend(data['data'])
#       if(data['next']):
#         page+=1
#       else:
#         break
#     else:
#       break
#   return movies
import requests

OULU_GET_VOCABULARY_BOOKS = f'https://api.frdic.com/api/open/v1/studylist/category'
"""
  {
  "data": [
      {
      "id": "0",
      "language": "en",
      "name": "我的生词本"
      },
      {
      "id": "132303016416635230",
      "language": "en",
      "name": "nanana3"
      },
      {
      "id": "132303016647118400",
      "language": "en",
      "name": "新的名称"
      }
  ],
  "message": ""
  }
"""
OULU_GET_WORD = f'https://api.frdic.com/api/open/v1/studylist/words'
"""
  {
  "data": [
      {
      "word": "action",
      "exp": "n. 行动；活动；功能；情节；战斗"
      },
      {
      "word": "and",
      "exp": "conj. 和，与；而且；然后；就；但是"
      }
  ],
  "message": ""
  }
"""
OULU_AUTHORIZATION = f'NIS WLj0gOA3wFGER4+2+PJzURvnSm12SqIgQEcSZpWB7x5E9hLO60aj0g=='

NOTION_SECRETS = f'secret_ycQG15vyl8v5LdQz2BrgB4XzxN3jn0WgCEhM6ABozIH'
NOTION_DATABASE_ID = f'7c136664ec514a49891a2fe89d3db5b6'


def get_vocabulary_books():
    """
    获取所有生词本
    :return: 生词本列表
    """
    headers = {"Authorization": OULU_AUTHORIZATION}
    params = 'language=en'
    response = requests.get(OULU_GET_VOCABULARY_BOOKS, headers=headers, params=params)
    if response.status_code == 200:
        vocabulary_books = response.json()
        return vocabulary_books["data"]


def get_words(id):
    """
    获取生词本中所有单词
    :return: 单词列表
    """
    headers = {"Authorization": OULU_AUTHORIZATION}
    params = 'language=en&page=0&page_size=100000&id=' + id
    response = requests.get(OULU_GET_WORD, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]




import requests
import constants


def get_vocabulary_books():
    """
    获取所有生词本
    :return: 生词本列表
    """
    headers = {"Authorization": constants.OULU_AUTHORIZATION}
    params = 'language=en'
    response = requests.get(constants.OULU_GET_VOCABULARY_BOOKS, headers=headers, params=params)
    if response.status_code == 200:
        vocabulary_books = response.json()
        return vocabulary_books["data"]


def get_words(id):
    """
    获取生词本中所有单词
    :return: 单词列表
    """
    headers = {"Authorization": constants.OULU_AUTHORIZATION}
    params = 'language=en&page=0&page_size=100000&id=' + id
    response = requests.get(constants.OULU_GET_WORD, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()["data"]

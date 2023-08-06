from notion_client import Client

import constants


def get_all_pages():
    """
    获取数据库中所有page
    :return: page列表
    """
    client = Client(auth=constants.NOTION_SECRETS)
    databases = client.databases.query(constants.NOTION_DATABASE_ID)
    return databases["results"]


def update_word(page_id, word, translation, node):
    """
    更新单词
    :param page_id: id 
    :param word: 单词
    :param translation: 翻译
    :param node: 笔记
    :return: None
    """
    page_update_entity = {
        "properties": {
            "Word": {"title": [{"text": {"content": word}, "plain_text": word}]},
            "Translation": {"rich_text": [{"text": {"content": translation}, "plain_text": translation}]},
            "Node": {"rich_text": [{"text": {"content": node}, "plain_text": node}]}
        }
    }
    client = Client(auth=constants.NOTION_SECRETS)
    client.pages.update(page_id=page_id, **page_update_entity)


def insert_word(word, translation, node):
    """
    添加单词
    :param word: 单词
    :param translation: 翻译
    :param node: 笔记
    :return: None
    """
    page_insert_entity = {
        "properties": {
            "Word": {"title": [{"text": {"content": word}, "plain_text": word}]},
            "Translation": {"rich_text": [{"text": {"content": translation}, "plain_text": translation}]},
            "Node": {"rich_text": [{"text": {"content": node}, "plain_text": node}]}
        },
        "parent": {"type": "database_id", "database_id": constants.NOTION_DATABASE_ID}
    }
    client = Client(auth=constants.NOTION_SECRETS)
    client.pages.create(**page_insert_entity)


def get_words_from_databases():
    """
    读取数据库中所有数据到full-properties.json文件中
    :return: 数据库中的所有单词
    """
    pages = get_all_pages()
    words = {}
    for page in pages:
        translation = page["properties"]["Translation"]["rich_text"][0]["text"]["content"]
        word = page["properties"]["Word"]["title"][0]["text"]["content"]
        words[word] = translation
    return words
